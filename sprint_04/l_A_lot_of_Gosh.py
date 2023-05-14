"""
L. МногоГоша

Дана длинная строка, состоящая из маленьких латинских букв. Нужно найти все её подстроки длины n, которые встречаются хотя бы k раз.

Формат ввода
В первой строчке через пробел записаны два натуральных числа n и k.

Во второй строчке записана строка, состоящая из маленьких латинских букв. Длина строки 1 ≤ L ≤ 106.

n ≤ L, k ≤ L.

Формат вывода
Для каждой найденной подстроки выведите индекс начала её первого вхождения (нумерация в строке начинается с нуля).

Выводите индексы в любом порядке, в одну строку, через пробел.

Пример 1
Ввод	                            Вывод
10 2
gggggooooogggggoooooogggggssshaa
                                    0 5

Пример 2
Ввод	                            Вывод
3 4
allallallallalla
                                    0 1 2
"""