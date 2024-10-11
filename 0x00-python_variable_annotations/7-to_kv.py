#!/usr/bin/env python3
"""
This module provides a function to return a tuple containing a string and the square of a number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the first element being the string k and the second element being
    the square of the number v as a float.

    :param k: The string key
    :param v: The number (int or float) to be squared
    :return: A tuple (k, v^2)
    """
    return k, float(v ** 2)
