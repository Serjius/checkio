import traceback


def i_love_python():
    """
        Let's explain why do we love Python.
    """
    print(traceback.extract_stack(None, 2)[0][2])

    return "I love Python!"

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert i_love_python() == "I love Python!"
