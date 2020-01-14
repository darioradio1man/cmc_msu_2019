# Написать декоратор класса sizer, который добавляет в него поле size,
# равное длине объекта, если у объекта есть длина, или модулю целочисленного
# представления объекта в противном случае (предполагается, что ошибок нет).
# Предоставить пользователю возможность произвольно менять это поле.


def sizer(cls):
    @property
    def size(self):
        try:
            return self.__size
        except:
            try:
                return len(self)
            except:
                return int(self)

    @size.setter
    def size(self, val):
        self.__size = val

    cls.size = size
    return cls
