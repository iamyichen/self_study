import time
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing.dummy import threading
#给线程池取一个别名ThreadPool
now=lambda :time.time()
lock=threading.RLock()
def run(x):
 lock.acquire()
 time.sleep(1)
 print(threading.current_thread().getName(),str(x))
 lock.release()
 return x,x

if __name__ == '__main__':
 testFL = [x for x in range(10)]
 
 start=now()
 pool = ThreadPool(5)#创建10个容量的线程池并发执行
 t=pool.map(run, testFL)
 end=now()
 print(type(t),t,str(end-start))
 
 start=now()
 t1=map(run,testFL)
 t2=list(t1)
 t3=tuple(t1)
 end=now()
 print(type(t1),t1,str(end-start))
 print(type(t2),t2,str(end-start))
 print(type(t3),t3,str(end-start))
 pool.close()
 pool.join()