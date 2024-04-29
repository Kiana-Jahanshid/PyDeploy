import time 
import random 
import asyncio


counter = 0

async def marriage(name):
    global counter
    rand = random.randint(0,10) 
    await asyncio.sleep(rand) 
    print(f"{name} married after {rand} years")
    counter +=1

async def main():
    # for each child , marriage function will be called
    for child in ["child_1" , "child_2" , "child_3" , "child_4"] :
       asyncio.create_task( marriage(child) )

    while counter < 4 :
        await asyncio.sleep(1)



if __name__ == "__main__" :

    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    duration_of_main_function = end_time - start_time
    print(f"executed in {duration_of_main_function} seconds ")