from src.converter import Converter

def test_converter():
    converter = Converter()
    converter.fit(["Hi!", "Hello World!", "foo", "bar"])
    assert converter.itos(converter.stoi("foobar")) == "foobar"