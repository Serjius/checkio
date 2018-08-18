def decor_upper(func):
    def wrapper():
        return func().upper()
    return wrapper


def decor_internal(func):
    def wrapper():
        return '<int>' + func() + '/<int>'
    return wrapper


def decor_external(func):
    def wrapper():
        return '<ext>' + func() + '/<ext>'
    return wrapper


@decor_external
@decor_internal
@decor_upper
def say_it():
    return 'This CammelCase String'

print(say_it())


def decor_internal(func):
    def wrapper():
        return '<int>' + func() + '/<int>'
    return wrapper
