def singleton(cls):  
        instances = {}  
        def getinstance():  
            if cls not in instances:  
                instances[cls] = cls()  
            return instances[cls]  
        return getinstance  
     
@singleton  
class A:
    def __init__(self):
        pass

a=A()
b=A()
print(a,b)