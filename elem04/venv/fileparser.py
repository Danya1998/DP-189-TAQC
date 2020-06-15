import  re

class StringFinder(object):
    count = 0
    def __init__(self,path_to_file,string):
        self.path_to_file = path_to_file
        self.string = string

    def __search_equal(self):
        with open(self.path_to_file, "r") as file:
            for line in file:
                if re.search(self.string,line): self.count += 1
        return self.count

    def print_result(self):
        return f"Result search: {self.__search_equal()}"

class StringChange(object):
    def __init__(self,path_to_file,string,new_string):
        self.path_to_file = path_to_file
        self.string = string
        self.new_string = new_string

    def __change_string(self):
        file_open = open(self.path_to_file).read()
        new_string = file_open.replace(self.string,self.new_string)
        file_write = open(self.path_to_file,'w')
        file_write.write(new_string)
        file_write.close()

    def print_result(self):
        self.__change_string()
        return f"Your file was succesfully changed"


def main():
    while(True):
        choose_mode = int(input("Choose mode:"))
        if choose_mode == 1:
            file = input("Enter your filename")
            string = input("Enter string which you search")
            string_finder = StringFinder(file,string)
            string_finder.print_result()
        elif choose_mode == 2:
            file = input("Enter your filename")
            string = input("Enter string which you search")
            new_string = input("Enter new string")
            string_changer = StringChange(file,string,new_string)
            string_changer.print_result()
        else: pass 
        continue_work = input("Do you want to continue?").lower()
        if continue_work != 'y': break
        
if __name__ == '__main__':
    main()