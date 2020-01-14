# Ввести несколько строк одинаковой длины, состоящих из символов '#' и '.'.
# Первый и последний символ каждой строки — '.', а первая и последняя строки состоят целиком из '-'.
# Известно (проверять не надо), что на получившемся поле изображены только прямоугольника, причём они не соприкасаются
# даже углами. Вывести количество этих прямоугольников.


count_of_rect = 0
tmp = set({})
indexes = set({})

input()
while 1:
    line = list(input())
    if line[0] == '-':
        count_of_rect += len(indexes)
        break

    tmp = indexes.copy()
    indexes.clear()
    is_rectangle = False
    start = 0

    for i, j in enumerate(line):
        if j == '#' and not is_rectangle:
            is_rectangle = True
            start = i
        elif is_rectangle and j != '#':
            is_rectangle = False
            indexes.add((start, i - 1))

    count_of_rect += len(tmp - indexes)

print(count_of_rect)
