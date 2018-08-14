import string


def checkio(words: str) -> bool:
    lst = words.split()
    if len(lst) < 3:
        return False

    for i in range(len(lst) - 2):
        if (any([x for x in lst[i] if x in string.ascii_letters]) and
                any([x for x in lst[i + 1] if x in string.ascii_letters]) and
                any([x for x in lst[i + 2] if x in string.ascii_letters])):
            return True

    return False


# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
