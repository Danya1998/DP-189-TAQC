import math


def fibo_length(len_el):
    fib1, fib2 = 0, 1
    fibo_result = []
    if len_el == 1:
        fibo_result.append(fib1)
        fibo_result.append(fib2)
    for elem in range(0, pow(10, len_el)):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        if len(str(fib2)) == len_el:
            fibo_result.append(fib2)
        elif len(str(fib2)) > len_el:
            break
        else:
            pass
    return fibo_result


def fibo_range(min_value, max_value):
    fibo_result = []
    fib1, fib2 = 0, 1
    if min_value == 0:
        fibo_result.append(fib1)
        fibo_result.append(fib2)
    for elem in range(min_value, max_value):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        if (min_value <= fib_sum <= max_value):
            fibo_result.append(fib2)
    return fibo_result


def main():
    choose_mode = int(input(f"Choose in which mode you want to search fibo sequence:\n"
                            "1 - in certain range\n"
                            "2 - length of elements\n"))
    if choose_mode == 1:
        min_value = int(input("Choose min value of Fibo-diapasone:"))
        max_value = int(input("Choose max value of Fibo-diapasone:"))
        print(fibo_range(min_value, max_value))
    else:
        len_el = int(input("Enter length of elem:"))
        print(fibo_length(len_el))


if __name__ == '__main__':
    main()
