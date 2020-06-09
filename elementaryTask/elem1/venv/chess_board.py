def main():
    board()

def input_parametrs():
    height = input("Enter height of chess board: ")
    width = input("Enter height of chess board: ")
    if (height.isnumeric() and width.isnumeric()):
        '''print(f'Your height is {height}, your width is {width}')'''
        return height, width
    else:
        print("Enter a number: ")
        height = input("Enter height of chess board: ")
        width = input("Enter height of chess board: ")
        if (height.isnumeric() == False and width.isnumeric() == False): input_parametrs()
        return height,width

def board():
    height,width = input_parametrs()
    str1 = '*  '
    str2 = '  *'
    print(f'Your height is {height}, your width is {width}')
    for i in range(0, int(height)):
        if i %2 ==0: print(int(width)*str1)
        else: print(int(width)*str2)

if __name__ == '__main__':
    main()
