class MyType(type):

    def __new__(cls, name, bases, attrs):
        print("000000000000")
        cs=super().__new__(cls, name, bases, attrs)
        print(cs,name)
        print(attrs)
        return cs

    def __init__(self,name,bases,attrs):
        print("111111111111")
        print(self,name)
        super().__init__(name,bases,attrs)
        print(attrs)

    def __call__(self,*args,**kwargs):
        print("222222222222")
        print(self)
        obj=self.__new__(self,*args,**kwargs)
        print(obj)
        self.__init__(obj,*args,**kwargs)
        return obj

class Foo(metaclass=MyType):

    def __new__(cls,*args,**kwargs):
        print("3333333333333")
        obj=super().__new__(cls)
        print(obj)
        return obj
    
    def __init__(self,name):
        print("4444444444444")
        self._name=name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name=name

f=Foo("xiaoming")
print(f)
print(f.name)
f.name="xiaoqiang"
print(f.name)