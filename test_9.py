text = input()
mass_text = text.split()

for i in range(len(mass_text)):
    for j in range (i+1, len(mass_text)):
        if mass_text[i]==mass_text[j]:
            print(mass_text[i])