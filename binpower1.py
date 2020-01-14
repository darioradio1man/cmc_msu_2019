# Написать рекурсивную функцию BinPow(), которая принимает три параметра: python3-объект a,
# натуральное число 0<N<1000000, и некоторую ассоциативную бинарную функцию f().
# Функция BinPow() реализует алгоритм бинарного возведения в степень (кроме нулевой степени).
# Результатом BinPow(a, n, f) будет применение f(x) к a n-1 раз. Более точно, BinPow(a, 1, f) == a,
# BinPow(a, 2, f) == f(a,a), BinPow(a, 3, f) == f(a,f(a, a)) == f(f(a, a), a) (в силу ассоциативности), …
# BinPow(a, n, f) == f(f(…f(a, a), …), a).


def BinPow(a, n, f):
    if n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 1:
        return f(BinPow(a, n - 1, f), a)
    else:
        return f(BinPow(a, n/2, f), BinPow(a, n/2, f))

