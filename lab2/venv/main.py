import re
import os.path
from typing import Tuple


def counter(filename:str) ->Tuple[int,int,int,int,int]:
    '''Funcion which counts needed symbols according to given condition'''
    lines = 0
    empty_str = 0
    line_z=0
    letter_z=0
    line_and=0
    for line in filename:
        lines += 1
        if (line == "\n" or line == "\r\n"): empty_str += 1
        if re.search('z',line): line_z+=1
        letter_z+=line.count('z')
        if re.search('and',line): line_and +=1
    return lines,empty_str,line_z,letter_z,line_and

def main() -> None:
    while(True):
        filename = input("Enter the name of the file:")
        check_file = os.path.exists(filename)
        if check_file:
            file_open = open(filename, 'r')
            break
        else:
            print("We had an error!")
    result = counter(file_open)
    print("Total lines:", result[0])
    print("Empty lines:", result[1])
    print("Lines with z:", result[2])
    print("Z count:", result[3])
    print("Lines with and:", result[4])
    file_open.close()


if __name__ == '__main__':
    main()