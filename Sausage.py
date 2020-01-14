# Написать класс sausage, имитирующий киберколбасу. Киберколбаса может быть проинициализирована нулём значений
# (создаётся колбаса по умолчанию), одним (фарш) и двумя (фарш и объём). Длина целого батона киберколбасы
# 12 символов фарша и 2 оболочки. Колбаса единичного объёма — это один полный батон, более, чем единичного —
# это несколько батонов (последний, возможно, неполон). Неполный батон заканчивается срезом.
# Киберколбаса поддерживает операции умножения и деления на целое число, а также сложения и вычитания с другой
# киберколбасой (фарш результата совпадает с фаршем первого операнда). Если объём киберколбасы нулевой,
# батон считается пустым.


class sausage:
    def __init__(self, fill="pork!", length=1):
        from fractions import Fraction
        self.fill = fill
        self.length = float(Fraction(length))

    def __add__(self, other):
        return sausage(self.fill, self.length + other.length)

    def __sub__(self, other):
        return sausage(self.fill, self.length - other.length)

    def __mul__(self, other):
        return sausage(self.fill, self.length * other)

    def __rmul__(self, other):
        return sausage(self.fill, self.length * other)

    def __truediv__(self, other):
        return sausage(self.fill, self.length / other)

    def __bool__(self):
        return True if self.length > 0 else False

    def __str__(self):
        def fill(filling, length):
            return ''.join([filling[i % len(filling)] for i in range(int(12 * length))])

        lngth_tmp = self.length
        main_part, top, bottom = '', '', ''
        while lngth_tmp > 1:
            top += '/' + fill('-', 1) + '\\'
            main_part += '|' + fill(self.fill, 1) + '|'
            bottom += '\\' + fill('-', 1) + '/'
            lngth_tmp -= 1

        top += '/' + fill('-', lngth_tmp) + ('\\' if lngth_tmp == 1 else '|')
        main_part += '|' + fill(self.fill, lngth_tmp) + '|\n'
        bottom += '\\' + fill('-', lngth_tmp) + ('/' if lngth_tmp == 1 else '|')

        return top + '\n' + main_part * 3 + bottom
