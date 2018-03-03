'''
实验表明，类属性在继承的过程中既不是深拷贝
也不是浅拷贝，而是子类属性对父类属性的引用，
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
B.x=2
print(A.x,B.x,C.x)
A.x=3
print(A.x,B.x,C.x)