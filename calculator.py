# Написать программу — калькулятор с переменными и обработкой ошибок
# Команда, начинающаяся на '#' — комментарий
# Команда вида Переменная=выражение задаёт переменную
# Команда вида выражение выводит значение выражения.
# Если команда содержит знак "=", но не является присваиванием, выводится диагностика "invalid assignment" (см. пример)
# Если слева от "=" находится не идентификатор, выводится диагностика "invalid identifier (см. пример)"
# В случае любых других ошибок выводится текст ошибки.
# «Выражение» — это произвольное выражение Python3, в котором вдобавок можно использовать уже определённые переменные
# (и только их). Пробелов в командах нет. Пустая команда или точка означает конец вычислений.
# Калькулятор вводит и исполняет команды по одной, тут же выводя диагностику, но в тестах это выглядит
# как ввод последовательности строк и вывод последовательности строк.
import sys


def main():
    calc_env = {}
    for line in sys.stdin:
        line = line.strip()
        if not line or line == ".":
            break
        try:
            if not line.startswith('#') and len(line) > 0:
                expr = line.split('=')
                if len(expr) == 1:
                    print(eval(line, calc_env))
                elif len(expr) == 2:
                    identifier = expr[0].strip()
                    if not identifier.isidentifier():
                        raise IndentationError(f"invalid identifier '{identifier}'")
                    calc_env[identifier] = eval(expr[1], calc_env)
                else:
                    raise AttributeError(f"invalid assignment '{line}'")
        except Exception as e:
            print(e)


global_builtins = __builtins__
if __name__ == '__main__':
    main()
