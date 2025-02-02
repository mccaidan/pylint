# Licensed under the GPL: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# For details: https://github.com/PyCQA/pylint/blob/main/LICENSE
# Copyright (c) https://github.com/PyCQA/pylint/blob/main/CONTRIBUTORS.txt

"""A collection of typing utilities."""

from __future__ import annotations

import sys
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Dict,
    Iterable,
    NamedTuple,
    Pattern,
    Tuple,
    Type,
    TypeVar,
    Union,
)

if sys.version_info >= (3, 8):
    from typing import Literal, TypedDict
else:
    from typing_extensions import Literal, TypedDict

if TYPE_CHECKING:
    from astroid import nodes

    from pylint.checkers import BaseChecker
    from pylint.config.callback_actions import _CallbackAction


class FileItem(NamedTuple):
    """Represents data about a file handled by pylint.

    Each file item has:
    - name: full name of the module
    - filepath: path of the file
    - modname: module name
    """

    name: str
    filepath: str
    modpath: str


class ModuleDescriptionDict(TypedDict):
    """Represents data about a checked module."""

    path: str
    name: str
    isarg: bool
    basepath: str
    basename: str


class ErrorDescriptionDict(TypedDict):
    """Represents data about errors collected during checking of a module."""

    key: Literal["fatal"]
    mod: str
    ex: ImportError | SyntaxError


class MessageLocationTuple(NamedTuple):
    """Tuple with information about the location of a to-be-displayed message."""

    abspath: str
    path: str
    module: str
    obj: str
    line: int
    column: int
    end_line: int | None = None
    end_column: int | None = None


class ManagedMessage(NamedTuple):
    """Tuple with information about a managed message of the linter."""

    name: str | None
    msgid: str
    symbol: str
    line: int | None
    is_disabled: bool


MessageTypesFullName = Literal[
    "convention", "error", "fatal", "info", "refactor", "statement", "warning"
]
"""All possible message categories."""


OptionDict = Dict[
    str,
    Union[
        None,
        str,
        bool,
        int,
        Pattern[str],
        Iterable[Union[str, int, Pattern[str]]],
        Type["_CallbackAction"],
        Callable[[Any], Any],
        Callable[[Any, Any, Any, Any], Any],
    ],
]
Options = Tuple[Tuple[str, OptionDict], ...]


AstCallback = Callable[["nodes.NodeNG"], None]
"""Callable representing a visit or leave function."""

CheckerT_co = TypeVar("CheckerT_co", bound="BaseChecker", covariant=True)
AstCallbackMethod = Callable[[CheckerT_co, "nodes.NodeNG"], None]
"""Callable representing a visit or leave method."""
