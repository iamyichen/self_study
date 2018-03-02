from queue import LifoQueue as Queue

def getQueue(var):
    for key in globals().keys():
        if key==var.lower():
            return eval(key)

def hannuota(n,A,B,C):
    global index
    
    if n==1:
        move(index,A,C)
        index+=1
    else:
        hannuota(n-1,A,C,B)
        move(index,A,C)
        index+=1
        hannuota(n-1,B,A,C)
    
def move(n,X,Y):
    d=getQueue(X).get()
    getQueue(Y).put(d)
    print("第{}步:移动{}号盘{}-->{}".format(n,d,X,Y))

n=int(input("请输入汉诺塔的盘子个数："))
steps=2**n-1
index=1
print("完成游戏共需{}步。".format(steps))
a=Queue(n)
for i in range(n,0,-1):
    a.put(i)
b=Queue(n)
c=Queue(n)

hannuota(n,"A","B","C")