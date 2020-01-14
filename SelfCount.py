# Написать класс WeAre, объекты которого содержат поле count, содержащее количество существующих экземпляров
# этого класса. Игнорировать попытки изменить значение этого поля вручную или удалить его.


class WeAre(object):
    rcount = 0

    def __init__(self):
        WeAre.rcount += 1

    @property
    def count(self):
        return self.rcount

    @count.setter
    def count(self, value):
        pass

    @count.deleter
    def count(self):
        pass

    def __del__(self):
        self.__class__.rcount -= 1
