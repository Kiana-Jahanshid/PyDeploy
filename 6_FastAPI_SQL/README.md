# FastAPI - SQL

# Description : [link](https://fastapi.tiangolo.com/tutorial/sql-databases/)
here , we used SQLAlchemy . so we can connect to different SQLs , without changing our code .
it means that , we can connect to sqlite and PostgreSQL with the same code .
here we want to connet FastAPI to SQL databases

# ORM (Object Relational Mapping):
its a tool that manage relation between objects (in class) and tables (in database) .
<img src= "assets/ORM.JPG" width=400px  />


# How to run :
+ ## Beginner mode : 
```
cd Beginner_mode
uvicorn main:app --reload
```
then open ``` http://127.0.0.1:8000/docs ``` in your browser and test all of it's methods .


+ ## Expert mode :

+ 1- docker pull postgres
+ 2_ test in local system : ``` uvicorn university:app --reload ```
make sure that API is connected to postgresql database .
+ 3- test in liara's posgresql database : 
enter postgresql database address in ```DATABASE_URL``` variable in university file . then check its connection . <br>
in liara : 
<br> first we create a [postgres database](https://console.liara.ir/databases/create) 

<br> then in 'نحوه اتصال' tab , it will give us a URL  , which is our ```DATABASE_URL``` :
``` 
SQLALCHEMY_DATABASE_URL  =  "postgresql://root:VNBfwH6bUSEcOi8PyWzi3LLb@university-db:5432/postgres"
```

then :
```
docker run -p 5432:5432 --name some-postgres -e POSTGRES_PASSWORD=33 -e POSTGRES_USER=kiki -e POSTGRES_DB=university -d postgres
```

now , our code will connect to liara's database .














+ how to download only a folder in a repository (not a whole repository) ?
https://download-directory.github.io/



