#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represents a class: BaseGeometry."""

    def area(self):
        """ Method that defines the area of a geomtric shape """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Args:
            name: Variable name.
            value: Value of the variable.
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
