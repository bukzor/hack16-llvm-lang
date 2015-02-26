from mylang import tokens


def test_hello():
    assert repr(tokens.ID('hello')) == "ID('hello',)"


def test_ws():
    assert repr(tokens.WS(' \n \t ')) == r"WS(' \n \t ',)"
