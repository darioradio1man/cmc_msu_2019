# Ввести целое положительное число и проверить, является ли оно палиндромом, т. е. совпадает ли первая цифра
# с последней, вторая — с предпоследней и т. д. Представлять число в виде последовательности (строки, списка и т. п.)
# нельзя. Вывести YES или NO соответственно. Лидирующие нули не учитывать (числа, заканчивающиеся на 0 — автоматически
# не палиндромы).


a = int(input())
n = 0
k = a
while a != 0:
    n = n * 10 + a % 10
    a //= 10
if k == n:
    print("YES")
else:
    print("NO")