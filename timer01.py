import time

now=lambda :time.time()

def timer(func):
    def wrapper(*args,**kwargs):
        start=now()
        print(func.__name__,"will be running.")
        res=func(*args,**kwargs)
        print(func.__name__,"is over!")
        end=now()
        t=end-start
        print("totals:",t)
        return res
    return wrapper

@timer
def fun():
    print("in the fun().")
    a="@@@@@@@@@@"
    print(a)
    print("fun() will be returned!")
    return a
    
def test():
    print("test() is running!")
    return "test()"

a=fun()
b=timer(test)
c=b()
print(b)
print(c)
print(vars())