import time

def timeslong(func):
    def call():
        start = time.clock()
        print("It's time starting ! ")
        print(func.__name__)
        print("It's time ending ! ")
        end = time.clock()
        return "It's used : %s ." % (end - start)
    return call
    
class MyTimer():
    def __init__(self,func):
        self.func=func
     
    def __call__(self):
        start = time.clock()
        print("It's time starting ! ")
        print(self.func.__name__)
        print("It's time ending ! ")
        end = time.clock()
        return "It's used : %s ." % (end - start)

@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y
    
@MyTimer    
def test():
    print("test() is called!")
    
f()
test()
