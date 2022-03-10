def doubler (func):
    def inner(*args, **kw):
        func(*args, **kw)
        func(*args, **kw)
        return None
    return inner

@doubler
def myFunc4():
    print("Myfunc4 is called")

myFunc4()