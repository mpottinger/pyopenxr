# This script creates an updated version of xr/constants.py

from clang.cindex import CursorKind
import typing
import xrg


def main():
    cg = xrg.CodeGenerator([
        CursorKind.FUNCTION_DECL,
    ])
    cg.print_header()
    print("from .library import openxr_loader_library")
    for fn in cg.items:
        assert isinstance(fn, xrg.FunctionItem)
        fn = typing.cast(xrg.FunctionItem, fn)
        print("")
        print(fn.ctypes_string())
    cg.print_all_list(py=False)


if __name__ == "__main__":
    main()