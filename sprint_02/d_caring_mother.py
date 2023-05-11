"""
D. Заботливая мама

Мама Васи хочет знать, что сын планирует делать и когда. Помогите ей: напишите 
функцию solution, определяющую индекс первого вхождения передаваемого ей на 
вход значения в связном списке, если значение присутствует.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать 
только функцию, которая принимает на вход голову списка и искомый элемент, а 
возвращает целое число — индекс найденного элемента или -1.

Формат ввода
Функция на вход принимает голову односвязного списка и элемент, который нужно 
найти. Длина списка не превосходит 10000 элементов. Список не бывает пустым.

Формат вывода
Функция возвращает индекс первого вхождения искомого элемента в список
(индексация начинается с нуля). Если элемент не найден, нужно вернуть -1.
"""

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(head, node):
    count = 0
    cur_node = head
    while cur_node.next_item:
        if cur_node.value != node:
            cur_node = cur_node.next_item
            count += 1
        else:
            return count

    count = -1
    return count


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    print(solution(node0))
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == '__main__':
    test()
