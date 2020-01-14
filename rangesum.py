# Вводится кортеж пар натуральных чисел. Это координаты отрезков на прямой. Рассмотрим объединение этих отрезков и
# найдём длину этого объединения (т. е. совокупную длину всех «закрашенных» нашими отрезками отрезков на прямой).


a = [list(x) for x in eval(input())]
b = []
cnt = 0
for begin, end in sorted(a):
    if b and b[-1][1] >= begin:
        b[-1][1] = max(b[-1][1], end)
    else:
        b.append([begin, end])
for idx in b:
    cnt += max(idx) - min(idx)
print(cnt)
