# Написать класс DivStr(str), полностью (за исключением правых операций со строками и split()/splitlines())
# воспроизводящий работу str. Дополнительно класс должен поддерживать операцию деления «/n», где n — натуральное число,
# которая должна возвращать n-ю часть от начала строки (если не делится, округлённую в меньшую сторону,
# если n>len(s) — пустую строку). Задача в том, чтобы любое возвращаемое методами значение типа str
# превращалось в DivStr. Согласно документации, мы не можем подсунуть методы, начинающиеся на «__», прямо в __dict__,
# или поймать __getattr__-ом, или даже __getattribute__-ом, а должны задать их явно, например, с помощью def.


def string_decorator(ags):
    def wrapper(f):
        def func(*args, **kwargs):
            var = f(*args, **kwargs)
            if type(var) is str:
                return DivStr(var)
            return var
        return func

    for keys, values in str.__dict__.items():
        if callable(values):
            setattr(ags, keys, wrapper(values))
    return ags


@string_decorator
class DivStr(str):
    def __truediv__(self, other):
        return self[: len(self) // other]

