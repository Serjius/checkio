import collections


def checkio(data):
    d = collections.OrderedDict({1000: 'M',
                                 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                                 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                                 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
                                 })
    res_str = ''
    while data > 0:
        for k, v in d.items():
            if data >= k:
                res_str += v
                data = data - k
                break
    return(res_str)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    # assert checkio(6) == 'VI', '6'
    # assert checkio(76) == 'LXXVI', '76'
    # assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
