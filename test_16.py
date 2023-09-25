text = input()
flag = True

for i in range(len(text)):
    if flag:
        if text[i] == "(":
            flag = False
        elif text[i] == ")":
            print("Скобки расставлены неправильно")
            break
    elif flag == False:
        if text[i] == ")":
            flag = True
        elif text[i] == "(":
            print("Скобки расставлены неправильно")
            break
    if flag == False and i==len(text)-1:
        print("Скобки расставлены неправильно")

if flag:
    print("Все скобки расставлены правильно")
