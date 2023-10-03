one_to_nineteen = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
decs = ['', 'десять', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
thousands = ['', 'одна тысяча', 'две тысячи', 'три тысячи', 'четыре тысячи']


def _one_convert(integer):
        return one_to_nineteen[integer]

def _two_convert(integer, string):
        if integer in range(20):
                result = one_to_nineteen[integer]

        else:
                result = decs[int(string[0])]

                if string[1] != '0':
                        result = '%s %s' % (result, one_to_nineteen[int(string[1])])

        return result


def convert(string):
        length = len(string)
        integer = int(string)

        if length == 1:
                result = _one_convert(integer)

        elif length == 2:
                result = _two_convert(integer, string)

        elif length == 3:
                result = hundreds[int(string[0])]

                tail = string[-2:]

                if tail != '00':
                        result = '%s %s' % (result, convert(tail))

        elif length in range(4, 7):
                tail = convert(string[-3:])

                str_head = string[:-3]
                int_head = int(str_head)

                if int_head in range(1, 5):
                        head = thousands[int_head]

                else:
                        head = '%s тысяч' % (convert(str_head))

                result = '%s %s' % (head, tail)
        elif length in range (7,10):
                tail = convert(string[-6:])

                str_head = string[:-6]
                int_head = int(str_head)

                if int_head%10 in range(2,5):
                        head = '%s миллиона' % (convert(str_head))
                elif int_head%10 == 1 and int_head%100!=11:
                        head = '%s миллион' % (convert(str_head))
                else:
                        head = '%s миллионов' % (convert(str_head))
                result = '%s %s' % (head, tail)
        else:
                result = ''

        return result.strip()


number = input()
print(convert(number))