#!/usr/bin/env python3
"""Defines a type-annotated function element_length"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable object as argument and returns a list of tuples"""
    return [(i, len(i)) for i in lst]
