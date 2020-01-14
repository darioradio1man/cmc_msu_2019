# Написать функцию moar(a, b, n) от трёх параметров — целочисленных последовательностей a и b, и натурального числа n.
# Функция возвращает True, если в a больше чисел, кратных n, чем в b, и False в противном случае.


def moar(a, b, n):
    flaga, flagb = 0, 0
    for i in range(0, len(a)):
        if a[i] % n == 0:
            flaga += 1
    for i in range(0, len(b)):
        if b[i] % n == 0:
            flagb += 1
    return True if flaga > flagb else False


