# Написать функцию-параметрический декоратор fix(n), с помощью которой все вещественные
# (как позиционные, так и именные) параметры произвольной декорируемой функции, а также её возвращаемое значение,
# округляются до n-го знака после запятой. Если какие-то параметры функции оказались не вещественными,
# или не вещественно возвращаемое значение, эти объекты не меняются.


def fix(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            targ = []
            for i in args:
                if isinstance(i, float):
                    targ.append(round(i, n))
            for k, v in kwargs.items():
                if isinstance(i, float):
                    kwargs[k] = round(v, n)
            return round(func(*targ, **kwargs), n)
        return wrapper
    return decorator

