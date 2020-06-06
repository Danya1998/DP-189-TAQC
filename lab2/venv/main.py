import re
from contextlib import contextmanager
from typing import Tuple, Generator, TextIO

@contextmanager
def file_open() ->Generator:
    """Function decorator which opens file for reading"""
    try:
        filename = input("Enter the name of the file:")
        file_open = open(filename, 'r')
        yield file_open
    except OSError:
        print("We had an error!")
    finally:
        file_open.close()

def counter(filename:str) ->Tuple[int,int,int,int,int]:
    '''Funcion which counts symbols according to given condition'''
    with file_open()  as filename:
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
    filename = file_open()
    res = counter(filename)
    print("Total lines:", res[0])
    print("Empty lines:", res[1])
    print("Lines with z:", res[2])
    print("Z count:", res[3])
    print("Lines with and:", res[4])

if __name__ == '__main__':
    main()