import asyncio
import time


async def func_1():
    print("one")

    await asyncio.sleep(1)
    # 1_
    #asyncio.create_task( func_2() )  # it wont wait to run fun_2 till the end , so 
    
    # 2_ if we wanted to run func2 & func3 together at the same time:
    #asyncio.gather(func_2() , func_3()) 
    # output= 1,4,2,6,5,3,7
    
    # 3_ if we use await :
    #await asyncio.gather(func_2() , func_3()) 
    # output= 1 ,  2,6,3,7  , 4,5
    

    print("four")
    await asyncio.sleep(1)
    print("five")


async def func_2():
    print("two")
    await asyncio.sleep(1)
    print("three")


async def func_3():
    print("six")
    await asyncio.sleep(1)
    print("seven") 

# asyncronous
# bc of << asyncio.create_task >> , numbers will be out of ordered
asyncio.run(func_1()) # one ,four ,  two , five , three  








# ********* نکــــته های مهــــــــــم **********

# 1_ put main() function in << asyncio.run() >>

# 2_ put (call) other < secondary > function like func_2 ,
# in <<< asyncio.create_task >>>

# 3_ or if you wana run multiple functions together use :
# << asyncio.gather( func2() , func3() , func4() , .... )  >>
# output order = 1,4,2,6,5,3,7


# عملیاتی که زمانبر نیست ، نیازی به استفاده از آسینک و اِوِیت هم ندارد 

# کارهای زمانبر بهتر است همزمان انجام شوند .  مثل قضیه آماده کردن همبرگر و صحبت کردن در حین انتظار برای آماده شدنش



'''
1_ we only can use << await >> before an << ASYNC >> function .

<< async >> def func_1() :
    ...

    
<< async >> def func_2()
    
    x = << await >> func_1(y)

---------------------------------------------------------

2_ << await >> only can be used in async function :

<< async >> def func_2(): دستور اِویت را فقط میتوان درون یک تابع آسینک استفاده کرد 
    print("two")
    await << asyncio >>.sleep(1) دستور اِویت را فقط برای یک دستور آسینک میتوان استفاده کرد 
    print("three")


'''