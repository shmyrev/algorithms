"""
B. Застёжка-молния

Даны два массива чисел длины n. Составьте из них один массив длины 2n, в 
котором числа из входных массивов чередуются (первый — второй — первый — 
второй — ...). При этом относительный порядок следования чисел из одного 
массива должен быть сохранён.

Формат ввода
В первой строке записано целое число n –— длина каждого из массивов, 
1 ≤ n ≤ 1000.

Во второй строке записано n чисел из первого массива, через пробел.

В третьей строке –— n чисел из второго массива.

Значения всех чисел –— натуральные и не превосходят 1000.

Формат вывода
Выведите 2n чисел из объединённого массива через пробел.

Пример 1
Ввод	  Вывод
3
1 2 3
4 5 6    1 4 2 5 3 6

Пример 2
Ввод	Вывод
1
1
2       1 2

Пример 3
Ввод	  Вывод
3
1 8 9
2 3 1    1 2 8 3 9 1
"""

n = int(input())
a = list(input().split())
b = list(input().split())
c = list()

for i in range(0, n):
	c.append(a[i])
	c.append(b[i])
		
print(" ".join(c))