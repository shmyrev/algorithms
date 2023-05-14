"""
G. Соревнование

Жители Алгосов любят устраивать турниры по спортивному программированию. Все 
участники разбиваются на пары и соревнуются друг с другом. А потом два самых 
сильных программиста встречаются в финальной схватке, которая состоит из 
нескольких раундов. Если в очередном раунде выигрывает первый участник, в 
таблицу с результатами записывается 0, если второй, то 1. Ничьей в раунде быть 
не может.

Нужно определить наибольший по длине непрерывный отрезок раундов, по 
результатам которого суммарно получается ничья. Например, если дана 
последовательность 0 0 1 0 1 1 1 0 0 0, то раунды с 2-го по 9-й (нумерация 
начинается с единицы) дают ничью.

Формат ввода
В первой строке задаётся n (0 ≤ n ≤ 105) –— количество раундов. Во второй 
строке через пробел записано n чисел –— результаты раундов. Каждое число равно 
либо 0, либо 1.

Формат вывода
Выведите длину найденного отрезка.

Пример 1
Ввод	Вывод
2
0 1
        2

Пример 2
Ввод	Вывод
3
0 1 0
        2
"""

import sys


def main():
    n = int(input())
    line = sys.stdin.readline().rstrip()
    arr = list(map(int, line.split()))

    sum = 0
    sums = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        if arr[i] == 0:
            sum -= 1
        else:
            sum += 1
        sums[i+1] = sum;

    dict = {}
    for i in range(len(sums)):
        list_by_sum = dict.get(sums[i])
        if list_by_sum is None:
            list_by_sum = [i]
            dict.setdefault(sums[i], list_by_sum)
        else:
            list_by_sum.append(i)

    max_length = 0
    for i in range(len(sums)):
        list_by_sum = dict.get(sums[i])

        if list_by_sum is None:
            continue

        length = abs(list_by_sum[-1]-i);
        if length > max_length:
            max_length = length;

    print(max_length)


if __name__ == '__main__':
    main()