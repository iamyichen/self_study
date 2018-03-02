import queue
import threading
import time

values_totals = 100
q_max = 20
in_max = 3
out_max = 5
id_num = 0
in_time = 0.5
out_time = 0.5
in_full_time = 1
out_empty_time = 1
threads_in_full_time = 1
threads_out_full_time = 1
values = (x for x in range(values_totals))
semaphore1 = threading.Semaphore(in_max)
semaphore2 = threading.Semaphore(out_max)
q = queue.Queue(q_max)


def qin():
    global id_num
    max = 30
    print(threading.currentThread().getName() + " is running!")
    if semaphore1.acquire():
        while max > 0:
            if not q.full():
                try:
                    data = next(values)
                    id_num += 1
                except StopIteration as error:
                    print(error)
                    break
                q.put(data)
                print("{0[4]}:{0[5]} member{1} in!".format(time.localtime(time.time()), data))
                max -= 1
                time.sleep(in_time)
            else:
                time.sleep(in_full_time)
        semaphore1.release()
    else:
        semaphore1.release()
        time.sleep(threads_in_full_time)
    print(threading.current_thread().getName() + "is dead!")


def qout():
    max = 30
    print(threading.current_thread().getName() + "is running!")
    if semaphore2.acquire():
        while max > 0:
            if not q.empty():
                print("{0[4]}:{0[5]} member{1} out!".format(time.localtime(time.time()), q.get()))
                max -= 1
                time.sleep(out_time)
            else:
                time.sleep(out_empty_time)
                if not q.empty():
                    pass
                else:
                    break
        semaphore2.release()
    else:
        semaphore2.release()
        time.sleep(threads_out_full_time)
    print(threading.current_thread().getName() + "is dead!")


def main():
    while id_num < values_totals:
        print("active threads counts:", str(threading.activeCount()))
        print("active threads list:", str(threading.enumerate()))
        t = threading.Thread(target=qin)
        t.start()
        time.sleep(2)
        t = threading.Thread(target=qout)
        t.start()
    print("main thread is dead!")


if __name__ == '__main__':
    main()
