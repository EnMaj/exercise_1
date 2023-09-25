'''
Задание 3.
Дан текст. Определить, сколько различных букв в нем.
'''


text = input()
words = []
count = 0
for i in range(len(text)):
    if text[i] not in words:
        count+=1
        words+=text[i]
print(words)
print(count)