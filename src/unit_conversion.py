"""Converts various units back and forth."""
def c_to_f(c) -> float:
    """Converts Celsius degrees to Fahrenheit degrees."""
    return c * 9/5 + 32

def f_to_c(f) -> float:
    """Converts Fahrenheit degrees to Celsius degrees."""
    return (f - 32) * 5/9

def m_to_ft(m) -> float:
    """Converts meters to feet."""
    return m * 3.28084

def ft_to_m(ft) -> float:
    """Converts feet to meters"""
    return ft / 3.28084