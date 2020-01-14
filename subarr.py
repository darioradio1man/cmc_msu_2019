# Ввести в столбик последовательность целых (положительных и отрицательных) чисел, не равных нулю;
# в конце этой последовательности стоит 0. Вывести наибольшую сумму последовательно идущих элементов
# этой последовательности (не менее одного).


from sys import maxsize
maxfar = -maxsize - 1
maxend = 0
s = 0
a = int(input())
while a != 0:
    maxend += a
    a = int(input())
    if maxfar < maxend:
        maxfar = maxend

    if maxend < 0:
        maxend = 0

print(maxfar)
