# Написать функцию fcounter(), которая первым параметром получает некоторый класс,
# а остальные параметры применяет для создания экземпляра этого класса.
# Функция должна возвращать 4 отсортированных списка: имена методов класса, имена полей класса,
# имена методов, которые появились в экземпляре и имена полей, которые появились в экземпляре
# (под «полями» имеются в виду не-callable() объекты).


def fcounter(*args):
    class_name = args[0]
    class_atrrs = list(filter(lambda x: not x.startswith("_"), dir(args[0])))
    cm = list(filter(lambda x: callable(getattr(class_name, x)), class_atrrs))
    cf = list(filter(lambda x: not callable(getattr(class_name, x)), class_atrrs))

    object_names = class_name(*args[1:])
    object_attrs = list(filter(lambda x: not x.startswith("_"), dir(object_names)))
    om = list(filter(lambda x: callable(getattr(object_names, x)) and x not in cm, object_attrs))
    of = list(filter(lambda x: not callable(getattr(object_names, x)) and x not in cf,
                     object_attrs))
    return cm, cf, om, of
