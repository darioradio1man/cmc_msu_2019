# Вводится карта проходимых в обе стороны тоннелей подземлья в виде строк,
# содержащих разделённые пробелом названия двух пещер, которые соединяет соответствующий тоннель.
# Две последние строки не содержат пробелов — это название входа в подземелье и название выхода.
# Вывести "YES", если из входа можно попасть в выход, и "NO" в противном случае.
# Пары могут повторяться или содержать одинаковые слова.


dungeons = {}
enter = input()
while " " in enter:
    enter, exit = enter.split()
    dungeons.setdefault(enter, set()).add(exit)
    dungeons.setdefault(exit, set()).add(enter)
    enter = input()
exit = input()
result, ways = set(), {enter}
while ways:
    new = set()
    for way in ways:
        new |= dungeons[way]
    result |= ways
    ways = new - result
print("YES" if exit in result else "NO")
