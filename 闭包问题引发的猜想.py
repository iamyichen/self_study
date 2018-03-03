'''
实验总结:
    1,2的实验结果为何不同？
    因为1中，inner中的j变量是通过参数传递
    的，而所有的报数传递都是对象的引用，
    所以在传参的那一刻起，j就指向了确定的对
    象;
    2中的inner中的i变量是对外部变量的i的直
    接访问，任意时刻，都随着外部i的改变而改
    变
    
    
'''

'''
#1
输出:[0,2,4,6]
def outer():
    tmp=[]
    for i in range(4):
        def inner(x,j=i):
            return x*j
        tmp.append(inner)
        print(inner)
    return tmp
'''

'''
#2
输出:[6,6,6,6]
def outer():
    tmp=[]
    for i in range(4):
        def inner(x):
            return x*i
        tmp.append(inner)
        print(inner)
    return tmp
      
a=outer()
print([a(2) for a in outer()])
'''    
        