# Ввести построчно четвёрки вида «число число число слово»,
# где первые три числа — это координаты галактики по имени «слово»
# (некоторые галактики могут называться одинаково, но координаты у всех разные).
# Последняя строка ввода не содержит пробелов и не учитывается.
# Вывести в алфавитном порядке имена любых двух наиболее удалённых друг от друга галактик.


def distance(pair):
    t1, t2 = pair
    return (t2[0] - t1[0]) ** 2 + (t2[1] - t1[1]) ** 2 + (t2[2] - t1[2]) ** 2


list_of_galaxies = dict()
while True:
    npts = input()
    if not ' ' in npts:
        break
    *coordinates, name_of_galaxy = npts.split()
    coordinates = tuple(float(i) for i in coordinates)
    list_of_galaxies[coordinates] = name_of_galaxy
x, y = max(((i, j) for i in list_of_galaxies for j in list_of_galaxies if i > j), key=distance)
print(*sorted((list_of_galaxies[x], list_of_galaxies[y])))
