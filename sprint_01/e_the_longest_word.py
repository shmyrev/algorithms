"""
E. Самое длинное слово

Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному 
менеджменту. Так как Гоша хочет спланировать день заранее, ему необходимо 
оценить сложность статьи.

Он придумал такой метод оценки: берётся случайное предложение из текста и в нём 
ищется самое длинное слово. Его длина и будет условной сложностью статьи.

Помогите Гоше справиться с этой задачей.

Формат ввода
В первой строке дана длина текста L (1 ≤ L ≤ 10^5).

В следующей строке записан текст, состоящий из строчных латинских букв и 
пробелов. Слово —– последовательность букв, не разделённых пробелами. Пробелы 
могут стоять в самом начале строки и в самом её конце. Текст заканчивается 
переносом строки, этот символ не включается в число остальных L символов.

Формат вывода
В первой строке выведите самое длинное слово. Во второй строке выведите его 
длину. Если подходящих слов несколько, выведите то, которое встречается раньше.

Пример 1
Ввод	               Вывод
19
i love segment tree
                       segment
                          7

Пример 2
Ввод	                Вывод
21
frog jumps from river
                        jumps
                         5
"""

def proposal(n: int, words: list) -> str:
	count_word = dict()
	
	for word in words:
		if len(word) in count_word:
			continue
		count_word[len(word)] = word

	max_count = max(count_word.keys())
	max_word = count_word.get(max_count)
	return f"{max_word}\n{max_count}"

def main():
	n = int(input())
	words = list(map(str, input().split()))
	result = proposal(n, words)
	print(result)

if __name__ == "__main__":
	main()