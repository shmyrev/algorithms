"""
C. Нелюбимое дело

Вася размышляет, что ему можно не делать из того списка дел, который он 
составил. Но, кажется, все пункты очень важные! Вася решает загадать число и 
удалить дело, которое идёт под этим номером. Список дел представлен в виде 
односвязного списка. Напишите функцию solution, которая принимает на вход 
голову списка и номер удаляемого дела и возвращает голову обновлённого списка.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать 
только функцию, которая принимает на вход голову списка и номер удаляемого 
элемента и возвращает голову обновлённого списка.

Формат вывода
Верните голову списка, в котором удален нужный элемент.
"""

class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def get_node_by_index(head, index):
    while index:
        head = head.next_item
        index -= 1
    return head


def insert_node(head, index, data):
    new_node = Node(data)
    if index == 0:
        new_node.next_item = head
        return new_node
    prev_node = get_node_by_index(head, index-1)
    new_node.next_item = prev_node.next_item
    prev_node.next_item = new_node
    return head


def solution(head, index):
    if index == 0:
        head = head.next_item
    else:
        prev_node = get_node_by_index(head, index-1)
        next_node = get_node_by_index(head, index+1)
        prev_node.next_item = next_node
    return head


def printLinkedList(node):
    while node:
        print(node.value)
        node = node.next_item


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    # insert_node(node0, 2, "node5")
    solution(node0, 2)
    printLinkedList(node0)


if __name__ == '__main__':
    test()
