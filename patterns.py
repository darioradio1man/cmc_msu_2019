# Ввести строку, содержащую произвольные символы (кроме символа «@»). Затем ввести строку-шаблон, которая может
# содержать символы '@'. Проверить, содержится ли в исходной строке подстрока, совпадающая со строкой-шаблоном везде,
# кроме символов '@'; на месте '@' в исходной строке должен стоять ровно один произвольный символ.
# Вывести наименьшую позицию в строке, с которой начинается эта подстрока, или '-1', если её там нет.
# Использовать регулярные выражения нельзя!


text_input = input()
pattern = input()

k, start, length, meta, i = 0, -1, 0, 0, 0

while i < len(text_input):
    if k == 0:
        start = i
    if text_input[i] == pattern[k]:
        k += 1
        length += 1
    elif pattern[k] == '@':
        k += 1
        length += 1
        meta += 1
    else:
        if meta:
            i -= meta
            meta = 0
        k, length = 0, 0

    if length == len(pattern):
        break
    elif i == len(text_input) - 1:
        start = -1
    i += 1

print(start)
