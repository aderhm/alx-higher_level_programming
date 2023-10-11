#!/usr/bin/python3
"""Defines a class Rectangle."""


class MyInt(int):
    """Represents a class: MyInt."""

    def __eq__(self, other):
        """Inverting the == operator"""
        return (int.__ne__(self, other))

    def __ne__(self, other):
        """Inverting the != operator"""
        return (int.__eq__(self, other))
