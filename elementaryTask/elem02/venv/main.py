from venv.envelop import Envelope

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

def main():
    side_a,side_b,side_c,side_d = input_sizes()
    envelope1 = Envelope(side_a,side_b)
    envelope2 = Envelope(side_c,side_d)
    square1 = envelope1.square()
    square2 = envelope2.square()
    if (square1<square2):
        print("You can envelope num#1 put in envelope num#2.")
    elif (square1>square2):
        print("You can envelope num#2 put in envelope num#1.")
    else:
        print("Your envelos are equal size.")
if __name__ == '__main__':
    main()