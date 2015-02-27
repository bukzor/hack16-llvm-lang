import llvmlite.ir as ll

i32 = ll.IntType(32)
i8 = ll.IntType(8)

builder = ll.IRBuilder()
module = ll.Module()
module.triple = ''

hellostr = 'hello, world!'

stringtype = ll.ArrayType(i8, len(hellostr))
hello = ll.GlobalVariable(module, stringtype, '.str4')
hello.initializer = builder.constant(stringtype, bytearray(hellostr))


fntype = ll.FunctionType(i32, [i8.as_pointer()])
puts = ll.Function(module, fntype, 'puts')


fntype = ll.FunctionType(i32, [])
func = ll.Function(module, fntype, name='main')
bb_entry = func.append_basic_block()

builder.position_at_end(bb_entry)

zero = builder.constant(i32, 0)
builder.call(puts, [hello.gep((zero, zero))])

builder.ret(zero)
print(module)
