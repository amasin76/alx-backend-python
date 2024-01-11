#!/usr/bin/env python3
"""Defines a type-annotated function safe_first_element."""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Takes a sequence as argument and returns the first element or None"""
    if lst:
        return lst[0]
    else:
        return None
