"""Dictionary functions"""
def dict_sort(dictionary):
    """Takes in a dictionary with integer values and outputs a list of the keys sorted by their associated values in descending order."""
    return list(sorted(dictionary, key=dictionary.__getitem__, reverse=True))

def dict_index(dictionary, value) -> str:
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    return keys[values.index(value)]


class BetterDict(object):
    """"An improved version of the dictionary class containing the dictionary functions in this module."""
    def __init__(self, keys, values):
        self.__keys = keys
        self.__values = values
    
    def __getitem__(self, key):
        if key not in self.__keys:
            raise IndexError(f"Key \'{key}\' not in keys.")
        pos = self.__keys.index(key)
        return self.__values[pos]
    
    def __setitem__(self, key, value):
        self.__keys[key] = key
        self.__values = value
    
    def __delitem__(self, key):
        if key not in self.__keys:
            raise IndexError(f"Key \'{key}\' not in keys.")
        pos = self.__keys.index(key)
        del self.__keys[pos]
        del self.__values[pos]
    
    def keys(self):
        return self.__keys
    
    def values(self):
        return self.__values
    
    def index(self, value):
        pos = self.__values.index(value)
        return self.__keys[pos]