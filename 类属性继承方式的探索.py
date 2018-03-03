'''
实验表明，类属性在继承的过程中既不是深拷贝
也不是浅拷贝，而是通过字典的方式传递的，当
访问累类的属性时，一次查找本类，父类。
因此，改变父类的属性会影响到子类，而改变子
类的属性不会影响到父类
'''
class A():
    x=1

class B(A):
    pass

class C(A):
    pass

print(A.x,B.x,C.x)
print(A.__dict__,B.__dict__,C.__dict__)
B.x=2
print(A.x,B.x,C.x)
print(A.__dict__,B.__dict__,C.__dict__)
A.x=3
print(A.x,B.x,C.x)
print(A.__dict__,B.__dict__,C.__dict__)
