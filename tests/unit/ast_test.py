from mylang import ast


def test_module():
    assert repr(ast.Module()) == 'Module()'


def test_module_with_hello():
    assert repr(ast.Module(ast.Hello())) == 'Module(Hello(),)'


def test_hello():
    assert repr(ast.Hello()) == 'Hello()'
