#!/usr/bin/python3
"""Module to add two numbers (integers or floats)."""


def add_integer(a, b=98):
    """Adds two numbers and returns an integer.

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number (default 98).

    Returns:
        int: Sum of a and b after converting floats to int.

    Raises:
        TypeError: If a or b are not int or float.
        OverflowError: If a float cannot be converted to int (inf, -inf, NaN).
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        a_int = int(a)
        b_int = int(b)
    except (OverflowError, ValueError):
        raise OverflowError("cannot convert float infinity to integer")

    return a_int + b_int
