from src.math import convert_to_base, base_to_dec
from src.dictionary import dict_sort

class Converter:
    """A class to convert strings to compact integers using a custom codec/lookup."""
    def __init__(self, lookup=None):
        if lookup == None:
            self.lookup = {}
        else:
            self.lookup = lookup
        self.codec = ''.join(dict_sort(lookup))
    
    @classmethod
    def from_codec(codec: str):
        """Creates a Converter object from a string codec."""
        lookup = {}
        for x in range(len(codec)):
            lookup[codec[x]] = x + 1
        return Converter(lookup)
    
    def fit(self, strings):
        """Takes in a string or list of strings, and changes the lookup/codec to fit the string(s)."""
        if type(strings) == list:
            string = '\n'.join(strings)
        else:
            string = strings
        # Find and count characters
        for x in string:
            if x not in self.lookup:
                self.lookup[x] = string.count(x)
            else:
                self.lookup[x] = self.lookup.get(x) + string.count(x)
        if type(strings) == list:
            self.lookup['\n'] = self.lookup.get('\n') - len(strings) + 1 # Correct \n count
            if self.lookup.get('\n') == 0:
                del self.lookup['\n']
        self.codec = ''.join(dict_sort(self.lookup))
    
    def stoi(self, string: str) -> int:
        """Converts strings to integers based on the lookup/codec."""
        return base_to_dec(string, len(self.codec), self.codec)
    
    def itos(self, number: int) -> str:
        """Converts integers to strings based on the lookup/codec."""
        return convert_to_base(number, len(self.codec), self.codec)
    
    def __str__(self):
        return "Converter({})/Converter.from_codec({})".format(self.lookup, self.codec)