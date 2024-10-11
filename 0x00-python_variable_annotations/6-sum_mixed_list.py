#!/usr/bin/env python3
"""
This module provides a function to sum a list of mixed integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums the elements of a mixed list of integers and floats and returns the result.

    :param mxd_lst: A list of integers and/or floats
    :return: The sum of the elements as a float
    """
    return float(sum(mxd_lst))
