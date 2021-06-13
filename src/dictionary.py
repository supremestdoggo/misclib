"""Dictionary functions"""
def dict_sort(dictionary: dict) -> list:
    """Takes in a dictionary with integer values and outputs a list of the keys sorted by their associated values in descending order."""
    return list(reversed(sorted(dictionary, key=dictionary.__getitem__)))

def dict_index(dictionary: dict, value) -> str:
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    return keys[values.index(value)]