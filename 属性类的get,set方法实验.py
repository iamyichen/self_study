'''
1,只有类的类属性的操作才会触发属性类的__get__,
__set__方法，而实例的类属性则不能。
2,类的类属性的属性操作不能触发__get__,
__set__
'''

class A():
    def __init__(self):
        print("A init...")
        
    def __get__(self,instance,owner):
        print("A get:",self,instance,owner)
        return self
        
    def __set__(self,instance,value):
        print("A set:",self,instance,value)
        
    def __getattr__(self,name):
        print("A getattr.")
        #return super().__getattr__(name)
        
    def __setattr__(self,name,value):
        print("A setattr.")
        super().__setattr__(name,value)

    def __getattribute__(self,name):
        print("A getattribute.")
        return super().__getattribute__(name)
        
    def __setattribute__(self,name):
        print("A setattribute.")
        super().__setattribute__(name)

class B():
    y=A()
    def __init__(self):
        self.x=A()

#测试类属性
print("*"*30)
b=B()
print("b.y:",b.y)
b.y=A()
print("b.y:",b.y)
print("*"*30)

#测试实例属性
print("*"*30)
print("b.x:",b.x)
b.x=A()
print("b.x:",b.x)
print("*"*30)

#测试属性类的取值，赋值
print("*"*30)
b.x.age=18
print(b.x.age)
print("*"*30)
b.y.age=38
print(b.y.age)