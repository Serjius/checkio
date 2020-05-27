def count_steps_length_3(n):
    """Calculate the number of options to reach the point
       if you can move for +1, +2 and +3 by one step
    """
    k = [0, 1, 1] + [0] * (n - 2)
    for i in range(3, n + 1):
        k[i] = k[i - 3] + k[i - 2] + k[i - 1]
    return k[n]


def count_steps_length_2(n):
    """Calculate the number of options to reach the point
       if you can move for +1 and +2 by one step
    """
    k = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        k[i] = k[i - 2] + k[i - 1]
    return k[n]


def count_steps_length_3_with_allow(n, allowed):
    """Calculate the number of options to reach the point
       if you can move for +1, +2 and +3 by one step
       allowed is an array False is this point fobitten True if allowed
       Zerro element is always False the first is always True - can ignore
    """
    k = [0, 1, int(allowed[2])] + [0] * (n - 2)
    for i in range(3, n + 1):
        if allowed[i]:
            k[i] = k[i - 3] + k[i - 2] + k[i - 1]
    return k[n]


def count_steps_length_3_with_cost(n, price):
    """Calculate the number of options to reach the point
       if you can move for +1, +2 and +3 by one step
       each point has a cost, need to find cheepiest path
    """
    c = [0, price[1], price[1] + price[2]] + [0] * (n - 2)
    for i in range(3, n + 1):
        c[i] = price[i] + min(price[i - 1], price[i - 2])
    return c[i]

print(count_steps_length_3(5) == 7)
print(count_steps_length_2(5) == 5)
print(count_steps_length_3_with_allow(5, [None, None, False, True, True, True]) == 3)
print(count_steps_length_3_with_allow(5, [None, None, False, False, True, True]) == 1)
print(count_steps_length_3_with_cost(5, [0, 1, 2, 500, 2, 2]))
