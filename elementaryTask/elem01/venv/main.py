from venv.chessboard import Chessboard
def main():
    height = int(input("Please enter a diserable height: "))
    width = int(input("Please enter a diserable width: "))
    chessboard = Chessboard(height,width)
    show = chessboard.print_board()
        

if __name__ == '__main__':
    main()