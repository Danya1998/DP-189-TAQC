from functools import wraps
import time

def timer(func):
    """Prints the runtime of the decorated function."""
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            value = func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f"Finished {func.__name__!r} in {run_time:.30f} secs")
        return value
    return wrapper_timer

def result_func(func):
    """Prints info about current state of decorated function, return true if parametrs given to function is valid\
     or return info about mistake"""
    @wraps(func)
    def wrapp_func(*args,**kwargs):
        try:
            result = f'{func(*args,**kwargs)}'
        except BaseException as e:
            result = f'info about exception: \n {e}'
        print(result)
    return wrapp_func

def sum(a,b):
    return a+b

@result_func
@timer
def main():
    a=float(input("Enter a value: "))
    b=float(input("Enter b value: "))
    print(sum(a,b))

if __name__ == '__main__':
    main()


