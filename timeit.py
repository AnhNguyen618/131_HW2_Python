import time

def calculate_time(func):
    def inner(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        stop = time.time()
        print(f'Total time {int((stop - start))}')
        return result
    return inner

@calculate_time
def myFunc3():
    for i in range (int(10e7)):
        pass

myFunc3()