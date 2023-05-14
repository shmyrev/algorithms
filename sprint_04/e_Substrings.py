"""
E. Подстроки

На вход подается строка. Нужно определить длину наибольшей подстроки, которая 
не содержит повторяющиеся символы.

Формат ввода
Одна строка, состоящая из строчных латинских букв. Длина строки не превосходит 
10 000.

Формат вывода
Выведите натуральное число —– ответ на задачу.

Пример 1
Ввод	    Вывод
abcabcbb
            3

Пример 2
Ввод	    Вывод
bbbbb
            1
"""

import sys


def main():
    s = str(input())

    if len(s) == 1:
        print(1)
        return

    max_length = 0
    current_dict = {}
    i = 0
    while i < len(s):
        if s[i] not in current_dict:
            current_dict.setdefault(s[i], i)
            i += 1
        else:
            max_length = get_max(max_length, len(current_dict))
            previous_index = current_dict[s[i]]
            i = previous_index + 1
            current_dict.clear()

    max_length = get_max(max_length, len(current_dict))
    print(max_length)

def get_max(current_max, new_value):
    if new_value > current_max:
        return new_value
    return current_max

  
if __name__ == '__main__':
    main()