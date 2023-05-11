"""
A. Дек

Гоша реализовал структуру данных Дек, максимальный размер которого определяется 
заданным числом. Методы push_back(x), push_front(x), pop_back(), pop_front() 
работали корректно. Но, если в деке было много элементов, программа работала 
очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите 
Гоше! Напишите эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 
100000. Во второй строке записано число m — максимальный размер дека. Он не 
превосходит 50000. В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека. Если в деке уже находится 
максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится 
максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то 
вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, 
то вывести «error».
Value — целое число, по модулю не превосходящее 1000.
Формат вывода
Выведите результат выполнения каждой команды на отдельной строке. Для успешных 
запросов push_back(x) и push_front(x) ничего выводить не надо.

Пример 1
Ввод	            Вывод
4
4
push_front 861
push_front -819
pop_back
pop_back
                    861
                    -819

Пример 2
Ввод	            Вывод
7
10
push_front -855
push_front 0
pop_back
pop_back
push_back 844
pop_back
push_back 823
                    -855
                    0
                    844

Пример 3
Ввод	            Вывод
6
6
push_front -201
push_back 959
push_back 102
push_front 20
pop_front
pop_back
                    20
                    102
"""

class Deque:
    def __init__(self, max_size: int) -> None:
        self._deque = [None] * max_size
        self._max_size = max_size
        self._head = 0
        self._tail = 0
        self._size = 0

    @property
    def is_empty(self) -> bool:
        return self._size == 0
    
    @property
    def is_not_full(self) -> bool:
        return self._size != self._max_size

    def push_front(self, item: int) -> None:
        if self.is_not_full:
            self._deque[self._head - 1] = item
            self._head = (self._head - 1) % self._max_size
            self._size += 1
        else:
            raise ValueError

    def push_back(self, item: int) -> None:
        if self.is_not_full:
            self._deque[self._tail] = item
            self._tail = (self._tail + 1) % self._max_size
            self._size += 1
        else:
            raise ValueError

    def pop_front(self) -> int:
        if self.is_empty:
            raise ValueError
        item = self._deque[self._head]
        self._deque[self._head] = None
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return item

    def pop_back(self) -> int:
        if self.is_empty:
            raise ValueError
        item = self._deque[self._tail - 1]
        self._deque[self._tail - 1] = None
        self._tail = (self._tail - 1) % self._max_size
        self._size -= 1
        return item


def main():
    count = int(input())
    max_size = int(input())
    deque = Deque(max_size)
    for _ in range(count):
        cmd, *item = input().split()
        if not item:
            try:
                print(getattr(deque, cmd)())
            except ValueError:
                print('error')
        else:
            try:
                getattr(deque, cmd)(*item)
            except ValueError:
                print('error')


if __name__ == '__main__':
    main()