import time

def timer(func):
    def wrapper(*args,**kwargs):
        print("begin running:",func.__name__)
        t1=time.time()
        res=func(*args)
        t2=time.time()
        print("exit ",func.__name__,t2-t1)
        print(args)
        return res
    return wrapper

@timer
def a(x,y,step,*args,**kwargs):
    m,n=x,x+step
    while n<y:
        m,n=m+n,n+step
    return m

@timer
def b(x,y):
    t=0
    if x%2!=0:
        x+=1
    while x<y:
            t+=x
            x+=2
    return t

r1=a(2,100,2,type="连加")
r2=b(1,100)
print(r1,r2)