text = input()
mass_text = text.split()
prime_words = mass_text[0]
mass_text.pop(0)

for i in range(len(mass_text)):
    if mass_text[i]!=prime_words:
        flag = True
        for j in range(len(mass_text[i])):
            if mass_text[i].count(mass_text[i][j])>1:
                flag = False
        if flag:
            print(mass_text[i])
