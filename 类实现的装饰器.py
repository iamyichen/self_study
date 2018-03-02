import time

class Timer():
    num=0
    def __init__(self,func):
        self.func=func
        self.now=lambda :time.time()

    def __call__(self,*args,**kwargs):
        start=self.now()
        res=self.func(*args,**kwargs)
        end=self.now()
        totals=end-start
        type(self).num+=1
        print("共耗时:",totals,"装饰器已调用次数:",type(self).num)
        return res
        
           
@Timer
def test():
    for i in range(10):
        print(i)
        time.sleep(0.2)
    return "over"
    
t=test()
t=test()
print("t:",t)