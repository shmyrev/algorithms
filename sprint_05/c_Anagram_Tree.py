"""
C. Дерево - анаграмма

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Гоша и Алла играют в игру «Удивительные деревья». Помогите ребятам определить, 
является ли дерево, которое им встретилось, деревом-анаграммой?
Дерево называется анаграммой, если оно симметрично относительно своего центра.

Формат вывода
Функция должна вернуть True если дерево является анаграммой. Иначе - False.
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def compare_two(node1, node2):
    if bool(node1) == bool(node2):
        if not node1:
            return True
    else:
        return True

    if bool(node1.left) != bool(node2.left):
        return False
    if bool(node1.right) != bool(node2.right):
        return False

    return True


def solution(root):
    node1 = root.left
    node2 = root.right




def test():
    node1 = Node(3, None, None)
    node2 = Node(4, None, None)
    node3 = Node(4, None, None)
    node4 = Node(3, None, None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)