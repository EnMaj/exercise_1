import keyword

text = input()
flag = True

if text[0] in "1234567890":
    flag = False

if flag:
    for i in range(len(text)):
        if text[i].upper() not in "QWERTYUIOPASDFGHJKLZXCVBNM_1234567890":
            flag = False
            break

if flag and keyword.iskeyword(text):
        flag = False

if flag:
    print("Может")
else:
    print("Не может")
