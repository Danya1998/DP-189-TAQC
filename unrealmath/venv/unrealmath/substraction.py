import random
import logging
import os
__log = logging.getLogger(__name__)

def substraction(minuend, subtrahend):
    print(__log)
    __log.info("Start function substraction()")
    __log.info(f"Give parametrs to the function: {minuend}, {subtrahend}")
    result = float(minuend) - float(subtrahend) + random.randint(1,10)
    __log.info(f"Result of function add: {result}")
    __log.info("End function substraction()")
    return result

