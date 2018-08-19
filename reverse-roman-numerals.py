import collections


def reverse_roman(roman_string):
    d = collections.OrderedDict({1000: 'M',
                                 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                                 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                                 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
                                 })

    d = collections.OrderedDict({y: x for x, y in d.items()})
    res_str = 0
    idx = 0
    while idx < len(roman_string):
        if idx + 1 < len(roman_string) and roman_string[idx] + roman_string[idx + 1] in d:
            res_str += d[roman_string[idx] + roman_string[idx + 1]]
            idx += 2
        else:
            res_str += d[roman_string[idx]]
            idx += 1
    return(res_str)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!')
