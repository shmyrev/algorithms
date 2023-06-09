"""
L. Лишняя буква

Васе очень нравятся задачи про строки, поэтому он придумал свою. Есть 2 строки 
s и t, состоящие только из строчных букв. Строка t получена перемешиванием букв 
строки s и добавлением 1 буквы в случайную позицию. Нужно найти добавленную 
букву.

Формат ввода
На вход подаются строки s и t, разделённые переносом строки. Длины строк не 
превосходят 1000 символов. Строки не бывают пустыми.

Формат вывода
Выведите лишнюю букву.

Пример 1
Ввод	Вывод
abcd
abcde
        e

Пример 2
Ввод	Вывод
go
ogg
        g
Пример 3
Ввод	Вывод
xtkpx
xkctpx
        c
"""

def extra_letter(s: list, t: list) -> str:
    
    for sing in s:
        if sing in t:
            t.remove(sing)

    result = "".join(t)
    return result


def main():
    s = list(map(str, input()))
    t = list(map(str, input()))
    result = extra_letter(s, t)
    print(result)

if __name__ == "__main__":
    main()