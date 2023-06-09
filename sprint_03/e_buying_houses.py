"""
E. Покупка домов

Тимофей решил купить несколько домов на знаменитом среди разработчиков 
Алгосском архипелаге. Он нашёл n объявлений о продаже, где указана стоимость 
каждого дома в алгосских франках. А у Тимофея есть k франков. Помогите ему 
определить, какое наибольшее количество домов на Алгосах он сможет приобрести 
за эти деньги.

Формат ввода
В первой строке через пробел записаны натуральные числа n и k.

n — количество домов, которые рассматривает Тимофей, оно не превосходит 100000;

k — общий бюджет, не превосходит 100000;

В следующей строке через пробел записано n стоимостей домов. Каждое из чисел не 
превосходит 100000. Все стоимости — натуральные числа.

Формат вывода
Выведите одно число —– наибольшее количество домов, которое может купить Тимофей.

Пример 1
Ввод	    Вывод
3 300
999 999 999
            0

Пример 2
Ввод	    Вывод
3 1000
350 999 200
            2
"""

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

def solution():
    arr.sort()
    idx = 0
    result = []
    if len(arr) == 1 and arr[0] <= k:
        return 1
    elif len(arr) == 1 and arr[0] > k:
        return 0
    while sum(result) + arr[idx] <= k:
        result.append(arr[idx])
        idx += 1
    return len(result)
print(solution())