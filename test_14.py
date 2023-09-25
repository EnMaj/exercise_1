'''
Задание 14.
В телевизионной игре "Поле чудес", игрок отгадывает слово. Напишите программу, которая спрашивает
у ведущего подсказку и загаданное слово. Далее, программа удаляет информацию с экрана, выполняя
вывод 25 пустых строк. После этого, выводится подсказка и слово, где вместо букв, выводятся
символы "*". Игрок должен с десяти попыток отгадать слово по буквам. После каждого хода выводится
слово, где неназванные буквы закрыты символом "*".  Отгаданные буквы выводятся на тех местах, где
они расположены. Каждый ход сопровождается вопросом "Буква или слово (0 - буква, 1 - слово)?".
В случае если слово отгадано верно, выводится сообщение "Победа!". Если слово названо неверно,
или закончились попытки, выводится сообщение "Проигрыш!".

Пример работы программы:
Ведущий вводит две строки: подсказку и загаданное слово.
Дикое животное.
тигр
Программа выводит 25 пустых строк и таким образом "скрывает" то, что написал ведущий.
Игрок пытается отгадать слово:
Дикое животное.
****
Буква или слово (0 - буква, 1 - слово)?0
a
****
Буква или слово (0 - буква, 1 - слово)?0
р
***р
Буква или слово (0 - буква, 1 - слово)?0
и
*и*р
Буква или слово (0 - буква, 1 - слово)?1
тигр
Победа!
'''


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