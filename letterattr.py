# Написать класс LetterAttr, в котором будут допустимы поля с любым именем; значение каждого поля по умолчанию
# будет совпадать с именем поля (строка), а при задании нового строкового значения туда будут попадать только буквы,
# встречающиеся в имени поля.


class LetterAttr:
    def __getattr__(self, item):
        return item

    def __setattr__(self, key, value):
        name_letters = set(key)
        object.__setattr__(self, key, ''.join([letter for letter in value if letter in name_letters]))


A = LetterAttr()
print(A.letter)
print(A.digit)
A.letter = "teller"
print(A.letter)
A.letter = "fortune teller"
print(A.letter)
