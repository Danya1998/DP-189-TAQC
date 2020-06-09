def main():
    attachments()
    cont = input("Do you want to continue: (enter 'y' or 'yes')")
    if (cont=='y' or cont=='yes'): attachments()
    else:
        exit(0)


def input_sizes():
    print("Input height and width of envelope num1: ")
    height1 = float(input("Enter a height:"))
    width1 = float(input("Enter a width:"))
    print(f"Envelop num#1:\n Heigth is {height1}, width is {width1}")
    print("Input height and width of envelope num2: ")
    height2 = float(input("Enter a height:"))
    width2 = float(input("Enter a width:"))
    print(f"Envelop num#2:\n Heigth is {height2}, width is {width2}")
    return height1,width1,height2,width2

def attachments():
    a,b,c,d = input_sizes()
    S1 = float(a)*float(b)
    S2= float(c)*float(d)
    if (S1<S2):
        print("You can envelope num#1 put in envelope num#2.")
    elif (S1>S2):
        print("You can envelope num#2 put in envelope num#1.")
    else:
        print("Your envelos are equal size.")

if __name__ == '__main__':
    main()