from __future__ import unicode_literals

from mylang import ast as AST

import string
_VALID_CHARS = (frozenset(ord(c) for c in string.ascii_letters) |
                frozenset(ord(c) for c in string.digits))


class LLModule(object):
    def __init__(self):
        self.header = set()
        self.body = []

        # internal book-keeping
        self._varcount = 0
        self._constants = {}

    def add_constant(self, constant):
        if constant in self._constants:
            (_type, varname) = self._constants[constant]
        else:
            _type = "[%i x i8]" % len(constant)
            varname = self.nextvar
            self._constants[constant] = (_type, varname)
            self.header.add(
                r'%s =   global %s c"%s"' % (
                    varname, _type, self.escape(constant),
                )
            )
        return (_type, varname)

    @staticmethod
    def escape(text):
        buf = []
        for ch in bytearray(text):
            if ch in _VALID_CHARS:
                buf.append(chr(ch))
            else:
                ashex = hex(ch)[2:]
                if len(ashex) == 1:
                    ashex = '0' + ashex
                buf.append('\\' + ashex)
        return ''.join(buf)

    @property
    def nextvar(self):
        self._varcount += 1
        return '@".str%i"' % self._varcount

    def __str__(self):
        header = '\n'.join(set(sorted(self.header)))
        body = '\n    '.join(self.body)
        return '''\
; ModuleID = ""
target triple = ""
target datalayout = ""

{header}


define i32 @"main"()
{{
    {body}
    ret i32 0
}}
'''.format(header=header, body=body)


def compiler(ast):
    module = LLModule()
    ast = iter(ast)
    for node in ast:
        cls = type(node)
        if cls is AST.Module:
            pass
        elif cls is AST.Hello:
            _type, hello = module.add_constant(b'hello, world!')
            module.header.add(
                'declare i32 @"puts"(i8* %".1")'
            )
            module.body.append(
                'call i32 (i8*)* @"puts"(i8* getelementptr (%s* %s, i32 0, i32 0))'
                % (_type, hello)
            )
        elif cls is AST.Print:
            print_codegen(ast, module, builder, zero)

    return module


def print_codegen(ast, module, builder, zero):
    string_node = next(ast)
    arg = string_node.datas[0]
    arg_value = module.add_constant(bytearray(arg))
    module.header.add(
        'declare i32 @"printf"(i8* %".1")'
    )
    module.body.append(
        'call i32 (i8*)* @"printf"(i8* getelementptr (%s, i32 0, i32 0))'
        % arg_value
    )

