"""
F. Палиндром

Помогите Васе понять, будет ли фраза палиндромом. Учитываются только буквы и 
цифры, заглавные и строчные буквы считаются одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово. Буквы могут быть только 
латинские. Длина текста не превосходит 20000 символов.

Фраза может состоять из строчных и прописных латинских букв, цифр, знаков 
препинания.

Формат вывода
Выведите «True», если фраза является палиндромом, и «False», если не является.

Пример 1
Ввод	                          Вывод
A man, a plan, a canal: Panama
                                   True

Пример 2
Ввод	Вывод
zo
        False
"""

def palindrome(words: str) -> bool:
	
	left = 0
	right = len(words) - 1
	
	while left <= right:
		if not words[left].isalnum():
			left += 1
			continue
		if not words[right].isalnum():
			right -= 1
			continue
		if words[left].lower() != words[right].lower():
			return False
		left += 1
		right -= 1
			
	return True

def main():
	words = input()
	result = palindrome(words)
	print(result)

if __name__ == "__main__":
	main()