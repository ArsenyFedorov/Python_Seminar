# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.
text = "She sells sea shells on the sea shore The shells that she sells are sea shells Im sure So if she sells sea shells on the sea shore Im sure that the shells are sea shore shells"
text = text.lower()
text = text.split()
text = set(text)
text.discard('.')
text.discard('"')
text.discard(",")
print(text)
print(len(text))
