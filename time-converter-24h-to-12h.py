from datetime import datetime as dt
from datetime import time as tm


def time_converter(time):
    # replace this for solution
    inp_msk = '%H:%M'
    out_msk = '%I:%M %p'

    s = dt.strptime(time, inp_msk).strftime(out_msk)
    s = s.replace('PM', 'p.m.').replace('AM', 'a.m.')
    if s[0] == '0':
        s = s[1:]
    print(s)
    return(s)

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
