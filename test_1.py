'''
Задание 1.
Дан текст. Необходимо определить максимальное количество последовательных пробельных символов  в нём.
'''


text = input()
count = 0
count_max=0
for i in range (len(text)):
    if text[i]==" ":
        count+=1
    else:
        count_max=max(count,count_max)
        count=0

print(count_max)