from ._tokenlike import Tokenlike


class AST(Tokenlike):
    def __iter__(self):
        stack = [self]
        while stack:
            node = stack.pop()
            yield node
            if isinstance(node, AST):
                stack.extend(reversed(node.datas))


class Module(AST):
    pass


class Hello(AST):
    pass


class Print(AST):
    pass


class String(AST):
    pass
