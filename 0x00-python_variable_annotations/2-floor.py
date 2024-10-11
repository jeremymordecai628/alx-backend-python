#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a float number.
"""

import math

def floor(n: float) -> int:
    """
    Returns the floor of the given float.

    :param n: The float number
    :return: The floor of the float as an integer
    """
    return math.floor(n)
if __name__ == "__main__":
    ans = floor(3.14)

print(ans == math.floor(3.14))
print(floor.__annotations__)
print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))

