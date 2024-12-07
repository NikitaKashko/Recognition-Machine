import os


def clear():
    os.system('cls')


class Validator():
    def __init__(self):
        self.s = ''
        self.i = 0

    def match(self, ch):
        if self.i < len(self.s) and self.s[self.i] == ch:
            self.i += 1
            return True
        else:
            return False

    def check(self, word):
        self.i = 0
        self.s = word
        return self.S() == self.s

    def S(self):
        return self.P() + self.G()

    def P(self):
        if self.match('l'):
            return 'l' + self.P()
        elif self.match('r'):
            return 'r' + self.P()
        else:
            return ''

    def G(self):
        if self.match('u'):
            res = 'u' + self.P() + self.A()
            if self.match('d'):
                res += 'd' + self.P()
                return res + self.G()
            else:
                return ''
        elif self.match('d'):
            res = 'd' + self.P() + self.B()
            if self.match('u'):
                res += 'u' + self.P()
                return res + self.G()
            else:
                return ''
        else:
            return ''

    def A(self):
        if self.match('u'):
            res = 'u' + self.P() + self.A()
            if self.match('d'):
                res += 'd' + self.P() + self.A()
                return res
            else:
                return ''
        else:
            return self.P()

    def B(self):
        if self.match('d'):
            res = 'd' + self.P() + self.B()
            if self.match('u'):
                res += 'u' + self.P() + self.B()
                return res
            else:
                return ''
        else:
            return self.P()


INFO_STR = (
    'Эта программа для проверки принадлжености слов\n'
    'языку путей робота, возвращающихся на ось абсцисс\n'
    'Символ r означает движение на одну клетку вправо\n'
    'Символ l означает движение на одну клетку влево\n'
    'Символ u означает движение на одну клетку вверх\n'
    'Символ d означает движение на одну клетку вниз\n'
    'Условием для возвращения на ось абсцисс является\n'
    'одинковое количество символов d и u в маршруте\n'
    'Программу написал: Кашко Никита\n'
    'Почта для связи: kashkonikev@gmail.com\n'
)


def main():
    val = Validator()
    print('Добро пожаловать в программу для распознавания!')
    while True:
        print('Для подробной информации введите команду - info')
        print('Для ввода слова введите команду - rec')
        print('Для выхода из программы введите - exit')
        s = input('Введите команду: ')
        match s:
            case 'exit':
                break
            case 'rec':
                clear()
                s = input('Введите слово для распознавания: ')
                if val.check(s):
                    print('Слово принадлежит языку')
                else:
                    print('Слово не принадлежит языку')
            case 'info':
                clear()
                print(INFO_STR)
            case _:
                clear()
                print('Неизвестная команда, введите другую')


if __name__ == '__main__':
    main()
