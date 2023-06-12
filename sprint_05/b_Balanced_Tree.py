"""
B. Сбалансированное дерево

Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Гоше очень понравилось слушать рассказ Тимофея про деревья. Особенно часть про 
сбалансированные деревья. Он решил написать функцию, которая определяет, 
сбалансировано ли дерево.
Дерево считается сбалансированным, если левое и правое поддеревья каждой 
вершины отличаются по высоте не больше, чем на единицу.

Формат вывода
Функция должна вернуть True, если дерево сбалансировано в соответствии с 
критерием из условия, иначе - False.
"""

def solution(root):
    if root is None:
        return True
 
    lh = height(root.left)
    rh = height(root.right)

    if (abs(lh - rh) <= 1) and solution(root.left) is True and solution(root.right) is True:
        return True
 
    return False


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)