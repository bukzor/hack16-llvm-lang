from ._tokenlike import Tokenlike


class AST(Tokenlike):
    def __iter__(self):
        stack = [self]
        while stack:
            node = stack.pop()
            yield node
            stack.extend(reversed(node.datas))


class Module(AST):
    pass


class Hello(AST):
    pass
