from mylang import tokens


def trynext(iterator):
    try:
        return next(iterator)
    except StopIteration:
        return ''


def lex(source):
    # TODO: hello, world! should be a valid program
    result = []

    source = iter(source)
    char = trynext(source)

    def one_token(char, predicate, tokentype):
        word = ''
        while predicate(char):
            word += char
            char = trynext(source)
        if word:
            result.append(tokentype(word))
        return char

    while char:
        char = one_token(char, lambda char: char.isspace(), tokens.WS)
        char = one_token(char, lambda char: char and not char.isspace(), tokens.ID)

    return result
