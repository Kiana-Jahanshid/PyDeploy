import asyncio
import time


async def func_1():
    print("one")
    await asyncio.sleep(1)
    await func_2() # it will wait until func_2 finishes
    await asyncio.sleep(1)
    print("four")
    await asyncio.sleep(1)
    print("five")


async def func_2():
    print("two")
    await asyncio.sleep(1)
    print("three")


# syncronous
# bc of << await >>  , numbers will be ordered
asyncio.run(func_1()) # 1,2,3,4,5

