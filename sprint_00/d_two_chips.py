"""
D. Две фишки

Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано 
количество очков. Сначала Гоша называет число k, затем Рита должна выбрать две 
фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки 
программирования для решения этой задачи. Помогите ей написать программу для 
поиска нужных фишек.

Формат ввода
В первой строке записано количество фишек n, 2 ≤ n ≤ 104.

Во второй строке записано n целых чисел —– очки на фишках Риты в диапазоне от 
-10^5 до 10^5.

В третьей строке —– загаданное Гошей целое число k, -10^5 ≤ k ≤ 10^5.

Формат вывода
Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.

Если таких пар несколько, то можно вывести любую из них.

Если таких пар не существует, то вывести «None».

Пример 1
Ввод	                Вывод
6
-1 -1 -9 -7 3 -6
2
                        -1 3

Пример 2
Ввод	                 Вывод
8
6 2 8 -3 1 1 6 10
100
                         None
"""

def twosum(numbers, X):
    for i in range(0, len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == X:
                return numbers[i], numbers[j]
    return None

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    X = int(input())
    result = twosum(numbers, X)
    if result is None:
        print(None)
    else:
        print(" ".join(list(map(str, result))))

if __name__ == "__main__":
    main()