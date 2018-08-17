def checkio(data):
    if len(data) <= 1:
        return int(data[0])
    n = data[0] + int(checkio(data[1:]))
    return n


print(checkio([1, 2, 3, 4, 5]))
