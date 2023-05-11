"""
G. Стек - MaxEffective

Реализуйте класс StackMaxEffective, поддерживающий операцию определения 
максимума среди элементов в стеке. Сложность операции должна быть O(1). Для 
пустого стека операция должна возвращать None. При этом push(x) и pop() также 
должны выполняться за константное время.

Формат ввода
В первой строке записано одно число — количество команд, оно не превосходит 
100000. Далее идут команды по одной в строке. Команды могут быть следующих 
видов:

push(x) — добавить число x в стек;
pop() — удалить число с вершины стека;
get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None», для команды 
pop — «error».
Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения. Если стек 
пустой, для команды get_max() напечатайте «None». Если происходит удаление из 
пустого стека — напечатайте «error».

Пример 1
Ввод	        Вывод
10
pop
pop
push 4
push -5
push 7
pop
pop
get_max
pop
get_max
                error
                error
                4
                None

Пример 2
Ввод	        Вывод
10
get_max
push -6
pop
pop
get_max
push 2
get_max
pop
push -2
push -6
                None
                error
                None
                2
"""

class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max = []

    def push(self, item):
        if len(self.max) == 0:
            self.max.append(item)
        elif item > self.max[-1]:
            self.max.append(item)
        else:
            self.max.append(self.max[-1])
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return 'error'
        self.max.pop()
        return self.items.pop()

    def get_max(self):
        if self.is_empty():
            return 'None'
        return self.max[-1]

    def is_empty(self):
        return self.items == []


def main():
    n = int(input())

    stack_max_eff = StackMaxEffective()
    result = []

    for i in range(n):
        item = input().split()
        if item[0] == 'push':
            stack_max_eff.push(int(item[1]))
        elif item[0] == 'pop':
            if stack_max_eff.pop() == 'error':
                result.append('error')
        elif item[0] == 'get_max':
            result.append(stack_max_eff.get_max())
    for i in result:
        print(i)


if __name__ == '__main__':
    main()