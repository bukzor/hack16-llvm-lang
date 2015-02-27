from mylang import ast
from mylang.compile import compiler


def test_compile_null():
    assert str(compiler(ast.Module())) == '''\
; ModuleID = ""
target triple = ""
target datalayout = ""




define i32 @"main"()
{
    
    ret i32 0
}
'''


def test_compile_hello():
    assert str(compiler(ast.Module(ast.Hello()))) == '''\
; ModuleID = ""
target triple = ""
target datalayout = ""

declare i32 @"puts"(i8* %".1")
@".str1" =   global [13 x i8] c"hello\\2c\\20world\\21"


define i32 @"main"()
{
    call i32 (i8*)* @"puts"(i8* getelementptr ([13 x i8]* @".str1", i32 0, i32 0))
    ret i32 0
}
'''

def test_compile_print():
    assert str(compiler(ast.Module(ast.Print(), ast.String(' butt')))) == '''\
; ModuleID = ""
target triple = ""
target datalayout = ""

@".str1" =   global [5 x i8] c"\\20butt"
declare i32 @"printf"(i8* %".1")


define i32 @"main"()
{
    call i32 (i8*)* @"printf"(i8* getelementptr ([5 x i8]* @".str1", i32 0, i32 0))
    ret i32 0
}
'''
