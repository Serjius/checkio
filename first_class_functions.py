def yell(text):
    return '>' + text.upper() + '!<'

# call a function
print(yell('Hi'))

# function via variable
f = yell
print(f('OPS'))

# names
print(f'yell name:{yell.__name__} qname:{yell.__qualname__}')
print(f'f name:{f.__name__} qname:{f.__qualname__}')

#__dict__
print(dir())

del yell
print('after function del')
print(dir())
print(f'f name:{f.__name__} qname:{f.__qualname__}')
print(f('Yeap'))
