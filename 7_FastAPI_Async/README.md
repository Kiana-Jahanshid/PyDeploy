

+ ### useful link : [async](https://fastapi.tiangolo.com/async/)

# How to install :
```
pip install -r requirements.txt
```


# How to run :
```
python rhyme_finder.py
```

# Description :
### asyncio package  :

+ we only can use __await__ before a ASYNC an function .

+ __await__ only can be used in async functions .

+ (async def) functions have to be awaited .
```
<< async >> def func_1() :
    ...

    
<< async >> def func_2()
    
     x = << await >> func_1(y)
```

## Sync :
in sync , childs has to wait for their turn .
children will get married in order : 1 , 2, 3 , 4
child_1 married after 2 years
child_2 married after 8 years
child_3 married after 2 years
child_4 married after 1 years

total time will be sumation of all times : 
sum (2 , 8 , 2 , 1) = 
executed in 13.034747699974105 seconds



## Async :
in async  , childs don't need to wait at all . and they get marry when ever they want .
child_3 married after 0 years
child_2 married after 2 years
child_1 married after 7 years
child_4 married after 8 years

total time is equal to the max time of all children :
max( 0 , 2 ,  7 , 8 ) =
executed in 8.069982000044547 seconds


## conclusion : 

async functions runs faster than sync ones , bc async wont wait for running another function to run .
in async , functions run simultaneously at the same time .

![img](assets/sync_async.png)



