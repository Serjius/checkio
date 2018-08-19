def longest_palindromic(text):
    res_list = list(text)
    for i in range(len(text)):
        # odd
        start, end = i - 1, i + 1
        while start >= 0 and end < len(text) and text[start] == text[end]:
            res_list.append(text[start:end + 1])
            start -= 1
            end += 1
        # even
        start, end = i, i + 1
        while start >= 0 and end < len(text) and text[start] == text[end]:
            res_list.append(text[start:end + 1])
            start -= 1
            end += 1

    return max(res_list, key=len)

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"
    assert longest_palindromic("abc") == 'a'
    print('OK')
