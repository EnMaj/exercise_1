'''
Задание 13.
Дима часто пользуется общественным транспортом и всегда проверяет номер билета,
является ли он "счастливым". Счастливым считается билет, имеющий в номере четное
количество цифр. Причем,  сумма цифр первой половины номера равна сумме цифр
второй половины.  Программа на вход получает  последовательность номеров билетов.
Ввод номеров должен завершить тогда, когда будет введен "счастливый" билет.
Программа должна вывести его порядковый номер. Счет начинается с 1.
'''
def summ_numbers(ticket):
    summ = 0
    for i in range(len(ticket)):
        summ+=int(ticket[i])
    return summ


i = 0
flag = False
while flag == False:
    i+=1
    ticket = input()
    len_ticket = len(ticket)
    if len_ticket%2==0:
        if summ_numbers(ticket[0:(len_ticket//2)]) == summ_numbers(ticket[len_ticket//2:len_ticket]):
            print(i)
            flag = True