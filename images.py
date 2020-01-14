# Вводятся строки, содержащие четыре целых числа и символ, разделённые пробелами.
# Код символа 32 < c < 128. Это абсцисса, ордината (ось ординат направлена вниз) некоторых точек, а также длина
# и ширина построенных на них прямоугольников, «нарисованных» с помощью указанных символов.
# Последняя строка начинается на четыре нуля (никаких трюков с -0 на этот раз ☺). Вывести наименьшую область,
# содержащюю все раскрашенные точки, нарисованные в порядке ввода прямоугольников. Область также прямоугольна и
# изначально заполнена символами '.'. Координаты и размеры могут быть отрицательны (в этом случае прямогуольник
# откладывается от исходной точки в противоположную сторону, а сама точка в него не попадает) или равны нулю.


strings = input()
x = []
y = []
sym = []

while not strings.startswith("0 0 0 0"):
    it = strings.split()
    if it[2] != "0" and it[3] != "0":
        x.append(tuple(sorted([int(it[0]), int(it[0]) + int(it[2])])))
        y.append(tuple(sorted([int(it[1]), int(it[1]) + int(it[3])])))
        sym.append(it[4])
    strings = input()


max_x, min_x = max(map(max, x)), min(map(min, x))
max_y, min_y = max(map(max, y)), min(map(min, y))

size_x = max_x - min_x
size_y = max_y - min_y

A = [["." for i in range(size_x)] for j in range(size_y)]
for k in range(len(sym)):
    for i in range(y[k][0] - min_y, y[k][1] - min_y):
        A[i][x[k][0] - min_x:x[k][1] - min_x] = list(sym[k] * (x[k][1] - x[k][0]))

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end='')
    print()
