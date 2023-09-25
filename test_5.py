text_1 = input()
text_2 = input()
text_3 = input()
for i in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю":
    if (i in text_1) and (i not in text_2) and (i not in text_3):
        print(i)
    elif (i in text_2) and (i not in text_1) and (i not in text_3):
        print(i)
    elif (i in text_3) and (i not in text_2) and (i not in text_1):
        print(i)