# misclib
`misclib` is a package of miscellaneous useful functions. It contains three modules, `converter`, `math`, and `unit_conversion`.
## converter
This module mainly centers around the `Converter` class, a class for compact integer-string conversion. It also contains the `dict_sort` function, which returns a list of a dictionary's keys sorted by their associated values in decending order.
### `Converter`
#### `fit`
This will fit the `Converter`'s codec to fit the inputted string or list of strings.
#### `stoi`
Converts strings (`str`) to integers (`int`).
#### `itos`
Reverse of `stoi`.
### `dict_sort`
Takes in a dictionary, and returns a list of the keys sorted by their values in decending order.
## `math`
This module is mainly just for containing math-related functions, such as the Sigmoid function and its inverse.
### `sigmoid`
Takes in an integer or float `x` and outputs a float between 0 and 1.
### `inverse_sigmoid`
Takes in a float `y` between 0 and 1 and outputs a value based on the inverse of the sigmoid function.
### `convert_to_base`
Converts a integer to a string of characters using a custom base and digits.
### `base_to_dec`
Reverse of `convert_to_base`.
## `unit_conversion`
Converts various units back and forth.
### `c_to_f`
Converts Celsius degrees to Fahrenheit degrees.
### `f_to_c`
Reverse of `c_to_f`.
### `m_to_ft`
Converts meters to feet.
### `ft_to_m`
Reverse of `m_to_ft`.