#!/usr/bin/env python3
"""
This module provides a function that returns a list of tuples containing an element and its length.
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from the input list and its length.

    :param lst: An iterable of sequences (e.g., strings, lists, etc.)
    :return: A list of tuples, where each tuple contains a sequence and its length
    """
    return [(i, len(i)) for i in lst]
