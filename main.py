"""text = input()
mass_text = text.split()
string = int(input())
new_text = ""
string_lenght = 0

for i in range(len(mass_text)):
    if len(mass_text[i])<=string-string_lenght:
        string_lenght+=len(mass_text[i])
        new_text = new_text + " " + mass_text[i]
    else:
        new_text = new_text + "\n" + mass_text[i]
        string_lenght = len(mass_text[i])

print(new_text)"""

def units(text):
    if text == 1:
        return "один "
    elif text == 2:
        return "два "
    elif text == 3:
        return "три "
    elif text == 4:
        return "четыре "
    elif text == 5:
        return "пять "
    elif text == 6:
        return "шесть "
    elif text == 7:
        return "семь "
    elif text == 8:
        return "восемь "
    elif text == 9:
        return "девять "

def from_ten_to_nineteen(text):
    if text == 10:
        return "десять"
    elif text == 11:
        return "одиннадцать"
    elif text == 12:
        return "двенадцать"
    elif text == 13:
        return "тринадцать"
    elif text == 14:
        return "четырнадцать"
    elif text == 15:
        return "пятнадцать"
    elif text == 16:
        return "шестнадцать"
    elif text == 17:
        return "семнадцать"
    elif text == 18:
        return "восемнадцать"
    elif text == 19:
        return "девятнадцать"

def tens(text):
    if text == 20:
        return "двадцать"
    elif text == 30:
        return "тридцать"
    elif text == 40:
        return "сорок"
    elif text == 50:
        return "пятьдесят"
    elif text == 60:
        return "шестьдесят"
    elif text == 70:
        return "семьдесят"
    elif text == 80:
        return "восемьдесят"
    elif text == 90:
        return "девяносто"


def numeral(number):
    position = 0
    mass=[]*4
    divider = 1000
    var = number
    rest = 0
    for i in range(4):
        rest = var//divider
        mass[i] = rest
        var = var - rest*divider
        divider /=10





number = input()


