"""
A. Полиномиальный хеш

Алле очень понравился алгоритм вычисления полиномиального хеша. Помогите ей 
написать функцию, вычисляющую хеш строки s. В данной задаче необходимо 
использовать в качестве значений отдельных символов их коды в таблице ASCII.

Полиномиальный хеш считается по формуле:


Формат ввода
В первой строке дано число a (1 ≤ a ≤ 1000) –— основание, по которому считается хеш.

Во второй строке дано число m (1 ≤ m ≤ 109) –— модуль.

В третьей строке дана строка s (0 ≤ |s| ≤ 106), состоящая из больших и маленьких латинских букв.

Формат вывода
Выведите целое неотрицательное число –— хеш заданной строки.

Пример 1
Ввод	Вывод
123
100003
a
        97

Пример 2
Ввод	Вывод
123
100003
hash
        6080

Пример 3
Ввод	Вывод
123
100003
HaSH
        56156
"""

def polynomial_hash(s: str, q: int, r: int, l: int):
    if not s:
        return 0
    result = ord(s[0])
    for i in range(1, l):
        result = (result * q + ord(s[i])) % r
    return result


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    string = input()
    print(polynomial_hash(string, n, m, len(string)))