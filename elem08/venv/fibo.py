class FiboLength(object):
    fib1, fib2 = 0, 1
    fibo_result = []

    def __init__(self, length_el):
        self.length_el = length_el

    def __fibo_length(self):
        if self.length_el == 1:
            self.fibo_result.append(self.fib1)
            self.fibo_result.append(self.fib2)
        for elem in range(0, pow(10, self.length_el)):
            fib_sum = self.fib1 + self.fib2
            self.fib1 = self.fib2
            self.fib2 = fib_sum
            if len(str(self.fib2)) == self.length_el:
                self.fibo_result.append(self.fib2)
            elif len(str(self.fib2)) > self.length_el:
                break
            else:
                pass
        return self.fibo_result

    def print_res(self):
        return print(f'{self.__fibo_length()}')


class FiboRange(object):
    fibo_result = []
    fib1, fib2 = 0, 1

    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __fibo_range(self):
        if self.min_value == 0:
            self.fibo_result.append(self.fib1)
            self.fibo_result.append(self.fib2)
        for elem in range(self.min_value, self.max_value):
            fib_sum = self.fib1 + self.fib2
            self.fib1 = self.fib2
            self.fib2 = fib_sum
            if (self.min_value <= fib_sum <= self.max_value):
                self.fibo_result.append(self.fib2)
        return self.fibo_result

    def print_res(self):
        return print(f'{self.__fibo_range()}')


def main():
    choose_mode = int(input(f"Choose in which mode you want to search fibo sequence:\n"
                            "1 - in certain range\n"
                            "2 - length of elements\n"))
    if choose_mode == 1:
        len_el = int(input("Enter length of elem:"))
        fibolength = FiboLength(len_el)
        fibolength.print_res()
    else:
        min_value = int(input("Choose min value of Fibo-diapasone:"))
        max_value = int(input("Choose max value of Fibo-diapasone:"))
        fiborange = FiboRange(min_value, max_value)
        fiborange.print_res()


if __name__ == '__main__':
    main()
