from mylang.lex import lex
from mylang import tokens


def test_lex_null():
    assert lex('') == []


def test_lex_hello():
    assert lex('hello') == [tokens.ID('hello')]


def test_lex_print():
    assert lex('print butt fart\n') == [
        tokens.ID('print'),
        tokens.WS(' '),
        tokens.ID('butt'),
        tokens.WS(' '),
        tokens.ID('fart'),
        tokens.WS('\n'),
    ]


def test_lex_hello_whitespace():
    assert lex('\n\n   hello\n\t') == [tokens.WS('\n\n   '), tokens.ID('hello'), tokens.WS('\n\t')]
