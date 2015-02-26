class Token(object):
    def __init__(self, *datas):
        self.datas = datas

    def __repr__(self):
        return '%s%r' % (type(self).__name__, self.datas)

    def __eq__(self, other):
        if not isinstance(other, Token):
            return NotImplemented

        return self.datas == other.datas


class ID(Token):
    pass


class WS(Token):
    pass
