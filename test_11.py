text = input()
mass_text = text.split()
flag = True

for i in range(len(mass_text)-1):
    if mass_text[i][len(mass_text[i])-1] != mass_text[i+1][0]:
        if i%2==0:
            print("Петя")
            flag = False
            break
        else:
            print("Вася")
            flag = False
            break
if flag:
    if (len(mass_text)-1)%2 == 0:
        print("Петя")
    else:
        print("Вася")