"""Python math functions"""
import math


def convert_to_base(decimal_number, base, digits):
    """Converts decimal numbers to strings of a custom base using custom digits."""
    if decimal_number == 0:
        return ''
    return digits[decimal_number % base] + convert_to_base(decimal_number // base, base, digits)
  
def base_to_dec(string, base, digits):
    """Converts strings to decimal numbers via a custom base and digits."""
    if string == '':
        return 0
    return digits.index(string[0]) + base_to_dec(string[1:], base, digits) * base

def sigmoid(x):
    """A Python function for the Sigmoid function."""
    return 1 / (1 + math.exp(-x))

def inverse_sigmoid(y):
    """A Python function for the inverse of the Sigmoid function."""
    return math.log(y / (1 - y))