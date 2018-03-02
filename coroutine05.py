
import asyncio
 
import time
 
now = lambda: time.time()
 
async def do_some_work(x):
    print('Waiting: ', x)
 
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)
 
async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)
    print("type of coroutine1:",type(coroutine1))
 
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]
 
    main_coroutine=asyncio.wait(tasks)
    dones, pendings = await main_coroutine
    print("type of main_coroutine:",type(main_coroutine))
 
    for task in dones:
        print('done Task result: ', task.result())
        
 
start = now()
 
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
 
print('TIME: ', now() - start)