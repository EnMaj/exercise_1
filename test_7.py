text = input()
min_word = float("inf")
last_space = len(text)
for i in range(len(text)-1,0,-1):
    if text[i] == " ":
        min_word = min(min_word,len(text[i+1:last_space]))
        last_space = i
min_word = min(min_word,len(text[0:last_space]))
print(min_word)
