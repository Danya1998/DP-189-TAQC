def main():
    set_num = int(input("Enter set value:"))
    count_el= int(input("Enter count of elements:"))
    if (set_num>=0 and count_el>=0): print(f"Elements is {finder_natural(set_num,count_el)}")
    else:
        print("Enter positive value")
        main()
    #print(f"Elements is {finder_natural(set_num,count_el)}")

def finder_natural(set_num,count_el):
    mass=[]
    natural = 1
    while pow(natural,2)<=int(set_num):
        natural+=1
    for i in range(0,count_el):
        mass.append(str(natural))
        natural+=1
    return ','.join(mass)

if __name__ == '__main__':
    main()