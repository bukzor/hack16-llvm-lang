from __future__ import unicode_literals

import llvmlite.ir as ll

from mylang import ast as AST

i32 = ll.IntType(32)
i8 = ll.IntType(8)


def compiler(ast):
    builder = ll.IRBuilder()
    module = ll.Module()
    module.triple = ''
    fntype = ll.FunctionType(i32, [])
    zero = builder.constant(i32, 0)

    hello_globals = False

    for node in ast:
        cls = type(node)
        if cls is AST.Module:
            main = ll.Function(module, fntype, name='main').append_basic_block()
            builder.position_at_end(main)
            builder.ret(zero)
            builder.position_at_start(main)
        elif cls is AST.Hello:
            hellostr = 'hello, world!'

            if not hello_globals:
                # TODO-TEST: two hellos
                stringtype = ll.ArrayType(i8, len(hellostr))
                hello = ll.GlobalVariable(module, stringtype, '.str4')
                hello.initializer = builder.constant(stringtype, bytearray(hellostr, 'utf-8'))

                fntype = ll.FunctionType(i32, [i8.as_pointer()])
                puts = ll.Function(module, fntype, 'puts')

                hello_globals = True

            builder.call(puts, [hello.gep((zero, zero))])

    return module
