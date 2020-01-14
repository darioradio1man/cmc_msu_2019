# Ввести небольшое натуральное число 2⩽N⩽1000000 и проверить, является ли оно степенью натурального числа (>1).
# Вывести YES или NO соответственно.


import math
n = int(input())
pow = 2
flag = False
while pow <= int(math.sqrt(n) + 1):
    if math.log(n, pow).is_integer() and math.log(n, pow) != 1:
        print("YES")
        flag = True
        break
    pow += 1
if not flag:
    print("NO")
