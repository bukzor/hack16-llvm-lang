from mylang import ast
from mylang import tokens


def parse(lexemes):
    # TODO-TEST: other ID's (eg no) do nothing
    result = ast.Module()
    lexemes = iter(lexemes)
    for lexeme in lexemes:
        if lexeme == tokens.ID('hello'):
            result = type(result)(*(result.datas + (ast.Hello(),)))
        elif lexeme == tokens.ID('print'):
            string_arg = print_arg(lexemes)
            result = type(result)(*(result.datas + (ast.Print(), ast.String(string_arg))))
    return result


def print_arg(lexemes):
    arg_value = ''
    for lexeme in lexemes:
        if type(lexeme) is tokens.WS:
            value = lexeme.datas[0]
            if '\n' in value:
                left = value.split('\n')[0]
                arg_value += left
                return arg_value
            arg_value += value
        elif type(lexeme) is tokens.ID:
            arg_value += lexeme.datas[0]
    return arg_value
