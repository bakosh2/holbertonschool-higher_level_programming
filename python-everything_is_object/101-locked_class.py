#!/usr/bin/python3
"""Module that defines a LockedClass."""


class LockedClass:
    """Prevents dynamic creation of instance attributes except first_name."""

    __slots__ = ["first_name"]
