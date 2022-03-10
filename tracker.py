

def func_counter(func):
    def inner(*args, **kw):
        result = func()
        inner.counter += 1
        print(f'Total of time called: {inner.counter}')
        return result
    inner.counter = 0
    return inner

@func_counter
def myFunc5():
    print("Myfunc5 is called")

myFunc5()
myFunc5()
myFunc5()

print(myFunc5.counter)