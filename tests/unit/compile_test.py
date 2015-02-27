import llvmlite.ir as ll
from mylang import ast
from mylang.compile import compile
from mylang.interpret import interpret


def test_compile_null():
    assert str(compile(ast.Module())) == '''\
; ModuleID = ""
target triple = ""
target datalayout = ""


define i32 @"main"() 
{
.1:
  ret i32 0
}



'''




def test_compile_hello():
    assert str(compile(ast.Module(ast.Hello()))) == '''\
; ModuleID = ""
target triple = ""
target datalayout = ""


define i32 @"main"() 
{
.1:
  %".3" = call i32 (i8*)* @"puts"(i8* getelementptr ([13 x i8]* @".str4", i32 0, i32 0))
  ret i32 0
}

@".str4" =   global [13 x i8] c"hello\\2c\\20world\\21"
declare i32 @"puts"(i8* %".1") 



'''
