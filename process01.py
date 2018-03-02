from multiprocessing import Process
import time

def fun(values):
    for v in values:
        print(v)
        time.sleep(0.2)
        

touple=(x for x in range(100))
p1=Process(target=fun,args=(touple,))
p1.start()
p2=Process(target=fun,args=(touple,))
p2.start()