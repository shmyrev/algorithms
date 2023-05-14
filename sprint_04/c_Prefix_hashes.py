"""
C. Префиксные хеши

Алла не остановилась на достигнутом –— теперь она хочет научиться быстро 
вычислять хеши произвольных подстрок данной строки. Помогите ей!

На вход поступают запросы на подсчёт хешей разных подстрок. Ответ на каждый 
запрос должен выполняться за O(1). Допустимо в начале работы программы сделать 
предподсчёт для дальнейшей работы со строкой.

Напомним, что полиномиальный хеш считается по формуле


В данной задаче необходимо использовать в качестве значений отдельных символов 
их коды в таблице ASCII.

Формат ввода
В первой строке дано число a (1 ≤ a ≤ 1000) –— основание, по которому считается 
хеш. Во второй строке дано число m (1 ≤ m ≤ 107) –— модуль. В третьей строке 
дана строка s (0 ≤ |s| ≤ 106), состоящая из больших и маленьких латинских букв.

В четвертой строке дано число запросов t –— натуральное число от 1 до 105. В 
каждой из следующих t строк записаны через пробел два числа l и r –— индексы 
начала и конца очередной подстроки. (1 ≤ l ≤ r ≤ |s|).

Формат вывода
Для каждого запроса выведите на отдельной строке хеш заданной в запросе подстроки.

Пример 1
Ввод	    Вывод
1000
1000009
abcdefgh
7
1 1
1 5
2 3
3 4
4 4
1 8
5 8
            97
            225076
            98099
            99100
            100
            436420
            193195

Пример 2
Ввод	Вывод
100
10
a
1
1 1
        7
"""

import sys


def main():
    a = int(input())
    m = int(input())
    string = sys.stdin.readline().rstrip()
    t = int(input())

    prefixes = [0] * (len(string) + 1)
    for i in range(1, len(string) + 1):
        prefixes[i] = (prefixes[i-1] * a % m + ord(string[i-1])) % m

    for i in range(t):
        line = sys.stdin.readline().rstrip()
        numbers = list(map(int, line.split()))
        left = numbers[0]
        right = numbers[1]

        hash = (prefixes[right] - (prefixes[left-1] * pow(a, right-left+1, m))) % m
        print(hash)


if __name__ == '__main__':
    main()