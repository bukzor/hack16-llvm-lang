from mylang.hello import hello


def test_lex_null():
    assert hello('') == ''


def test_hello():
    assert hello('hello') == 'hello, world!\n'


def test_hello_whitespace():
    assert hello('\n\n   hello\n\t') == 'hello, world!\n'


def test_comments():
    assert hello('hello no') == 'hello, world!\n'


def test_hihi():
    assert hello('hello hello') == 'hello, world!\nhello, world!\n'


def test_print():
    assert hello('print butt') == ' butt'


def test_print_twice():
    assert hello('print butt\n    print fart 420 blaze it') == ' butt fart 420 blaze it'


def test_print_with_escaped_newlines():
    assert hello('print butt\\n\n    print fart 420 blaze it') == ' butt\n fart 420 blaze it'
