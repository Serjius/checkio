def fib_recursion(n):
    if n <= 1:
        return n
    return fib_recursion(n - 2) + fib_recursion(n - 1)


def fib_array(n):
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


def fib_var(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(2, n + 1):
        a, b = a + b, a
    return a + b


def test_fib(function):
    print('test #1', function.__name__, 'ok' if function(10) == 55 else 'failed')
    print('test #2', function.__name__, 'ok' if function(20) == 6765 else 'failed')
    print('test #3', function.__name__, 'ok' if function(0) == 0 else 'failed')
    print('test #4', function.__name__, 'ok' if function(1) == 1 else 'failed')
    print('test #5', function.__name__, 'ok' if function(2) == 1 else 'failed')
    print('test #6', function.__name__, 'ok' if function(3) == 2 else 'failed')
    print('test #7', function.__name__, 'ok' if function(4) == 3 else 'failed')
    print('test #8', function.__name__, 'ok' if function(5) == 5 else 'failed')

test_fib(fib_recursion)
test_fib(fib_array)
test_fib(fib_var)
