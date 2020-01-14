# Написать функцию-декоратор nonify(func), которая заменяет возвращаемое значение функции func на None,
# если оно было пустое (и не меняет в противном случае).


def nonify(func):
    def wrapper(*args, **kwargs):
        if not func(*args, **kwargs):
            return None
        else:
            return func(*args, **kwargs)
    return wrapper
