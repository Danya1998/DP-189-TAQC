import os,sys
import functools
from  constant import *
from contextlib import contextmanager
from datetime import datetime

path_to_program = "quiz/"

def result_func(func):
    @functools.wraps(func)
    def wrapp_func(*args,**kwargs):
        try:
            result = f'{func(*args,**kwargs)}'
        except BaseException as e:
            result = f'Info about exception: \n {e.__traceback__}'
        print(result)
    return wrapp_func

@contextmanager
def write_answers():
    try:
        user_answer = open('answers.txt', 'w')
        yield user_answer
    except OSError:
        print("We had an error!")
    finally:
        print('Closing file')
        user_answer.close()

@contextmanager
def write_time():
    try:
        time = open('timer.txt', 'w')
        yield time
    except OSError:
        print("We had an error!")
    finally:
        print('Closing file')
        time.close()


def play(file,user_answers,time):
    with file:
        start = datetime.now()
        for line in file:
                string= line.rstrip()
                print(string)
                b = input("")
                user_answers.write(f"{string} {b} \n")
        end = datetime.now()
        time.write(f"{file}:{timer(start,end)} \n")
    return user_answers, time

def read_file(filename:str):
    try:
        file = open(filename,'r')
        print(f"Your file {filename} is succesfully opened")
        return file
    except IOError:
        print("No file")

def timer(start_section,end_section):
    return end_section-start_section

'''@result_func'''
def main():
    with write_answers() as user_answers, write_time() as time:
        continue_game = 'y'
        while(continue_game == 'y'):
            list_files = [i for i in os.walk(path_to_program)] [0][2] ###
            print(list_files)
            filename = input("Enter your quiz file name: ")
            file = read_file(f"{path_to_program}{filename}")
            play(file,user_answers,time)
            continue_game = input("Do you want to continue?").lower()

if __name__ == '__main__':
    main()