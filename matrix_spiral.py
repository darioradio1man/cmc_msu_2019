# Ввести целые M и N, вывести последовательность 0 1 2 3 4 5 6 7 8 9 0 1 2 3 … в виде спирально
# (по часовой стрелке, из верхнего левого угла) заполненной таблицы N×M (N строк, M столбцов).
# Не забываем про то, что M и N могут быть чётными, нечётными и неизвестно, какое больше.


m, n = map(int, input().split(','))
a = [[0 for j in range(m)] for i in range(n)]

k, l, p = 0, 0, -1
while k < m and l < n:
    for i in range(l, n):
        p += 1
        a[k][i] = p % 10
    k += 1
    for i in range(k, m):
        p += 1
        a[i][n - 1] = p % 10
    n -= 1
    if k < m:
        for i in range(n - 1, l - 1, -1):
            p += 1
            a[m - 1][i] = p % 10
        m -= 1
    if l < n:
        for i in range(m - 1, k - 1, -1):
            p += 1
            a[i][l] = p % 10
        l += 1
for row in a:
    print(' '.join([str(elem) for elem in row]))

