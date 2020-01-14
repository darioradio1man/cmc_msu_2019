# Написать, держитесь крепче, генератор-декоратор statcounter(), который конструирует объекты
# (назовём один из них stat) со следующим поведением. Первый вызов next(stat) (он же stat.send(None))
# возвращает словарь, в котором stat будет хранить информацию вида функция: количество вызовов,
# где функция — это исходный (не обёрнутый) объект-функция (да, так тоже можно!).
# Все последующие вызовы stat.send(function) оборачивают вызов произвольной функции
# function увеличением на 1 соответствующего элемента словаря. Глобальными именами пользоваться нельзя.


def statcounter():
    dict = {}

    class object:
        def __next__(self):
            return dict

        def send(self, func):
            def wrapper(*args, **kwargs):
                dict[func] = 1 if func not in dict.keys() else dict[func] + 1
                return func(*args, **kwargs)
            return wrapper
    return object()
