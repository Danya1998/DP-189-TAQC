class FindNatural(object):
    natural = 1
    natural_number = []
    def __init__(self,set_number,count_elements):
        self.set_number = set_number
        self.count_elements = count_elements

    def __search_number(self):
        while pow(self.natural, 2) <= int(self.set_number):
            self.natural += 1
        for i in range(0, self.count_elements):
            self.natural_number.append(str(self.natural))
            self.natural += 1
        return ','.join(self.natural_number)

    def print_result(self):
        return print(f"Elements is {self.__search_number()}")

def main():
    set_number = int(input("Enter set value:"))
    count_elements = int(input("Enter count of elements:"))
    find_natural = FindNatural(set_number,count_elements)
    find_natural.print_result()

if __name__ == '__main__':
    main()