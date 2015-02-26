class Tokenlike(object):
    def __init__(self, *datas):
        self.datas = datas

    def __repr__(self):
        return '%s%r' % (type(self).__name__, self.datas)

    def __eq__(self, other):
        if not isinstance(other, Tokenlike):
            return NotImplemented

        return (
            type(self) is type(other),
            self.datas == other.datas,
        )
