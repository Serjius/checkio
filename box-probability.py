from collections import namedtuple
from fractions import Fraction

StRec = namedtuple('StRec', 'pearls, step, w_taken, b_taken')


def checkio(pearls: str, steps: int) -> float:
    lst = []
    n = 1
    p = pearls.count('w')
    lst.append(StRec(pearls,
                     n,
                     Fraction(p, len(pearls)),
                     Fraction(len(pearls) - p,  len(pearls))
                     )
               )

    while n < steps:
        for l in lst:
            if l.step == n:
                if l.w_taken > 0:
                    new_p = l.pearls.replace('w', 'b', 1)
                    p = new_p.count('w')
                    lst.append(StRec(new_p,
                                     n + 1,
                                     l.w_taken * Fraction(p, len(pearls)),
                                     l.w_taken * Fraction(len(pearls) - p,  len(pearls))
                                     )
                               )
                if l.b_taken > 0:
                    new_p = l.pearls.replace('b', 'w', 1)
                    p = new_p.count('w')
                    lst.append(StRec(new_p,
                                     n + 1,
                                     l.b_taken * Fraction(p, len(pearls)),
                                     l.b_taken * Fraction(len(pearls) - p,  len(pearls))
                                     )
                               )
        n += 1

    for l in lst:
        print(l)

    r = Fraction(0, 1)
    for l in lst:
        if l.step == steps:
            r += l.w_taken

    print(round(r.numerator / r.denominator, 2))
    return(round(r.numerator / r.denominator, 2))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    # print("Example:")
    # print(checkio('bbw', 3))

    # # assert checkio('bbw', 3) == 0.48, "1st example"
    # # assert checkio('wwb', 3) == 0.52, "2nd example"
    # # assert checkio('www', 3) == 0.56, "3rd example"
    # # assert checkio('bbbb', 1) == 0, "4th example"
    # # assert checkio('wwbb', 4) == 0.5, "5th example"
    # # assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    assert checkio('bbb', 5) == 0.48, "7th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")
