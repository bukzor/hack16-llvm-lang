import os
from subprocess import Popen, PIPE
from tempfile import mkstemp


def interpret(llsource):
    _, s = mkstemp('.s')
    interpreter = Popen(('llc', '-o', s), stdin=PIPE)
    interpreter.communicate(llsource)
    assert interpreter.returncode == 0, interpreter.returncode

    _, exe = mkstemp('.exe')
    compiler = Popen(('clang', s, '-o', exe))
    compiler.wait()
    assert compiler.returncode == 0, compiler.returncode
    os.unlink(s)

    process = Popen((exe,), stdout=PIPE)
    output, _ = process.communicate()
    assert process.returncode == 0, (process.returncode, output)
    os.unlink(exe)

    return output
