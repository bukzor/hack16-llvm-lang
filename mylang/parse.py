from mylang import ast
from mylang import tokens


def parse(lexemes):
    # TODO-TEST: other ID's (eg no) do nothing
    result = ast.Module()
    for lexeme in lexemes:
        if lexeme == tokens.ID('hello'):
            result = type(result)(*(result.datas + (ast.Hello(),)))
    return result
