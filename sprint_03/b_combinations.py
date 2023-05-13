"""
B. Комбинации

На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько 
букв. Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов. 
Напечатайте все комбинации букв, которые можно набрать такой 
последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не 
превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.

Пример 1
Ввод	Вывод
23
        ad ae af bd be bf cd ce cf
Пример 2
Ввод	Вывод
92
        wa wb wc xa xb xc ya yb yc za zb zc
"""

def combinations(item):
    comba = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }

    def combinat(item, prefix, res):
        if item == "":
            res.append(prefix)
            return
        for combo in comba[item[0]]:
            prefix += combo
            combinat(item[1:], prefix, res)
            prefix = prefix[:-1]

    res = list()
    combinat(item, "", res)
    print(*res)


item = input()
combinations(item)