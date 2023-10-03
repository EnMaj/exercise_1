one_to_nineteen = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
decs = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
thousands = ['', 'одна тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи']


def one_transfer(integer):
        return one_to_nineteen[integer]

def two_transfer(integer, string):
        if integer in range(20):
                result = one_to_nineteen[integer]
        else:
                result = decs[int(string[0])]

                if string[1] != '0':
                        result = '%s %s' % (result, one_to_nineteen[int(string[1])])
        return result


def transfer(string):
        length = len(string)
        integer = int(string)
        if length == 1:
                result = one_transfer(integer)
        elif length == 2:
                result = two_transfer(integer, string)
        elif length == 3:
                result = hundreds[int(string[0])]
                ending = string[-2:]
                if ending != '00':
                        result = '%s %s' % (result, transfer(ending))

        elif length in range(4, 7):
                ending = transfer(string[-3:])
                str_starting = string[:-3]
                int_starting = int(str_starting)
                if int_starting in range(1, 5):
                        starting = thousands[int_starting]
                else:
                        starting = '%s тысяч' % (transfer(str_starting))

                result = '%s %s' % (starting, ending)
        elif length in range (7,10):
                ending = transfer(string[-6:])
                str_starting = string[:-6]
                int_starting = int(str_starting)
                if int_starting%10 in range(2,5):
                        starting = '%s миллиона' % (transfer(str_starting))
                elif int_starting%10 == 1 and int_starting%100!=11:
                        starting = '%s миллион' % (transfer(str_starting))
                else:
                        starting = '%s миллионов' % (transfer(str_starting))
                result = '%s %s' % (starting, ending)
        else:
                result = ''
        return result.strip()


number = input()
print(transfer(number))