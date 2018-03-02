import asyncio
import time

async def fun(n):
    print("start pause:",str(n),"s.")
    await asyncio.sleep(n)
    print("stop pause.")
    return str(n)    

async def main():
    l=(x for x in range(1,7,2))
    tasks=[]
    for i in l:
        task=asyncio.ensure_future(fun(i))
        tasks.append(task) 
    print(asyncio.Task.all_tasks())  
    results=await asyncio.gather(*tasks)
    print(asyncio.Task.all_tasks())
    return results

now=lambda :time.time()
loop=asyncio.new_event_loop()
t1=now()
results=loop.run_until_complete(main())
for result in results:
    print(result)
t2=now()
print("{:.2f}".format(t2-t1))