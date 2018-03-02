# _*_ coding: utf-8 _*_

"""
python_thread_multiprocee.py by xianhu
"""

import time
import threading
import multiprocessing as mp
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool

# 定义全局变量Queue
g_queue = mp.Queue()
g_search_list = list(range(10000))


# 定义一个IO密集型任务：利用time.sleep()
def task_io(task_id):
    print("IOTask[%s] start" % task_id)
    while not g_queue.empty():
        time.sleep(1)
        try:
            data = g_queue.get(block=True, timeout=1)
            print("IOTask[%s] get data: %s" % (task_id, data))
        except Exception as excep:
            print("IOTask[%s] error: %s" % (task_id, str(excep)))
    print("IOTask[%s] end" % task_id)
    return


# 定义一个计算密集型任务：利用一些复杂加减乘除、列表查找等
def task_cpu(task_id):
    print("CPUTask[%s] start" % task_id)
    while not g_queue.empty():
        count = 0
        for i in range(10000):
            count += pow(3*2, 3*2) if i in g_search_list else 0
        try:
            data = g_queue.get(block=True, timeout=1)
            print("CPUTask[%s] get data: %s" % (task_id, data))
        except Exception as excep:
            print("CPUTask[%s] error: %s" % (task_id, str(excep)))
    print("CPUTask[%s] end" % task_id)
    return task_id


def init_queue():
    print("init g_queue start")
    while not g_queue.empty():
        g_queue.get()
    for _index in range(10):
        g_queue.put(_index)
    print("init g_queue end")
    return
    
def process(task):
    init_queue()
    time_0 = time.time()
    num=mp.cpu_count()
    pool=ProcessPool(num)
    pool.map(task,range(num))
    print("结束：", time.time() - time_0, "\n")
    
def thread(task):
    init_queue()
    time_0 = time.time()
    num=mp.cpu_count()
    pool=ThreadPool(num)
    pool.map(task,range(num))
    print("结束：", time.time() - time_0, "\n")
    
def commn(task):
    init_queue()
    time_0 = time.time()
    task(0)
    print("结束：", time.time() - time_0, "\n")
    
if __name__ == '__main__':
    print("cpu count:", mp.cpu_count(), "\n")

    print("========== 直接执行IO密集型任务 ==========")
    commn(task_io)

    print("========== 多线程执行IO密集型任务 ==========")
    thread(task_io)

    print("========== 多进程执行IO密集型任务 ==========")
    process(task_io)
    
    print("========== 直接执行CPU密集型任务 ==========")
    commn(task_cpu)

    print("========== 多线程执行CPU密集型任务 ==========")
    thread(task_cpu)

    print("========== 多进程执行cpu密集型任务 ==========")
    process(task_cpu)

    exit()
