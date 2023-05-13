"""
L. Два велосипеда

Вася решил накопить денег на два одинаковых велосипеда — себе и сестре. У Васи 
есть копилка, в которую каждый день он может добавлять деньги (если, конечно, у 
него есть такая финансовая возможность). В процессе накопления Вася не вынимает 
деньги из копилки.

У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке 
было денег в каждый из дней.

Ваша задача — по заданной стоимости велосипеда определить

первый день, в которой Вася смог бы купить один велосипед,
и первый день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).

Формат ввода
В первой строке дано число дней n, по которым велись наблюдения за Васиными 
накоплениями. 1 ≤ n ≤ 106.

В следующей строке записаны n целых неотрицательных чисел. Числа идут в порядке 
неубывания. Каждое из чисел не превосходит 106.

В третьей строке записано целое положительное число s — стоимость велосипеда. 
Это число не превосходит 106.

Формат вывода
Нужно вывести два числа — номера дней по условию задачи.

Если необходимой суммы в копилке не нашлось, нужно вернуть -1 вместо номера дня.

Пример 1
Ввод	        Вывод
6
1 2 4 4 6 8
3
                3 5

Пример 2
Ввод	        Вывод
6
1 2 4 4 4 4
3
                3 -1

Пример 3
Ввод	        Вывод
6
1 2 4 4 4 4
10
                -1 -1
"""

def one_bicycle(arr: list, item: int, left: int, right: int):
    if left >= right:
        return -1
    mid = (left + right) // 2
    if item <= arr[mid]:
        if mid != 0:
            if item <= arr[mid-1]:
                return one_bicycle(arr, item, left, mid)
        return mid + 1
    elif item < arr[mid]:
        return one_bicycle(arr, item, left, mid)
    else:
        return one_bicycle(arr, item, mid+1, right)

def two_bicycles(arr: list, item: int, left: int, right: int):
    if left >= right:
        return -1
    mid = (left + right) // 2
    sum = arr[mid] // 2
    if item <= sum:
        if mid != 0:
            sum2 = arr[mid-1] // 2
            if item <= sum2:
                return two_bicycles(arr, item, left, mid)
        return mid + 1

    else:
        return two_bicycles(arr, item, mid+1, right)

def main():
    count = int(input())
    arr = list(map(int, input().split()))
    item = int(input())

    left = 0
    right = count

    res1 = one_bicycle(arr, item, left, right)
    res2 = two_bicycles(arr, item, left, right)

    print(res1, res2)


if __name__ == "__main__":
    main()
