
def run(n):
    l=[2]
    if n<2:
        raise StopIteration
    else:
        for i in l:
            if i>n:
                break
            yield i
        flag=False
        for next in range(3,n+1):
            for item in l:
                if not next%item:
                    flag=False
                    break
                else:
                    flag=True                  
            if flag:
                l.append(next)
                yield next
                
def judge(m):
    data=run(m)
    if m in data:
        return True
    else:
        return False

#测试代码
num=int(input("求出给定数n以内的质数:"))    
d=run(num)
for i in d:
    print(i)
    
while True:
    num=int(input("输入一个正整数，判断其是否为质数:"))
    if judge(num):
        print(num,"是一个质数！")
    else:
        print(num,"是一个合数！")