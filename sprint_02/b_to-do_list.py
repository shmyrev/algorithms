"""
B. Список дел

Васе нужно распечатать свой список дел на сегодня. Помогите ему: напишите 
функцию, которая печатает все его дела. Известно, что дел у Васи не больше 
5000.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать 
только функцию, которая принимает на вход голову списка и печатает его 
элементы. Ниже дано описание структуры, которая задаёт узел списка.

Формат ввода
В качестве ответа сдайте только код функции, которая печатает элементы списка. 
Длина списка не превосходит 5000 элементов. Список не бывает пустым.
"""

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node):
    while node:
        print(node.value, end="\n")
        node = node.next_item
    return node


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    print(solution(node0))


if __name__ == '__main__':
    test()