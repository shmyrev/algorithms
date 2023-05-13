"""
L. Фибоначчи по модулю

У Тимофея было очень много стажёров, целых N (0 ≤ N ≤ 10^6) человек. Каждый 
тажёр хотел быть лучше своих предшественников, поэтому i-й стажёр делал столько 
коммитов, сколько делали два предыдущих стажёра в сумме. Два первых стажёра 
были менее инициативными — они сделали по одному коммиту.

Пусть F^i —– число коммитов, сделанных i-м стажёром (стажёры нумеруются с 
нуля). Первые два стажёра сделали по одному коммиту: F0=F1=1. Для всех i≥ 2 
выполнено Fi=Fi−1+Fi−2.

Определите, сколько кода напишет следующий стажёр –— найдите последние k цифр 
числа Fn.


Как найти k последних цифр

Чтобы вычислить k последних цифр некоторого числа x, достаточно взять остаток 
от его деления на число 10k. Эта операция обозначается как x mod 10k. Узнайте, 
как записывается операция взятия остатка по модулю в вашем языке 
программирования.

Также обратите внимание на возможное переполнение целочисленных типов, если в 
вашем языке такое случается.

Формат ввода
В первой строке записаны через пробел два целых числа n (0 ≤ n ≤ 106) и 
k (1 ≤ k ≤ 8).

Формат вывода
Выведите единственное число – последние k цифр числа Fn.

Если в искомом числе меньше k цифр, то выведите само число без ведущих нулей.

Пример 1
Ввод	Вывод
3 1
         3

Пример 2
Ввод	Вывод
10 1
         9
"""

n, k = (int(i) for i in input().split())
ab = [1, 1]
d=(10 ** k)
if n < 2:
    fib = 1
else:
    n -= 1
    for i in range(n):
        s = (ab[0] + ab[1]) % d
        ab[0] = ab[1]
        ab[1] = s
        fib = ab[1]
print(fib)