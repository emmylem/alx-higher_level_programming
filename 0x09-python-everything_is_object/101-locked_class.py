#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """Prevent the user from instantiating new LockedClass attributes
    except first_name."""
    lock = ["first_name"]
