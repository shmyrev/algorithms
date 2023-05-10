"""
C. Соседи

Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его 
соседей. Соседним считается элемент, находящийся от текущего на одну ячейку 
влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.

Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для 
(2, 1) –— 1, 2, 7, 7.

    0 1 2
    -----
0 | 1 2 3
1 | 0 2 6
2 | 7 4 1
3 | 2 7 0

Формат ввода
В первой строке задано n — количество строк матрицы. Во второй — количество 
столбцов m. Числа m и n не превосходят 1000. В следующих n строках задана 
матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000. В 
последних двух строках записаны координаты элемента, соседей которого нужно 
найти. Индексация начинается с нуля.

Формат вывода
Напечатайте нужные числа в возрастающем порядке через пробел.

Пример 1
Ввод	Вывод
4
3
1 2 3
0 2 6
7 4 1
2 7 0
3
0
         7 7
Пример 2
Ввод	Вывод
4
3
1 2 3
0 2 6
7 4 1
2 7 0
0
0
        0 2

"""

from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], y: int, x: int) -> List[int]:
    result = []
    if y + 1 < len(matrix):
        result.append(matrix[y + 1][x])
    if x + 1 < len(matrix[0]):
        result.append(matrix[y][x + 1])
    if y - 1 >= 0:
        result.append(matrix[y - 1][x])
    if x - 1 >= 0:
        result.append(matrix[y][x - 1])

    result.sort()
    return result


def read_input() -> Tuple[int, List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    y = int(input())
    x = int(input())
    return m, matrix, y, x


def main():
    m, matrix, y, x = read_input()
    print(" ".join(map(str, get_neighbours(matrix, y, x))))


if __name__ == '__main__':
    main()