#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the specified multiplier.

    :param multiplier: The multiplier (a float)
    :return: A function that multiplies a float by the multiplier
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
