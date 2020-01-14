# Написать модуль, в котором будет 4 функции.
# Первые две: shex(n), которая переводит число n в 64-ричное представление,
# и xehs(s), которая переводит строку с 64-ричным числом в число. 64-ричная система счисления пользуется
# «цифрами» с ASCII-кодом от 32 до 32+63=95 (т. е. от пробела до подчёркивания) включительно.
# Функция encode(txt) упаковывает строку txt, состоящую из символов диапазона " "…"_" по следующим правилам.
# Символы, встретившиеся в тексте, упорядочиваются по убыванию частоты их появления в тексте
# (вторичный ключ — сам символ). Самому частому (и с наибольшим ASCII-кодом, если таковых несколько)
# ставится в соответствие бит "0", следующему — последовательность битов "10", следующему — "110", и т. д.
# Биты записываются единой строкой, строка дополняется нулями, если это необходимо, и превращается в 64-ричное число.
# Функция encode(txt) возвращает кортеж (длина txt, строка упорядоченных символов, закодированная строка).
# Четвёртая функция, decode(length, chars, code), раскодирует строку code, используя описанное выше
# сопоставление chars битам, и возвращает раскодированную строку длиной length.


from functools import reduce


def shex(n):
    if not hasattr(shex, 'table'):
        shex.table = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_'
    num = n
    r = []
    while num:
        x, y = divmod(num, 64)
        r.append(shex.table[y])
        num = x
    return ''.join(reversed(r))


def xehs(s):
    if not hasattr(xehs, 'table'):
        xehs.table = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_'
    result = reduce(lambda x, y: x*64+(xehs.table.find(y)), s.strip().upper(), 0)
    return result


def encode(txt):
    dictionary = {}
    for i in txt:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    keys = list(dictionary.keys())
    keys.sort(key=lambda x: (dictionary[x], x), reverse=True)

    bits_dictionary = {}
    begin = 0
    for i, val in enumerate(keys):
        v = begin
        begin += 1 << (i + 1)
        bits_dictionary[val] = (v, i + 1)

    length = 0
    result = 0
    accurcy = []
    for wd in txt:
        length += bits_dictionary[wd][1]
        result <<= bits_dictionary[wd][1]
        result += bits_dictionary[wd][0]
        while length >= 6:
            accurcy.append(chr(32 + ((result >> (length - 6)) & 63)))
            length -= 6
        result &= 63

    if length != 0:
        k = (result << (6 - length)) & 63
        accurcy.append(chr(32 + k))

    while result % 64:
        result <<= 1

    return len(txt), "".join(keys), "".join(accurcy)


def decode(length, char, code):
    dictionary = {}
    begin = 1
    for k in char:
        dictionary[begin] = k
        begin *= 2

    result = []
    tchar = 1
    decisions = xehs(code)
    while decisions:
        if decisions & 1:
            tchar *= 2
        else:
            result.append(dictionary[tchar])
            tchar = 1
        decisions >>= 1
    result.append(dictionary[tchar])
    return "".join(result[::-1][:length])
