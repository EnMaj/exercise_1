text = input()
text_new = ""
last_space = len(text)
for i in range(len(text)-1,0,-1):
    if text[i] == " ":
        text_new= text_new + text[i+1:last_space] + " "
        last_space = i
text_new = text_new + text[0:last_space]
print(text_new)