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
    global_symbols = dict()
    zero = builder.constant(i32, 0)
    global_symbols['zero'] = zero

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
            print_codegen(ast, module, builder, global_symbols)

    return module


def print_codegen(ast, module, builder, global_symbols):
    string_node = next(ast)
    arg = string_node.datas[0]
    print_codegen.i = print_codegen.i + 1
    stringtype = ll.ArrayType(i8, len(arg))
    arg_value = ll.GlobalVariable(module, stringtype, 'print_arg%s' % print_codegen.i)
    arg_value.initializer = builder.constant(stringtype, bytearray(arg))
    if 'printf' in global_symbols:
        printf = global_symbols['printf']
    else:
        printf = global_symbols['printf'] = ll.Function(module, ll.FunctionType(i32, [i8.as_pointer()]), 'printf')
    zero = global_symbols['zero']
    builder.call(printf, [arg_value.gep((zero, zero))])

print_codegen.i = 0
