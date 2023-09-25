def number_bulls_cows(number,number_enter):
    bulls = 0
    cows = 0
    for i in range(4):
        if number[i]==number_enter[i]:
            bulls+=1
        elif number[i]!=number_enter[i] and number_enter in number:
            cows+=1
    return bulls, cows



number = input("Введите число: ")
print("\n"*25)

for i in range(10):
    number_enter = input()
    bulls, cows = number_bulls_cows(number,number_enter)
    print(f"Быков: {bulls} Коров: {cows}")
    if bulls == 4:
        print("Победа!")
        break
    elif i == 9:
        print("Проигрыш!")
