#!/usr/bin/env python3
def concat(str1: str, str2: str) -> str:
    """
    Function to concatenate two strings.

    :param str1: first string
    :param str2: second string
    :return: concatenated result of str1 and str2
    """
    return str1 + str2

if __name__ == "__main__":
    str1 = "egg"
    str2 = "shell"

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
