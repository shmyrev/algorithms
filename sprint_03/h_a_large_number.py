"""
H. Большое число

Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из 
которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.

Пример 1
Ввод	    Вывод
3
15 56 2
            56215

Пример 2
Ввод	    Вывод
3
1 783 2
            78321

Пример 3
Ввод	    Вывод
5
2 4 5 2 10
            542210
"""

def bubble_sort(number, source_array):
    for i in range(number - 1):
        for j in range(0, number-i-1):
            var1 = source_array[j] + source_array[j+1]
            var2 = source_array[j + 1] + source_array[j]
            if var1 < var2:
                source_array[j], source_array[j+1] = source_array[j+1], source_array[j]
                
    print("".join(source_array))

if __name__ == '__main__':
    number = int(input())
    source_array = input().split(' ')
    bubble_sort(number, source_array)
