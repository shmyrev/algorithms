"""
K. Списочная форма

Вася просил Аллу помочь решить задачу. На этот раз по информатике.

Для неотрицательного целого числа X списочная форма –— это массив его цифр 
слева направо. К примеру, для 1231 списочная форма будет [1,2,3,1]. На вход 
подается количество цифр числа Х, списочная форма неотрицательного числа Х и 
неотрицательное число K. Число К не превосходят 10000. Длина числа Х не 
превосходит 1000.

Нужно вернуть списочную форму числа X + K.

Формат ввода
В первой строке — длина списочной формы числа X. На следующей строке — сама 
списочная форма с цифрами записанными через пробел.

В последней строке записано число K, 0 ≤ K ≤ 10000.

Формат вывода
Выведите списочную форму числа X+K.

Пример 1
Ввод	    Вывод
4
1 2 0 0
34
            1 2 3 4

Пример 2
Ввод	Вывод
2
9 5
17
        1 1 2
"""

def list_form(X: list, K: int) -> int:
	X = "".join(X)
	X = int(X)
	S = X + K
	S = str(S)
	result = " ".join(S)
	return result

def main():
	n = input()
	X = input().split()
	K = int(input())
	result = list_form(X, K)
	print(result)

if __name__ == "__main__":
	main()