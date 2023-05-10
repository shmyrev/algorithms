"""
G. Работа из дома

Вася реализовал функцию, которая переводит целое число из десятичной системы в 
двоичную. Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.

Не используйте встроенные средства языка по переводу чисел в бинарное 
представление.

Формат ввода
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода
Выведите двоичное представление этого числа.

Пример 1
Ввод	Вывод
5
         101
Пример 2
Ввод	Вывод
14
         1110
"""

def decimal_to_binary(n: int) -> str:
	if n == 0:
		return n

	binary = str()
	while n > 0:
		b = n % 2
		binary += str(b)
		n -= b
		n //= 2
	return binary[::-1]

def main():
	n = int(input())
	result = decimal_to_binary(n)
	print(result)

if __name__ == "__main__":
	main()