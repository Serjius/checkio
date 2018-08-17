def checkio(first, second):
    f_set = set(first.split(','))
    s_set = set(second.split(','))
    lst = ','.join(sorted([x for x in f_set.intersection(s_set)]))
    return lst

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three",
                   "four,five,one,two,six,three") == "one,three,two", "1 2 3"
