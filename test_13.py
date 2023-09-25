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