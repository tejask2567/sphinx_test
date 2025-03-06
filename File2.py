"""
File2.py - This module contains example classes for Sphinx documentation.
"""

class Calculator:
    """
    A simple calculator class.
    """

    def add(self, a: int, b: int) -> int:
        """
        Adds two numbers.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The sum of a and b.
        """
        return a + b

    def multiply(self, a: int, b: int) -> int:
        """
        Multiplies two numbers.

        Args:
            a (int): The first number.
            b (int): The second number.

        Returns:
            int: The product of a and b.
        """
        return a * b


class Converter:
    """
    A simple converter class for units.
    """

    def km_to_miles(self, km: float) -> float:
        """
        Converts kilometers to miles.

        Args:
            km (float): Distance in kilometers.

        Returns:
            float: Distance in miles.

        Example:
            >>> Converter().km_to_miles(5)
            3.10686
        """
        return km * 0.621371

    def miles_to_km(self, miles: float) -> float:
        """
        Converts miles to LM.

        Args:
            miles (float): Distance in miles.

        Returns:
            float: Distance in KM.

        Example:
            >>> Converter().km_to_miles(5)
            3.10686
        """
        return miles * 0.621371
    
    
class Converter_2:
    """
    A simple converter class for units.
    """

    def km_to_miles(self, km: float) -> float:
        """
        Converts kilometers to miles.

        Args:
            km (float): Distance in kilometers.

        Returns:
            float: Distance in miles.

        Example:
            >>> Converter().km_to_miles(5)
            3.10686
        """
        return km * 0.621371

    def miles_to_km(self, miles: float) -> float:
        """
        Converts miles to LM.

        Args:
            miles (float): Distance in miles.

        Returns:
            float: Distance in KM.

        Example:
            >>> Converter().km_to_miles(5)
            3.10686
        """
        return miles * 0.621371