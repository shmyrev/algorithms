"""
B. A+B 2

Даны два числа A и B. Вам нужно вычислить их сумму A+B. В этой задаче вам нужно
читать из файла и выводить ответ в файл

Формат ввода
Первая строка входного файла содержит числа A и B (-2 ⋅ 109 ≤ A, B ≤ 2 ⋅ 109)
разделенные пробелом

Формат вывода
В единственной строке выходного файла выведите сумму чисел A+B
"""

with open("input.txt", "r") as fr:
	for item in fr:
		data = item

a, b = data.split()
summa = int(a) + int(b)

with open("output.txt", "w") as fw:
	fw.write(str(summa))
