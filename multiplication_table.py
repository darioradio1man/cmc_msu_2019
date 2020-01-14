# Ввести два натуральных числа через запятую: N и M. Вывести таблицу умножения от 1 до N включительно в формате,
# представленном ниже. Количество столбцов в выводе должно быть наибольшим, но общая ширина строки не должна
# превышать M (предполагается, что M достаточно велико, чтобы вместить один столбец). Ширина колонок под сомножители и
# произведения должна соответствовать максимальной ширине соответствующего значения (даже если в данной колонке данного
# столбца эта ширина не достигается, см. пример). Таким образом все столбцы должны быть одинаковой ширины, без учёта
# пробелов в конце строк, которых быть не должно. Разделители вида "===…===" должны быть ширины M.


n, m = eval(input())
index = 1
nlen, multlen = len(str(n)), len(str(n*n))

lencol = len(f"{n} * {n} = {n*n}")
lenrow = (m+3) // (lencol+3)

print('=' * m)
for k in range(n // lenrow):
    for i in range(n):
        text = ""
        for j in range(lenrow):
            text += f"{index:>{nlen}} * {i + 1:<{nlen}} = {index * (i + 1):<{multlen}} | "
            index += 1
        text = text[:-3]
        print(text)
        index -= lenrow
    print("=" * m)
    index += lenrow

for i in range(n):
    text = ""
    for j in range(n % lenrow):
        text += f"{index:>{nlen}} * {i + 1:<{nlen}} = {index * (i + 1):<{multlen}} | "
        index += 1
    text = text[:-3]
    print(text)
    index -= n % lenrow
if n % lenrow:
    print("=" * m)
