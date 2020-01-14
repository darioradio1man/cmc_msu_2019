# Написать функцию maxfun(), которая принимает переменное число параметров — числовую последовательность S,
# функцию F1 и, возможно, ещё несколько функций F2 … Fn. Возвращает она ту из функций Fi, сумма значений которой
# на всех элементах S наибольшая. Если таких функций больше одной, возвращается Fi с наибольшим i.


def maxfun(ndxs, *args):
    result = 0
    maxsum = sum(map(args[0], ndxs))
    for cnt, the_value in enumerate(args):
        maxvalue = sum(map(the_value, ndxs))
        if maxvalue >= maxsum:
            maxsum = maxvalue
            result = the_value
    return result
