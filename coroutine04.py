import asyncio
import random

async def fun(x,y):
    for i in range(20):
        print(str(i))
        await asyncio.sleep(random.uniform(0.2,0.3))
    return x+y

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    p=await fun(x,y)
    return p

async def print_sum(x, y):
    result = await compute(x, y)
    return ("%s + %s = %s" % (x, y, result))

async def main():
    task1=asyncio.ensure_future(print_sum(1,1))
    task2=asyncio.ensure_future(print_sum(1,2))
    task3=asyncio.ensure_future(print_sum(1,3))
    task4=asyncio.ensure_future(print_sum(1,4))
    task5=asyncio.ensure_future(print_sum(1,5))
    task6=asyncio.ensure_future(print_sum(1,6))
    task7=asyncio.ensure_future(print_sum(1,7))
    task8=asyncio.ensure_future(print_sum(1,8))
    task9=asyncio.ensure_future(print_sum(1,9))
    tasks=[task1,task2,task3,task4,task5,task6,task7,task8,task9]
    
    dones,pendings=await asyncio.wait(tasks)
    for task in dones:
        print("dones tasks:",task.result())

loop = asyncio.get_event_loop()        
loop.run_until_complete(main())
loop.close()