from ctypes import Array, byref, c_uint32

from . import raw_functions  # Side effect of defining low-level c signatures
from .enums import *
from .exceptions import check_result
from .typedefs import *


# function transformations:
#  * brief docstring
#  * parameter docstring
#  * exception docstring
#  * output_array_parameters
#  * check result
#  * string input parameter


def enumerate_instance_extension_properties(
    layer_name: str = None,
) -> Array[ExtensionProperties]:
    """
    Returns properties of available instance extensions

    :param layer_name: is either NULL or a pointer to a string naming the API layer to retrieve extensions from,
        as returned by xrEnumerateApiLayerProperties.
    :return: an array of XrExtensionProperties

    On failure, this command raises
        XR_ERROR_VALIDATION_FAILURE
        XR_ERROR_RUNTIME_FAILURE
        XR_ERROR_OUT_OF_MEMORY
        XR_ERROR_SIZE_INSUFFICIENT
        XR_ERROR_RUNTIME_UNAVAILABLE
        XR_ERROR_API_LAYER_NOT_PRESENT
    """
    # First call returns the item count
    if layer_name is not None:
        layer_name = layer_name.encode()

    extension_count = c_uint32(0)
    fn = raw_functions.xrEnumerateInstanceExtensionProperties
    result = check_result(fn(layer_name, 0, byref(extension_count), None))
    if result.is_exception():
        raise result

    properties_type = ExtensionProperties * extension_count.value
    properties = properties_type()

    # TODO: automatically initialize?
    for p in properties:
        p.type = StructureType.EXTENSION_PROPERTIES.value

    result = check_result(
        fn(
            layer_name,
            extension_count,
            byref(extension_count),
            properties,  # Don't use byref for arrays...
        )
    )
    if result.is_exception():
        raise result

    return properties


__all__ = [
    "enumerate_instance_extension_properties",
]
