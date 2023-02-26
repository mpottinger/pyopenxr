"""
`xr` is the top level module of the pyopenxr unofficial python bindings for the
OpenXR SDK to access VR and AR devices.
"""

from . import (
    version,
    constants,
    enums,
    typedefs,
    functions,
    platform,
    exception,
    classes,
    context_object,
    matrix4x4f,
)

from .version import *
from .constants import *
from .enums import *
from .typedefs import *
from .functions import *
from .platform import *
from .exception import *
from .classes import *
from .context_object import *
from .matrix4x4f import *


# from .experiment import *

__all__ = []

for subpackage in (
    version,
    constants,
    enums,
    typedefs,
    functions,
    platform,
    exception,
    classes,
    context_object,
    matrix4x4f,
):
    __all__ += subpackage.__all__

__version__ = version.PYOPENXR_VERSION  # Not in __all__, right?
