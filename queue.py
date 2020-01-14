# Ввести последовательность объектов Python (кортежей или целых чисел), и сымитировать работу Чудо-Конвейера.
# Если объект — кортеж, это означает, что на вход конвейеру подаются поочерёдно все объекты из этого кортежа.
# Если объект — натуральное число N, это означает, что с выхода конвейера надо снять поочерёдно N объектов,
# объединить их в кортеж и вывести. Если с конвейера нельзя снять N объектов, или в последовательности нет
# больше команд, Чудо-Конвейер немедленно останавливается.


pack = []
new_package = eval(input())

for p in new_package:
    if isinstance(p, tuple):
        pack += p
        continue
    if len(pack) < p:
        break
    print(tuple(pack[:p]))
    pack = pack[p:]