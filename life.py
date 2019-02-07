import os
import random as r
import time


def clear(): return os.system('cls')


obj = ['~', 'F', '#', ' ', ' ']  # """0 - криветка, 1 - рыбка, 2 - гора, 3 - абсолютное ничего как ты)))) """
r.seed()


def DoL(field, i, j, size):
    F = 0
    S = 0
    M = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            if (a != 0 or b != 0):
                if field[i - a][j - b] == obj[0]:
                    S += 1
                if field[i - a][j - b] == obj[1]:
                    F += 1
                if field[i - a][j - b] == obj[2]:
                    M += 1
    return [F, S, M]


class MyLife:
    def __init__(self, size):
        self.size = size + 1

    def random_generation(self):
        left = 1
        right = 1000000
        field = []
        field.append(obj[4] * (self.size + 10))
        for i in range(self.size):
            string = obj[4]
            for j in range(self.size):
                number = r.randint(left, right)
                if number % 3 == 0:
                    string += obj[0]
                    continue
                if number % 5 == 0 or number % 4 == 0:
                    string += obj[1]
                    continue
                if number % 7 == 0:
                    string += obj[2]
                    continue
                string += obj[3]
            string += obj[4]
            field.append(string)
        field.append(obj[4] * (self.size + 10))
        return field

    def do_life(self, field):
        while (True):
            clear()
            for i in range(0, self.size):
                print(field[i])
            for i in range(1, self.size):
                for j in range(1, self.size):
                    nb = DoL(field, i, j, self.size)
                    cell = field[i][j]
                    # print(cell)
                    # time.sleep(10)
                    if cell == obj[0] and (nb[1] >= 4 or nb[1] < 2):
                        s = list(field[i])
                        s[j] = obj[3]
                        field[i] = ''.join(s)
                    if cell == obj[1] and (nb[0] >= 4 or nb[0] < 2):
                        s = list(field[i])
                        s[j] = obj[3]
                        field[i] = ''.join(s)
                    if cell == obj[3]:
                        s = list(field[i])
                        if nb[0] == 3:
                            s[j] = obj[1]
                        elif nb[1] == 3:
                            s[j] = obj[0]
                        field[i] = ''.join(s)
            time.sleep(0.5)


def main():
    print("plaese input size table")
    size = int(input())
    life = MyLife(size)
    field = life.random_generation()

    life.do_life(field)
    k = int(input())


clear()
print("hello, its my game LIFE, if we want play here, please input paly else input goodbye")
a = str(input())
while (a != 'play' and a != 'goodbye'):
    clear()
    print('write play or goodbye')
    a = str(input())
if a == 'play':
    main()
