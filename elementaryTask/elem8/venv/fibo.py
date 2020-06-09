def main():
    print(fibo_mass())

def fibo_mass():
    min_value = int(input("Choose min value of Fibo-diapasone:"))
    max_value = int(input("Choose max value of Fibo-diapasone:"))
    fibo_arr = [0,1]
    fibo_res=[]
    sum_fibo=0
    for i in range(2,50):
        sum_fibo= fibo_arr[i-1]+fibo_arr[i-2]
        fibo_arr.append(sum_fibo)
        if (min_value<sum_fibo<=max_value): fibo_res.append(sum_fibo)
    return fibo_res

if __name__ == '__main__':
    main()

