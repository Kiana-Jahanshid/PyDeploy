import time 
import random 
import asyncio


async def get_file() :
    print("get file started ...")
    rand = random.randint(0,10)
    await asyncio.sleep(1)
    print(f"get file completed in {rand} seconds")

def extract_file() :
    print("extracting file started ...")
    rand = random.randint(0,10)
    time.sleep(1)
    print(f"extracting file completed in {rand} seconds")


async def download():
    print("download started ...")
    # order of running get and extract is important
    # so shouldnt run async , they should be sync
    # so we remove extract_file function async
    # so we remove << await >> before calling extract_file() in below lines :
    await get_file()
    extract_file()
    print(f"download completed ")

async def printer():
    print("printer started ...")
    rand = random.randint(0,10)
    await asyncio.sleep(1)
    print(f"printer completed in {rand} seconds")

# -----------------------------------------------------------
async def create_ai_video():
    print("create video started ...")
    rand = random.randint(0,10)
    await asyncio.sleep(1)
    print(f"video completed in {rand} seconds")

async def create_ai_audio():
    print("create audio started ...")
    rand = random.randint(0,10)
    await asyncio.sleep(1)
    print(f"audio completed in {rand} seconds")

def combine_video_and_audio():
    print("combining started ...")
    rand = random.randint(0,10)
    time.sleep(1)
    print(f"combining completed in {rand} seconds")

async def ai_job():
    print("ai started ...")
    rand = random.randint(0,10)
    # creating video & audio are independent , so run at the same time
    await asyncio.gather(create_ai_video() , create_ai_audio())
    # because combining have to wait until above line be finished , should use await before asyncio
    combine_video_and_audio()
    print(f"ai completed in {rand} seconds")

# --------------------------------------------------

async def main():
    await asyncio.gather(download() , printer() , ai_job())
    # for seeing blow line in terminal , should use await before previous line
    print("main ended")


if __name__ == "__main__" :
    start_time = time.perf_counter()
    asyncio.run(main())
    end_time = time.perf_counter()
    duration_of_main_function = end_time - start_time
    print(f"executed in {duration_of_main_function} seconds ")



