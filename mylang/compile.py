from __future__ import unicode_literals

import llvmlite.ir as ll

from mylang import ast as AST

i32 = ll.IntType(32)
i8 = ll.IntType(8)
i = 0


def compiler(ast):
    builder = ll.IRBuilder()
    module = ll.Module()
    module.triple = ''
    fntype = ll.FunctionType(i32, [])
    zero = builder.constant(i32, 0)

    hello_globals = False

    ast = iter(ast)
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
                stringtype = ll.ArrayType(i8, len(hellostr))
                hello = ll.GlobalVariable(module, stringtype, '.str4')
                hello.initializer = builder.constant(stringtype, bytearray(hellostr, 'utf-8'))

                fntype = ll.FunctionType(i32, [i8.as_pointer()])
                puts = ll.Function(module, fntype, 'puts')

                hello_globals = True

            builder.call(puts, [hello.gep((zero, zero))])
        elif cls is AST.Print:
            print_codegen(ast, module, builder, zero)

    return module


def print_codegen(ast, module, builder, zero):
    global i
    string_node = next(ast)
    arg = string_node.datas[0]
    i = i + 1
    stringtype = ll.ArrayType(i8, len(arg))
    arg_value = ll.GlobalVariable(module, stringtype, 'print_arg%s' % i)
    arg_value.initializer = builder.constant(stringtype, bytearray(arg))
    printf = ll.Function(module, ll.FunctionType(i32, [i8.as_pointer()]), 'printf')
    builder.call(printf, [arg_value.gep((zero, zero))])
