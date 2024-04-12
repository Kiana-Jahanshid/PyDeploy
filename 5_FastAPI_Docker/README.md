# FastAPI - Docker 


## Docker :

+ Docker can have many "Images" (like classes in oop). <br>
+ then , we can have some "CONTAINERS" from an "Image" (like class objects )

## example :

+ how to bring a docker (like hello-world docker)into our system :
in this [link](https://hub.docker.com/_/hello-world) you can copy it's command and paste it in terminal : <br>
### 1_ ```docker pull hello-world``` 
<br>
then write : <br>

```docker images```
<br>
NOW we have ONE IMAGE : <br>
```
REPOSITORY     TAG        IMAGE ID         CREATED        SIZE 
python         latest     6cbe1053f244    2 weeks ago     1.02GB
hello-world    latest     d2c94e258dcb    11 months ago   13.3kB 
```

### 2_ ```docker pull python```
### 3_ ```docker pull tensorflow/tensorflow```
### 4_ ```docker pull pytorch/pytorch```
----------------------------------------------
<br>

## terminal commands  : <br>

+ # ```docker images``` :
shows all docker images which are pulled in terminal .
+ # ```docker ps``` : 
shows list of only RUNNIG containers
<br>

+ # ```docker ps -a``` : 
shows list of all containers (even exited ones)
<br>
----------------------------------------------------------

# [How to build a Docker image for FastAPI :](https://fastapi.tiangolo.com/deployment/docker/) (from scratch)

+ Create an app directory and enter it.
+ Create an empty file ```__init__.py```.
+ Create a ```main.py``` file with:


+ # How to create containers from IMAGE ?

## 1_ create a container :
+ # ```docker run <ImageName>```
after running an IMAGE , a container will be create automatically .<br>
for example :<br>
(a container form helllo-world Image)
```docker run hello-world```
(from hello-world image , a container built )
until now , we have two images .
and one container .
if we run ```docker run hello-world``` again , therefore we will have TWO docker CONTAINERS (from hello-world image )
+ containers :
![img](assets/containers.JPG)
<br>

+ Images :
![img](assets/images.JPG)

------------------------------------------

by runnig this command ```docker run python``` didnt anything happend . <br>
so we should add ```-it``` :
### ```docker run -it python bash ```
<br>

-it : means making command's run INTERACTIVE .

+ after runnig this command we enter to docker environment ! : <br>
``` root@7dcfdb670a76:/# ```
+ here it remains in docker and didnt exit from it & its status stay in runnig mode . ``` root@7dcfdb670a76:/# ```
+ here , docker container is running .
+ if we type ```docker ps -a``` in None docker terminal , we will have : <br>
```
CONTAINER ID   IMAGE         COMMAND     CREATED          STATUS                      PORTS     NAMES
7dcfdb670a76   python        "bash"      3 minutes ago    Up 3 minutes                          relaxed_keller
c4ab3c35e3ab   python        "python3"   22 minutes ago   Exited (0) 22 minutes ago             eloquent_booth
a7a127fbf36b   hello-world   "/hello"    54 minutes ago   Exited (0) 54 minutes ago             affectionate_rhodes
545876914cbc   hello-world   "/hello"    10 hours ago     Exited (0) 10 hours ago               tender_solomon 
``` 


<br>

-----------------------------
# How to delete a docker  : 
(dead) containers that are exited , Taking up the system space  .
so we have to delete them : <br>

``` 
docker rm <NAMES> 
 
    or 

docker rm <CONTAINER ID>
```
for example : ``` docker rm tender_solomon ```


# _______________________________________________________

# GOAL 
## Create Docker for FastAPI :
here we want to run a FastAPI project in docker (not in our os ) or virtual machine . but we didnt find a vm for FastAPI (in ducker hub). SO we should create a docker for it


--------------------------------
<br>

## 1_ create a file named __""Dockerfile""__ without any postfix .
## 2_ paste below codes from [FastAPI website](https://fastapi.tiangolo.com/deployment/docker/) into Dockerfile :
these are our docker layers :
```
# 
FROM python

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```
<br>

```
.
├── app
│   └── main.py
│
├── Dockerfile
└── requirements.txt

```
# 3_ Now , build a docker  , so run this command :
```
docker build -t <desired_name> . 
```
like ``` docker build -t kiki . ```

now we have 3 Images . 
```
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
kiki          latest    342c9791cd4d   49 seconds ago   1.04GB
python        latest    6cbe1053f244   2 weeks ago      1.02GB
hello-world   latest    d2c94e258dcb   11 months ago    13.3kB
``` 

the SIZE of new image is equal to = python SIZE + hello-world SIZE

+ now we should run a container from new Image .
so : <br>

```
docker run -d --name myname -p 80:80 kiki
```
output :  1d780c52539f5a0efa9f6fd89f324fc1c5d32d3e07d347f913120b219473e7a7 
<br>

+ type ``` docker ps ``` ,  then we can see it's running :
```
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                NAMES
1d780c52539f   kiki      "uvicorn app.main:ap…"   2 minutes ago   Up 2 minutes   0.0.0.0:80->80/tcp   modest_curie
7dcfdb670a76   python    "bash"                   2 hours ago     Up 2 hours                          relaxed_keller
```

therefore , because it's running  , we can use it .<br>

```
http://127.0.0.1/items/5?q=somequery 
```
and check it . 
```
http://127.0.0.1/docs
```


# how to delete docker container that has built from kiki's Image  ?
```
├── kiki's Image
│   └── Container ──> modest_curie 
```
### if we run ``` docker rm modest_curie``` , we will face this error , bc docker container is running : 

``` 
cannot remove container "/modest_curie": container is running : stop the container before removing .
```
<br>

## 1_ ```docker stop modest_curie``` --> exited
## 2_ ```docker rm modest_curie```

# _______________________________________
## how to delete python's docker container ?
### 1_ ``` docker stop relaxed_keller```
### 2_ ``` docker rm relaxed_keller ```



# _________________________________________
## make sure to delete all containers (Exited or running)
### ``` docker ps -a ```
now all of the 3 Images are Unused .






# ترتیب انجام دستورات برای اجرای تودولیست

## 1_ docker pull python
<!-- ## docker pull nouchka/sqlite3
## docker run -it nouchka/sqlite3 -->
## 2_ docker build -t todo .
## 3_ docker run -d -p 80:80 todo






