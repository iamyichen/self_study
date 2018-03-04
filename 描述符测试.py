

class Field():
    def __init__(self,name):
        self.name=name
        print("Field init.")
        
    def __get__(self,instance,owner):
        print("Field get.")
        return self.name
        
    def __set__(self,instance,value):
        print("Field set.")
        self.name=value
        
    def __delete__(self,name):
        print("Field delete.")
        del self.name
        
class Person():
    t=Field("test")
    
#测试
print("*"*30)
p=Person()
print(type(p.t),p.t)
p.t="over"
print(type(p.t),p.t)
del p.t
print(Person.__dict__)