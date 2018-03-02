a=111
def fun(x,y):
    return x+y
    
def func(self,x,y):
    self.x=x
    self.y=y
    return x*y

test=type("Test",(object,),{"add":fun,"num":a,"mul":func})
print(test.add(12,23))
print(test.num)

b=test()
print(b.mul(11,22))
print(b.x,b.y,b.num)