'''
Задание 8.
Дано предложение. Напечатать все его слова в порядке неубывания их длин.
'''

text = input()
mass_text = []
last_space = len(text)
for i in range(len(text)-1,0,-1):
    if text[i] == " ":
        mass_text.append(text[i+1:last_space])
        last_space = i
mass_text.append(text[0:last_space])
text_new = " ".join(sorted(mass_text,key=len))
print(text_new)
