VOWELS = "aeiouy"


def translate(phrase):
    r = ''
    i = 0
    while i < len(phrase):
        l = phrase[i]
        r += l
        if l in VOWELS:
            i += 2
        elif l == ' ':
            i += 0
        else:
            i += 1
        i += 1
    return r


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
