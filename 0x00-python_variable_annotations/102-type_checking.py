#!/usr/bin/env python3
"""Defines a type-annotated function zoom_array."""
from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Takes a tuple and an integer factor and returns a list."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
