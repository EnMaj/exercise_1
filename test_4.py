'''
Задание 4.
Определите какой символ встречается ровно три раза в тексте. Гарантируется, что символ
с такой частотой встречаемости только один.
'''


text = input()
words = []
count = 0
for i in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю":
    count = text.count(i)
    if count == 3:
        print(i)
        break