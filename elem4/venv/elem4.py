import re

def count_need_line(path, string):
    with open(path, 'r') as file:
        count_line = 0
        for line in file:
            if (re.search(string,line)): count_line +=1
        return count_line

def change_line(path, string, new_string):
    s = open(path).read()
    s = s.replace(string, new_string)
    f = open(path, 'w')
    f.write(s)
    f.close()

def main():
    while(True):
        choose_mode = int(input("Which mode do you want to choose (1 or 2):"))
        if (choose_mode == 1):
            filename = input("Enter name of your file:")
            string = input("Enter string which you search:")
            print(count_need_line(filename,string))

        elif choose_mode==2:
            filename = input("Enter name of your file:")
            string = input("Enter string which you search:")
            new_string = input("Enter new string:")
            change_line(filename,string,new_string)
        else: pass
        continue_work = input("Do you want to continue:").lower()
        if(continue_work != 'y'): break

            
if __name__ == '__main__':
    main()