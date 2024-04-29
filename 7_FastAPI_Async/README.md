# Sync / Async 

+ useful link : [async](https://fastapi.tiangolo.com/async/)

## How to install :
```
pip install -r requirements.txt
```


## How to run :
```
python rhyme_finder.py
```

## Description :
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
children will get married in order : 1 , 2, 3 , 4 <br>
child_1 married after 2 years <br>
child_2 married after 8 years <br>
child_3 married after 2 years <br>
child_4 married after 1 years <br>

total time will be sumation of all times :  <br>
sum (2 , 8 , 2 , 1) =  <br>
executed in 13.034747699974105 seconds <br>



## Async :
in async  , childs don't need to wait at all . and they get marry when ever they want . <br>
child_3 married after 0 years<br>
child_2 married after 2 years<br>
child_1 married after 7 years<br>
child_4 married after 8 years<br>
<br>
total time is equal to the max time of all children :<br>
max( 0 , 2 ,  7 , 8 ) =<br>
executed in 8.069982000044547 seconds<br>


## conclusion : 

async functions runs faster than sync ones , bc async wont wait for running another function to run .<br>
in async , functions run simultaneously at the same time .

![img](assets/sync_async.png)



