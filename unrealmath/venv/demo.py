from unrealmath.addition import *
from unrealmath.substraction import *
import sys
import functools
import logging

def main():
    continue_work = 'y'
    while(continue_work == 'y'):
        '''Create object with package name'''
        logger = logging.getLogger('unrealmath')
        '''Format for writing in .log file'''
        formatter = logging.Formatter("%(asctime)s - %(message)s")
        '''Set level of logging'''
        logger.setLevel(logging.INFO)
        '''Set filter for each file in package'''
        addition_filter = logging.Filter('unrealmath.addition')
        substraction_filter = logging.Filter('unrealmath.substraction')
        '''Create handler of log file '''
        addition_handler = logging.FileHandler('addition.log')
        addition_handler.addFilter(addition_filter)
        addition_handler.setFormatter(formatter)

        substraction_handler = logging.FileHandler('substraction.log')
        substraction_handler.addFilter(substraction_filter)
        substraction_handler.setFormatter(formatter)
        '''Create handler for logger'''
        logger.addHandler(addition_handler)
        logger.addHandler(substraction_handler)
        add(8,9)
        substraction(6,2)
        continue_work = input("Do you want to continue?").lower()


if __name__ == '__main__':
    main()