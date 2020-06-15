class EasySearch(object):
    easy_way = []
    sum_to_half = 0
    sum_after_half = 0
    char_zero = "0"

    def __init__(self,number):
        self.number = number

    def search_easy_ticket(self):
        number = str(self.number)
        list_numbers = list(number)
        if len(list_numbers) % 2 == 0:
            for i in range(0, len(list_numbers) // 2):
                self.sum_to_half += int(list_numbers[i])
            for j in range(len(list_numbers) // 2, len(list_numbers)):
                self.sum_after_half += int(list_numbers[j])
            if self.sum_to_half == self.sum_after_half:
                if len(number) != 6:
                    number = f"{self.char_zero * (6 - len(number))}{number}"
                    return self.easy_way.append(number)

    def print_easy_list(self):
        return print(self.easy_way)

class DifficultSearch(object):
    difficult_way = []
    sum_even = 0
    sum_odd = 0
    char_zero = "0"

    def __init__(self,number):
        self.number = number

    def search_difficult_ticket(self):
        number = str(self.number)
        list_numbers = list(number)
        for i in range(0, len(list_numbers)):
            if int(list_numbers[i]) % 2 == 0:
                self.sum_even += int(list_numbers[i])
            else:
                self.sum_odd += int(list_numbers[i])
        if self.sum_odd == self.sum_even:
            if len(number) != 6:
                number = f"{self.char_zero * (6 - len(number))}{number}"
                return self.difficult_way.append(number)

    def print_difficult_way(self):
        return print(self.difficult_way)

class SearchTicket(EasySearch,DifficultSearch):
    def search_way(self):
        if len(EasySearch.easy_way) == len(DifficultSearch.difficult_way):
            print("Both ways have the same quantity of tickets")
        elif len(EasySearch.easy_way) > len(DifficultSearch.difficult_way):
            print("Easy way is win")
            for i in range(0, len(EasySearch.easy_way)):
                print(f"№ of ticket: {EasySearch.easy_way[i]}")
        else:
            print("Difficult way is win")
            for i in range(0, len(DifficultSearch.difficult_way)):
                print(f"№ of ticket: {DifficultSearch.difficult_way[i]}")

def main():
    print("-------Program which find lucky numbers-------")
    min = int(input("Enter a min number:"))
    max = int(input("Enter a max number:"))
    for i in range(min, max):

        easy_search = EasySearch(i)
        easy_search.search_easy_ticket()
        difficult_search = DifficultSearch(i)
        difficult_search.search_difficult_ticket()

    search_ticket = SearchTicket(i)
    search_ticket.search_way()

if __name__ == '__main__':
    main()

