"""Simple calculator helper functions."""

# Exemplary calculator functions
import builtins


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of two integers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the quotient of two numbers as float."""
    return a / b


def to_binary(a: int) -> int:
    """Return the binary representation of an integer."""
    if not isinstance(a, int):
        raise TypeError("Input must be an integer.")
    if a < 0 or a > 100:
        raise ValueError("Input must be between 0 and 100.")
    return int(builtins.bin(a)[2:])
