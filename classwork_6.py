def up(string):
    if isinstance(string, str):
        return string.upper()
    else:
        raise TypeError(f"Введена не строка")


try:
    print(up(1))
except TypeError as exc:
    print(f"Возникла ошибка: {exc}")

def decorator(func):
    def wrapper(*args, **kwargs):
        print("Выполняем действия до функции")
        result = func(*args, **kwargs)
        print("Выполняем действия после функции")
        return result

    return wrapper


@decorator
def hello(name):
    print(f"Hello, {name}")


hello("Alex")


def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')

        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')

        return original_result

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


print(say('Jane', 'Hello, World'))


def greetings(st):
    print(st)
    if len(st) == 0:  # Граничный случай
        return
    else:  # Рекурсивный случай
        greetings(st[:-1])


greetings('Hello, world!')
