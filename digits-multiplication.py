from functools import reduce


def checkio(number: int) -> int:
    return reduce((lambda x, y: x * y),
                  [int(x) for x in str(number) if int(x) > 0])

# These "asserts" using only for self-checking and not necessary for
# auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
