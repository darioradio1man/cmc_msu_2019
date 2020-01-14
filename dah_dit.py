# Написать класс morse("строка"), экземпляр которого переводит арифметические выражения в морзянку!
# Параметр «строка» бывает разных видов, более подробно описан в подсказках, желающие могут догадаться
# о его компонентах по примеру (пример почти полный). «+» — точка, «-» — тире, «~» — промежуток между буквами
# (бывает только между буквами и только один, проверять не надо).


class morse:
    def __init__(self, parser="", buffer="."):
        self.parser = parser
        self.buffer = buffer
        self.end = "."
        if parser == "":
            self.dah = "dah"
            self.dit = "dit"
            self.di = "di"
        else:
            ls = parser.split(" ")
            if len(ls) == 1:
                self.end = ""
                self.di = ls[0][0]
                if len(ls[0]) == 2:
                    self.dah = ls[0][1]
                    self.dit = ls[0][0]
                elif len(ls[0]) == 3:
                    self.dah = ls[0][2]
                    self.dit = ls[0][1]
                else:
                    self.end = ls[0][3]
                    self.dah = ls[0][2]
                    self.dit = ls[0][1]
            elif len(ls) == 2:
                self.dah = ls[1]
                self.di = ls[0]
                self.dit = ls[0]
            elif len(ls) == 3:
                self.dah = ls[2]
                self.dit = ls[1]
                self.di = ls[0]
            else:
                self.end = ls[3]
                self.dah = ls[2]
                self.dit = ls[1]
                self.di = ls[0]

    def __neg__(self):
        if len(self.parser.split(" ")) == 1 and self.parser != "":
            return morse(self.parser, self.dah + self.buffer)
        else:
            return morse(self.parser, self.dah + " " + self.buffer)

    def __pos__(self):
        if len(self.parser.split(" ")) == 1 and self.parser != "":
            return morse(self.parser, self.di + self.buffer)
        else:
            return morse(self.parser, self.di + " " + self.buffer)

    def __invert__(self):
        return morse(self.parser, ", " + self.buffer)

    def __str__(self):
        if len(self.parser.split(" ")) == 1 and self.parser != "":
            self.buffer = self.buffer.replace(self.di + ",", self.dit)
            self.buffer = self.buffer.replace(self.dah + ",", self.dah)
            self.buffer = self.buffer[:len(self.buffer) - 1]
            if self.buffer[len(self.buffer)-1] == self.di:
                self.buffer = self.buffer[:len(self.buffer)-1] + self.dit + self.end
            else:
                self.buffer = self.buffer + self.end
        else:
            self.buffer = self.buffer.replace(self.di + " ,", self.dit + ",")
            self.buffer = self.buffer.replace(self.dah + " ,", self.dah + ",")
            self.buffer = self.buffer.replace(self.di + " .", self.dit + self.end)
            self.buffer = self.buffer.replace(self.dah + " .", self.dah + self.end)
        return self.buffer
