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
            varname = self._constants[constant]
        else:
            varname = self.nextvar
            self._constants[constant] = varname
            self.header.add(
                r'%s =   global [%i x i8] c"%s"' % (
                    varname, len(constant), self.escape(constant),
                )
            )
        return varname

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
            hello = module.add_constant(b'hello, world!')
            module.header.add(
                'declare i32 @"puts"(i8* %".1")'
            )
            module.body.append(
                'call i32 (i8*)* @"puts"(i8* getelementptr (%s, i32 0, i32 0))'
                % hello
            )
        # elif cls is AST.Print:
            # print_codegen(ast, module, builder, zero)

    return module


# def print_codegen(ast, module, builder, zero):
    # global i
    # string_node = next(ast)
    # arg = string_node.datas[0]
    # i = i + 1
    # stringtype = ll.ArrayType(i8, len(arg))
    # arg_value = ll.GlobalVariable(module, stringtype, 'print_arg%s' % i)
    # arg_value.initializer = builder.constant(stringtype, bytearray(arg))
    # printf = ll.Function(module, ll.FunctionType(i32, [i8.as_pointer()]), 'printf')
    # builder.call(printf, [arg_value.gep((zero, zero))])
