#!/usr/bin/env python3
"""Defines a type-annotated function safely_get_value."""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """
    Takes a mapping, a key and a default value and returns the value of the key
    or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
