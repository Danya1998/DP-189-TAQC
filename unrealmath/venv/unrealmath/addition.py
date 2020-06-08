import random
import logging

__log = logging.getLogger(__name__)
print(__log)

def add(first, second):
    __log.info("Start function add()")
    result = float(first) + float(second) - random.randint(1,10)
    __log.info(f"Result of function add: {result}")
    print("Enter integer value")
    __log.info("End function add()")
    return result
