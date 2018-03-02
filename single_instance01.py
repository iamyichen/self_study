
class A:
    _instance=None
    def __init__(self):
        pass
        
    def __new__(cls): 
        if not cls._instance:
            cls._instance=super(A,cls).__new__(cls)
        return cls._instance
    
a=A()
b=A()
print(a)
print(b)