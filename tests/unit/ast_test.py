from mylang import ast

def test_module():
    repr(ast.Module()) == 'Module()'

def test_module_with_hello():
    repr(ast.Module()) == 'Module(Hello(),)'

def test_hello():
    repr(ast.Hello()) == 'Hello()'
