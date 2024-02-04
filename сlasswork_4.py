# СПИСКИ (упорядоченные, не плоские, не хешируемые, динамические (ИЗМЕНЯЕМЫЕ))
# a = ["sasha", "masha", 1 , 2, 3]
# print(a)

# b = "Саша пошёл в магазин!"
# c = list(b)
# print(c[2:9:1])

# list.append(x) Добавляет элемент в конец списка
# list.extend(L) Расширяет список list, добавляя в конец все элементы списка L
# list.insert(i, x)	Вставляет на i-ый элемент значение x
# list.remove(x) Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует
# list.pop([i])	Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
# list.index(x, [start [, end]]) Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
# list.count(x)	Возвращает количество элементов со значением x
# list.sort([key=функция])	Сортирует список на основе функции
# list.reverse() Разворачивает список
# list.copy() Поверхностная копия списка
# list.clear() Очищает список

# Операторы del, in, not in
# Общая функция sorted

# del c[0]
# print(c)
# print("sasha" in a)

#----------------------------------------------------------

# КОРТЕЖИ (упорядоченные, не плоские, хешируемые, НЕ ИЗМЕНЯЕМЫЕ)

# a = ("sasha", "masha", 1, 2, 3)
# b = "Саша пошёл в магазин"
# c = tuple(b)
# print(c)

#----------------------------------------------------------

# МНОЖЕСТВА (изменяемые, только уникальные элементы, не упорядоченные)
# только Len и in/not in

# a = {"sasha", "masha", 2, 3, 4}
# b = "Саша пошёл в магазин магазин в Минске"
# c = set(b)
# print(c)
#
# len(s) - число элементов в множестве (размер множества).
# x in s - принадлежит ли x множеству s.
# set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
# set == other - все элементы set принадлежат other, все элементы other принадлежат set.
# set.issubset(other) или set <= other - все элементы set принадлежат other.
# set.issuperset(other) или set >= other - аналогично.
# set.union(other, ...) или set | other | ... - объединение нескольких множеств.
# set.intersection(other, ...) или set & other & ... - пересечение.
# set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.
# set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
# set.copy() - копия множества.
#
# Операции, непосредственно изменяющие множество:
#
# set.update(other, ...); set |= other | ... - объединение.
# set.intersection_update(other, ...); set &= other & ... - пересечение.
# set.difference_update(other, ...); set -= other | ... - вычитание.
# set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
# set.add(elem) - добавляет элемент в множество.
# set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
# set.discard(elem) - удаляет элемент, если он находится в множестве.
# set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
# set.clear() - очистка множества.

#----------------------------------------------------------

# FROZENSET - неизменяемое множество

#----------------------------------------------------------

# СЛОВАРИ (не плоские, не хешируемые, динамические (ИЗМЕНЯЕМЫЕ))

# a = {
#     "magneto": "avto",
#     "monitor": "lg",
#     "year": 2023
# }
# print(a)
#
# b = dict(mds="trans", monitor="samsung")
# print(b)
#
# c = dict.fromkeys(["fraktlogistic", "magneto"], "super")
# print(c)
#
# d = {"sasha"+str(i): i for i in range(5)}
# print(d)
#
# d["masha"] = 1000
#
# print(d)
# print(d["masha"])

# dict.clear() - очищает словарь.
# dict.copy() - возвращает копию словаря.
# classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).
# dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
# dict.items() - возвращает пары (ключ, значение).
# dict.keys() - возвращает ключи в словаре.
# dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
# dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.
# dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).
# dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
# dict.values() - возвращает значения в словаре

# name = "Sasha"
# last_name = "Maruhenko"
# conv_dict = dict(name=last_name)
# print(conv_dict)

# string = '{"name":"Иван Иванов","ids":[1,2,3],"balance":12345}'
# print(string)
# data = eval(string)
# print(data)
# print(type(string))
# print(type(data))
# print(data["ids"][1])
#
# data1 = {
#     "name": "Иван Иванов",
#     "ids": [1, 2, 3],
#     "balance": 12345
# }
# print(type(data1))
#
# name = "al"
# last_name = "Maruhenko"
# conv_dict = dict(((name, last_name), ("shurik", "super")))
# print(conv_dict)
#
# conv_dict1 = dict([name, "cd"])
# print(data.items())

#----------------------------------------------------------

# COLLECTIONS - МОДУЛЬ СПЕЦИАЛИЗИРОВАННЫХ ТИПОВ

# import collections
# text = "Hello"
# data = collections.Counter(text)
# print(set(data.elements()))


