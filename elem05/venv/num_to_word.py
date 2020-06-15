zero = ('ноль')

ones = {
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять'
}

tens = {
    0: 'десять',
    1: 'одиннадцать',
    2: 'двенадцать',
    3: 'тринадцать',
    4: 'четырнадцать',
    5: 'пятнадцать',
    6: 'шестнадцать',
    7: 'семнадцать',
    8: 'восемнадцать',
    9: 'девятнадцать'
}

dozens = {
    2: 'двадцать',
    3: 'тридцать',
    4: 'сорок',
    5: 'пятьдесят',
    6: 'шестьдесят',
    7: 'семьдесят',
    8: 'восемьдесят',
    9: 'девяносто'
}

hunderets = {
    1: 'сто',
    2: 'двести',
    3: 'триста',
    4: 'четыреста',
    5: 'пятьсот',
    6: 'шестьсот',
    7: 'семьсот',
    8: 'восемьсот',
    9: 'девятьсот'
}

class Converter(object):
    def __init__(self,number):
        self.number = number

    def nums_to_word(self):
        if self.number == 0:
            print(zero)

        elif self.number in range(1, 9):

            for i in ones:
                if i == self.number: print(ones[i])

        elif self.number in range(10, 19):

            for i in tens:
                if number - 10 == i: print(tens[i])

        elif self.number in range(20, 99):
            if self.number % 10 == 0:
                for i in dozens:
                    if self.number / 10 == i: print(dozens[i])
            else:
                print("This number is not in dictionary")

        elif self.number in range(100, 900):
            if self.number % 10 ** 2 == 0:

                for i in hunderets:
                    if self.number / 10 ** 2 == i: print(hunderets[i])

            else:
                print("This number is not in dictionary")
        else:
            print("This num is out of range")
        return dict

def main():
    while(True):
        value = int(input("Enter value:"))
        converter = Converter(value)
        converter.nums_to_word()
        continue_work = input("Do you want to continue?").lower()
        if continue_work != 'y': break
if __name__ == '__main__':
    main()