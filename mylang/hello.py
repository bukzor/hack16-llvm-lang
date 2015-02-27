from mylang.lex import lex
from mylang.parse import parse
from mylang.compile import compiler
from mylang.interpret import interpret

def hello(source):
    return interpret(str(compiler(parse(lex(source)))))
