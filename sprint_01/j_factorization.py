"""
J. Факторизация

Основная теорема арифметики говорит: любое число раскладывается на произведение 
простых множителей единственным образом, с точностью до их перестановки. 
Например:

Число 8 можно представить как 2 × 2 × 2.
Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта 
отличаются лишь порядком следования множителей.

Разложение числа на простые множители называется факторизацией числа.

Напишите программу, которая производит факторизацию переданного числа.

Формат ввода
В единственной строке дано число n (2 ≤ n ≤ 109), которое нужно факторизовать.

Формат вывода
Выведите в порядке неубывания простые множители, на которые раскладывается 
число n.

Пример 1
Ввод	Вывод
8
        2 2 2

Пример 2
Ввод	Вывод
13
        13

Пример 3
Ввод	Вывод
100
        2 2 5 5
"""

from typing import List


def factorize(number: int) -> List[int]:
    result = []
    div = 2
    while div ** 2 <= number:
        if number % div == 0:
            number //= div
            result.append(div)
        else:
            div += 1
    if number > 1:
        result.append(number)
    return result


def main():
    print(" ".join(map(str, factorize(int(input())))))


if __name__ == '__main__':
    main()