class Chessboard():
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def print_board(self):
        print("i tut")
        for i in range(0, self.height):
            if i %2 ==0: print(int(self.width)*'*  ')
            else: print(int(self.width)*'  *')
        