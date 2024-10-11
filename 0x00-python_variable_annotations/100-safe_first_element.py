#!/usr/bin/env python3
"""
This module provides a function to safely return the first element of a list or None if the list is empty.
"""

from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list if it exists, otherwise returns None.

    :param lst: A sequence of elements of any type
    :return: The first element of the list if available, otherwise None
    """
    if lst:
        return lst[0]
    else:
        return None
