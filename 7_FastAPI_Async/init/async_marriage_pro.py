import time 
import random 
import asyncio


async def marriage(name):

    rand = random.randint(0,10) 
    await asyncio.sleep(rand) 
    print(f"{name} married after {rand} years")


async def main():
    # it will run all 4 function together 
    # await : Waits until all functions execution are finished
    await asyncio.gather(marriage("child_1")  , marriage("child_2") , marriage("child_3") , marriage("child_4"))


    # for child in ["child_1" , "child_2" , "child_3" , "child_4"] :
    #    asyncio.create_task( marriage(child) )


if __name__ == "__main__" :
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    duration_of_main_function = end_time - start_time
    print(f"executed in {duration_of_main_function} seconds ")