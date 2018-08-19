def repeat_inside(line):
    max_str = ''
    for i in range(0, len(line)):
        for j in range(1, len(line) + 1 - i):
            s = ''
            n = len(line[i:i + j])
            while n < len(line) and line[i + n:i + j + n] == line[i:i + j]:
                s += line[i:i + j]
                n += len(line[i:i + j])
            if s != '':
                # print(f'({line})', line[i:i + j] + s)
                if len(line[i:i + j] + s) > len(max_str):
                    max_str = line[i:i + j] + s
    # print(max_str)
    return max_str

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa'
    assert repeat_inside('aabbff') == 'aa'
    assert repeat_inside('aababcc') == 'abab'
    assert repeat_inside('abcabcabab') == 'abcabc'

    print('"Run" is good. How is "Check"?')
