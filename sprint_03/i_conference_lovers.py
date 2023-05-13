"""
I. Любители конференций

На IT-конференции присутствовали студенты из разных вузов со всей страны. Для 
каждого студента известен ID университета, в котором он учится.

Тимофей предложил Рите выяснить, из каких k вузов на конференцию пришло больше 
всего учащихся.

Формат ввода
В первой строке дано количество студентов в списке —– n (1 ≤ n ≤ 15 000).

Во второй строке через пробел записаны n целых чисел —– ID вуза каждого 
студента. Каждое из чисел находится в диапазоне от 0 до 10 000.

В третьей строке записано одно число k.

Формат вывода
Выведите через пробел k ID вузов с максимальным числом участников. Они должны 
быть отсортированы по убыванию популярности (по количеству гостей от 
конкретного вуза). Если более одного вуза имеет одно и то же количество 
учащихся, то выводить их ID нужно в порядке возрастания.

Пример 1
Ввод	        Вывод
7
1 2 3 1 2 3 4
3
                1 2 3

Пример 2
Ввод	        Вывод
6
1 1 1 2 2 3
1
                1
"""

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
arr.sort()
max_arr = arr[-1]
id_dict = {k:0 for k in reversed(range(1,max_arr+1))}

def solution():
    for i in arr:
        id_dict[i] += 1
    from operator import itemgetter
    sorted_tuple = sorted(id_dict.items(), key=itemgetter(1))
    return sorted_tuple
result_dict = solution()
result_str = ''
result_dict.reverse()
for key, val in result_dict:
    if k == 0:
        break
    result_str += f'{key} '
    k -= 1
print(result_str)