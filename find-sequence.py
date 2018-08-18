def checkio(matrix):
    # replace this for solution
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if x >= 3 and \
                    matrix[x][y] == matrix[x - 1][y] and\
                    matrix[x][y] == matrix[x - 2][y] and\
                    matrix[x][y] == matrix[x - 3][y]:
                return True
            if y >= 3 and \
                    matrix[x][y] == matrix[x][y - 1] and\
                    matrix[x][y] == matrix[x][y - 2] and\
                    matrix[x][y] == matrix[x][y - 3]:
                return True

            if y >= 3 and x >= 3 and\
                    matrix[x][y] == matrix[x - 1][y - 1] and\
                    matrix[x][y] == matrix[x - 2][y - 2] and\
                    matrix[x][y] == matrix[x - 3][y - 3]:
                return True

            if x <= len(matrix[x]) - 4 and y >= 3 and\
                    matrix[x][y] == matrix[x + 1][y - 1] and\
                    matrix[x][y] == matrix[x + 2][y - 2] and\
                    matrix[x][y] == matrix[x + 3][y - 3]:
                return True
    return False

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    print('OK')
