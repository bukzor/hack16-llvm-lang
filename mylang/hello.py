import os
from subprocess import Popen, PIPE
from tempfile import mkstemp

from mylang.lex import lex
from mylang.parse import parse
from mylang.compile import compiler
from mylang.interpret import interpret


def hello(source):
    return interpret(str(compiler(parse(lex(source)))))

def hic(source):
    llsource = str(compiler(parse(lex(source))))

    _, s = mkstemp('.s')
    interpreter = Popen(('llc', '-o', s), stdin=PIPE)
    interpreter.communicate(llsource)
    assert interpreter.returncode == 0, interpreter.returncode

    clang = Popen(('clang', s))
    clang.wait()
    assert clang.returncode == 0, clang.returncode
    os.unlink(s)
