from mylang import tokens
from mylang.parse import parse
from mylang import ast

def test_parse_null():
    assert parse([]) == ast.Module()


def test_parse_hello():
    assert parse([tokens.ID('hello')]) == ast.Module(ast.Hello()) 


def test_parse_hello():
    assert parse([tokens.WS('\n\n   '), tokens.ID('hello'), tokens.WS('\n\t')]) == ast.Module(ast.Hello()) 
