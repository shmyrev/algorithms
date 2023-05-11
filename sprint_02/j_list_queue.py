"""
J. Списочная очередь

Любимый вариант очереди Тимофея — очередь, написанная с использованием связного 
списка. Помогите ему с реализацией. Очередь должна поддерживать выполнение трёх 
команд:

get() — вывести элемент, находящийся в голове очереди, и удалить его. Если 
очередь пуста, то вывести «error».

put(x) — добавить число x в очередь
size() — вывести текущий размер очереди
Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 
1000. В каждой из следующих n строк записаны команды по одной строке.

Формат вывода
Выведите ответ на каждый запрос по одному в строке.

Пример 1
Ввод	    Вывод
10
put -34
put -23
get
size
get
size
get
get
put 80
size
            -34
            1
            -23
            0
            error
            error
            1

Пример 2
Ввод	    Вывод
6
put -66
put 98
size
size
get
get
            2
            2
            -66
            98

Пример 3
Ввод	    Вывод
9
get
size
put 74
get
size
put 90
size
size
size
            error
            0
            74
            0
            1
            1
            1
"""

class Queue:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def put(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
    
    def get(self):
        if self.is_empty():
            return "error"
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


def main():
    n = int(input())
    q = Queue(n)
    for _ in range(n):
        data = list(input().split())
        if data[0] == "get":
            print(q.get())
        if data[0] == "put":
            q.put(data[1])
        if data[0] == "size":
            print(q.size)


if __name__ == "__main__":
    main()