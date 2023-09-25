def star_replacement(word_new,word,word_enter):
    for i in range(len(word)):
        if word_enter.upper() == word[i].upper():
            word_new = word_new[:i] + word_enter + word_new[(i+1):]
    return word_new

help = input("Введите подсказку: ")
word = input("Введите слово: ")
print("\n"*25)
word_new = len(word)*"*"
print(help)
for i in range(10):
    choice = int(input("Буква или слово (0 - буква, 1 - слово)? "))
    word_enter = input()
    if choice == 1 and word_enter.upper() == word.upper():
        print("Победа!")
        break
    elif choice == 1 and word_enter.upper() != word.upper():
        print("Проигрыш!")
        break
    if word_enter.upper() in word.upper():
        word_new = star_replacement(word_new,word,word_enter[0])
        print(word_new)
        if word_new.upper() == word.upper():
            print("Победа!")
            break
    elif i == 9:
        print("Проигрыш!")