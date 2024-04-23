# FastAPI - SQL

# Description : [link](https://fastapi.tiangolo.com/tutorial/sql-databases/)
here , we used SQLAlchemy . so we can connect to different SQLs , without changing our code .
it means that , we can connect to sqlite and PostgreSQL with the same code .
here we want to connet FastAPI to SQL databases

# ORM (Object Relational Mapping):
its a tool that manage relation between objects (in class) and tables (in database) . <br>

<img src= "assets/ORM.JPG" width=400px  />


# How to run :
+ ## Beginner mode : 
```
cd Beginner_mode
uvicorn main:app --reload
```
then open ``` http://127.0.0.1:8000/docs ``` in your browser and test all of it's methods .


+ ## Expert mode :
you only need to enter this url in your browser :<br>
```
https://fastapi-todo-app.liara.run/docs
```

# ---------------------------

## step by step Explanation :
## test in localhost (postgresql):
+ 1- docker pull postgres
+ 2- write this url in ```database``` file : 
```
SQLALCHEMY_DATABASE_URL = "postgresql://username:pass@localhost:5432/db-name"
```
+ 3- 
```
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=pass -e POSTGRES_USER=username -e POSTGRES_DB=db-name -d postgres 
 ```

+ 4_ run this command : ``` uvicorn Expert_mode.main:app --reload ```

+ 5- open ``` http://127.0.0.1:8000/docs ``` url to test methods.


## test in liara : 
+ 1- first we create a [postgres database](https://console.liara.ir/databases/create) 

+ 2- then in 'نحوه اتصال' tab , it will give us a URL  , which is our ```DATABASE_URL``` value :
``` 
SQLALCHEMY_DATABASE_URL  =  "postgresql://root:VNBfwH6bUSEcOi8PyWzi3LLb@university-db:5432/postgres"
```

we will paste it in ``` database.py ``` file .

+ 3- run in lara :
```
npx liara login
npx liara deploy --> enter port 80 

then open this link :
https://fastapi-todo-app.liara.run/docs

```







