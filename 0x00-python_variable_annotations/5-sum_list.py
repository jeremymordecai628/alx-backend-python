#!/usr/bin/env python3
"""
This module provides a function to sum a list of floats.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums the elements of a list of floats and returns the result.

    :param input_list: A list of float numbers
    :return: The sum of the floats as a float
    """
    return sum(input_list)
