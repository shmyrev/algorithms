"""
A. Лампочки
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Гоша повесил на стену гирлянду в виде бинарного дерева, в узлах которого 
находятся лампочки. У каждой лампочки есть своя яркость. Уровень яркости 
лампочки соответствует числу, расположенному в узле дерева. Помогите Гоше найти 
самую яркую лампочку в гирлянде, то есть такую, у которой яркость наибольшая.

Формат вывода
Функция должна вернуть максимальное значение яркости в узле дерева.

"""

def solution(root):
    return find_max(root, root.value)

  
def find_max(node, max):
    if node is None:
        return max

    if node.value > max:
        max = node.value

    if node.left is None and node.right is None:
        if max > node.value:
            return max
        else:
            return node.value
    else:
        left_max = find_max(node.left, max)
        right_max = find_max(node.right, max)

        if max > left_max and max > right_max:
            return max

        if left_max > right_max:
            if max > left_max:
                return max
            return left_max
        else:
            if max > right_max:
                return max
            return right_max


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(2, node3, None)
    assert solution(node4) == 3