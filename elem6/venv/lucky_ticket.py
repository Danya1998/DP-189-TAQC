def easy_search(number):
    char_zero = "0"
    sum_to_half = 0
    sum_after_half = 0
    number = str(number)
    list_numbers = list(number)
    if len(list_numbers)%2 == 0:
        for i in range(0, len(list_numbers)//2):
            sum_to_half+=int(list_numbers[i])
        for j in range(len(list_numbers)//2,len(list_numbers)):
            sum_after_half+=int(list_numbers[j])
        if sum_to_half == sum_after_half:
            if len(number) != 6:
                number = f"{char_zero*(6-len(number))}{number}"
                return number

def difficult_search(number):
    char_zero = "0"
    sum_even = 0
    sum_odd = 0
    number = str(number)
    list_numbers = list(number)
    for i in range(0,len(list_numbers)):
        if int(list_numbers[i])%2 == 0: sum_even+= int(list_numbers[i])
        else: sum_odd+=int(list_numbers[i])
    if sum_odd == sum_even:
        if len(number) != 6:
            number = f"{char_zero * (6 - len(number))}{number}"
            return number

def main():
    easy_way = []
    diff_way = []
    print("-------Program which find lucky numbers-------")
    min = int(input("Enter a min number:"))
    max = int(input("Enter a max number:"))
    for i in range(min,max):
        lucky_number = easy_search(i)
        if lucky_number: easy_way.append(lucky_number)
        difficult_number = difficult_search(i)
        if difficult_number: diff_way.append(difficult_number)
    if len(easy_way) == len(diff_way):
        print("Both ways have the same quantity of tickets")
    elif len(easy_way) > len(diff_way):
        print("Easy way is win")
        for i in range(0,len(easy_way)):
            print(f"№ of ticket: {easy_way[i]}")
    else:
        print("Difficult way is win")
        for i in range(0, len(diff_way)):
            print(f"№ of ticket: {diff_way[i]}")


if __name__ == '__main__':
    main()