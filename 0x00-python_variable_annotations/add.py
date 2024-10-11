#!/usr/bin/env python3

def add(a: float, b: float) -> float:
    """
    Function to add two float numbers.

    :param a: first float number
    :param b: second float number
    :return: sum of a and b as a float
    """
    return a + b
if __name__ == "__main__":
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
