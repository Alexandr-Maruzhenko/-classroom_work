def up(string):
    if isinstance(string, str):
        return string.upper()
    else:
        raise TypeError(f"Введена не строка")


try:
    print(up(1))
except TypeError as exc:
    print(f"Возникла ошибка: {exc}")
