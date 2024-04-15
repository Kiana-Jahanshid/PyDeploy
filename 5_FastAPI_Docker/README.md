# FastAPI - Docker 

# Description :
here, we want to create docker image for FastAPI . bc there isnt any in 
[docker hub]("hub.docker.com") for FastAPI .

<br>

# How to install :
```
pip install -r requirements.txt
```

# How to run :
liara's docs :
```
https://fastapi-todo-app.liara.run/docs
```


## In postman :
+ Read database : (use __GET__ metod in postman)
```
https://fastapi-todo-app.liara.run/read_db
```
+ Add new task to database : ( use __POST__ method in postman)
```
https://fastapi-todo-app.liara.run/add_task/{id}/{title}/{description}/{time}/{status}
```

+ update or edit a task : (use __PUT__ in postman)
```
https://fastapi-todo-app.liara.run/update_task/{id}/{field_name}/{new_field_value}
```

+ delete a task : (use __DELETE__ in postman)
```
https://fastapi-todo-app.liara.run/delete_task/{id}
```

# _______________________________________________________

# GOAL 
## Create Docker for FastAPI :
here we want to run a FastAPI project in docker (not in our os ) or virtual machine . but we didn't find a vm for FastAPI (in ducker hub). SO we should create a docker for it .


--------------------------------
<br>

## [How to build a Docker image for FastAPI :](https://fastapi.tiangolo.com/deployment/docker/) (from scratch)

+ Create an app directory and enter it.
+ Create an empty file ```__init__.py```.
+ Create a ```main.py``` file .

+ create a file named __""Dockerfile""__ without any postfix .
+ paste below codes from [FastAPI website](https://fastapi.tiangolo.com/deployment/docker/) into Dockerfile ,
these are our docker layers :
```
FROM python
WORKDIR /code
COPY ./requirements.txt /code/requirements.tx
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```


```
.
├── app
│   └── main.py
├── Dockerfile
└── requirements.txt
```
+ # How to build a docker Image :

 
+ ### ``` docker build -t <docker-image>   .  ```

<br>


+ # start & run a docker container : <br>

+ ### ```docker run -d --name myname -p 80:80 <docker-image>```


# ___________________________________________________________________________
# Summary
### Create a docker for FastAPI :

+ ### 1_ pip install -r requirements.txt
+ ### 2_ docker pull python
+ ### 3_ docker build -t (docker-Image) 
+ ### 4_ docker run -d -p 80:80 (docker-Image)
+ ### 5_ check it using liara or http://127.0.0.1/ localhost 

# ___________________________________________________________________________
# ___________________________________________________________________________


# About Docker :

+ Docker can have many "Images" (like classes in oop). <br>
+ then , we can have some "CONTAINERS" from an "Image" (like class objects )

+ how to bring a docker (like hello-world docker)into our system :
in this [link](https://hub.docker.com/_/hello-world) you can use it's command : <br>
+ ### ```docker pull hello-world``` 

+ ### ```docker pull python```
then write : ```docker images```

NOW we have 2 IMAGEs . 

----------------------------------------------
<br>

## commands  : <br>

+ ## ```docker images``` :
shows all docker images which are pulled in terminal .
+ ## ```docker ps``` : 
shows list of only RUNNIG containers
+ ## ```docker ps -a``` : 
shows list of all containers (even exited ones)
<br>

----------------------------------------------------------
<br>
<br>




+ # How to create containers from IMAGE ?

## 1_ create a container :
+ # ```docker run <ImageName>```
after running an IMAGE , a container will be create automatically .for example :<br>
(a container form helllo-world Image)
```docker run hello-world```
until now , we have two images and one container .
if we run ```docker run hello-world``` again , therefore we will have TWO docker CONTAINERS (from hello-world image )
<br>

------------------------------------------

by runnig ```docker run python``` didn't anything happend . so we should add ```-it``` :  which means making command's run INTERACTIVE .
### ```docker run -it python bash ```

after runnig this command we enter to docker environment : <br>
``` root@7dcfdb670a76:/# ```
here it remains in docker and didnt exit from it & its status stay in runnig mode (docker container is running ).


<br>

-----------------------------
# how to delete docker container  ?
(dead) containers that are exited , Taking up the system space  . so we have to delete them : <br>

``` 
docker rm <NAMES> 
    or 
docker rm <CONTAINER ID>
```
for example : ``` docker rm tender_solomon ```

```
├── Image
│   └── Container ──> container-NAMES 
```
if we run ``` docker rm container-NAMES``` , we will face this error , bc docker container is running : 

``` 
cannot remove container "/container-NAMES": container is running : stop the container before removing .
```
so we have to stop it first :

## 1_ ```docker stop container-NAMES``` --> exited
## 2_ ```docker rm container-NAMES```



# ___________________________________________________
## make sure to delete all containers (Exited or running) :
## ``` docker ps -a ```

