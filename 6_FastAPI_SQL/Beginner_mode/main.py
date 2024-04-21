'''
This code can works with all databases like sqlite or postgresql and ....

https://fastapi.tiangolo.com/tutorial/sql-databases
'''

from sqlalchemy import create_engine , Column , Integer , String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker , Session 
from fastapi import FastAPI , HTTPException , Depends


# we can use ANY kind of database here 
SQLALCHEMY_database_url = "sqlite:///./database.db"
# SQLALCHEMY_database_url = "postgresql://user:password@postgresserver/db" # for this we have to pull postgresql docker
# with using docker we dont need to know postgresql details . bc we use from its docker .
# pull docker postgres

# یکبار به صورت لوکال با استفاده از داکر پستگر
# و مطمعن میشیم ای پی آی به دیتابیس پستگر وصل شده 
# در مرحله بعد به دیتابیس پستگر لیارا وصلش میکنیم

# liara  = /apps ->  دیتابیس-> راه اندازی دیتابیس  -> postgres
# نحوه اتصال --> اتصال به دیتابیس با استفاده از url 
# این یوار ال رو کپی میکنیم و در خط ۱۵ بالا قرار میدییم

# create connection to database :
# Second parameter is only for sqlite : connect_args={"check_same_thread":False}
# so we dont write it for another databases  
# https://fastapi.tiangolo.com/tutorial/sql-databases/#note
# big databases like SQLserver / MySql /ORACEL / ... for resposing to lots of users requests at the same time ,
# using from threads in themselves .
# but sqlite , doesnt support threads  , bc its a tiny DB .
# so we set config_argument to False value , and make thread false .
# Engine is a connection to DB
# create ENGINE :
Engine = create_engine(SQLALCHEMY_database_url , connect_args={"check_same_thread":False}) # here we will use sqlite , so we should change it to False



# (in sqlite ) : after creating connection , then we create a cursor from that connection (in sqlite)
# (in sqlalchemy ) : we create a SESSION (like curser)
# we do all tasks using SESSION 
# autocommit=False : in sqlite we had to commit every changes(tasks) we made in database .
# autocommit= if we set it TRUE , it will commit automatically (like autosave)

# autoflush=False : تا زمانی که اطلاعات رو به سمت دیتابیس نفرستیم به اون سطر خاص آی دی تعلق نمیگیره
# اگر فرض کنیم فیلد آدی به طور خودکار آتواینکریمنت هست ، دیگه نیازی نیست ما این فیلد رو به دیتابیس بدیم
# و خودش به ترتیب مقدار آی دی رو اختصاص میده 
# difference between flush and commit :
'''
using flush : data store in DB , and an id allocated to that new task 
BUT Changes have not been saved yet ... 
by using COMMIT changes will be saved .

flush : allocate an id to each task . 

<<<<<<<<<<<<<<   flush +  save changes ==  COMMIT   >>>>>>>>>>>>>>>>>>>>

COMMIT HAS A FLUSH IN ITSELF ( flush() is always called as part of a call to commit())
'''
# bind=Engine :  Base (base class) which wants to create its tables , will 
# create its tables in <<<< Engine >>>>
# bind=Engine : means where to save changes in classes (in which database)
# WITH bind=Engine , WE ARE CONNECTING SQL DB TO THE Base class , to save data in tables 

# create SESSION :
Session_local = sessionmaker(autocommit=False , autoflush=False , bind=Engine)


# base is using for ORM and creating it's CLASSES 
# Base is a class that will use for INHERITANCE
# ALL CLASSES WILL BE INHERITED FROM Base Class
# Base is a CLASS ,  NOT an object
Base = declarative_base()


# create database models : (models are classes)
'''
CLASSES == TABLES 
number of classes == number of tables 
'''
class User(Base):
    __tablename__ = "users" #it's not accessible from outside the class
    # __tablename__ : its a private attribute (bc of 2 underline)
    # users = name of <<table>> must be polural and start with lowercase letter
    # User = name of a <<class>> must be start with capslock and should be singular
    # these are columns in 'users' table

    id = Column(Integer , primary_key=True) # id is an integer column 
    # primary_key=True : means id is our main key
    name =  Column(String) # name its a string column
    email = Column(String)# email is a string Column
    # Column  , Integer , String  , are classes 


# we  create our tables,  using this below line 
# Base will bind to above Engine
Base.metadata.create_all(bind=Engine)
# WHAT DOES OBOVE LILNE DO ?
# creating DB  : here If the database does not exist then it will be created by Base.metadata.create_all
# creating ttable of DB : "users" table will be created automatically by Base.metadata.create_all
# creating table fields : Base.metadata.create_all , will create above columns automaticallly

# table creation and config. has been finished

# from this part onwards its like previous codes
app = FastAPI()

def get_db():
    db = Session_local() # we are creating an object from 'Session_local' class
    yield  db     # if we use return we wont be able to close it in next line
    db.close() 


# summarized using yield 
@app.get("/users")
def read_user(user_id: int , db: Session= Depends(get_db)): # db says that im depended to get_db function , so it must be run

    # 1_ first we should create a DB from Session_local
    #db = Session_local() # creating an object from Session_local class
    user = db.query(User).filter(User.id == user_id).first()    # in user's table , return an id which is equal to user_id
    #db.close()    # at the end ,we should close the database which we created
    if user is None :
        raise HTTPException(status_code=404 , detail="user not found")
    return user



@app.post("/users")
def create_new_user(name: str, email :str  , db:Session=Depends(get_db)) : # id will be allocated by databse  

    # 1_ first create a DB 
    #db = Session_local()
    # 2_ create a user object 
    user = User(name=name , email=email)
    # 3_ add user to db 
    db.add(user)
    # 4_ commit 
    # bc at first lines we set 'autocommit=False' , so we have to commit here .
    db.commit() 
    db.refresh(user)# using 'refresh' will also return user id 
    #db.close()
    return user  # متغییر یوزر در اینجا فقط اسم و ایمیل داره و آی دی نداره 
    # یعنی  یوزر در خط ۱۳۶ قبل از اینکه بخواد کامیت بشه و آی دی بگیره 
    # متغییر یوزر مقداردهی شده و هنوز آی دی نگرفته بوده 
    # چون کامیت در خط ۱۴۱ انجام شده و آی دی گرفته
    # پس باید قبل از کلوز کردن دیتابیس دستور رفرش را بزاریم
    # اگر نمیخواستیم یوزر رو ریترن کنیم دیگه نیازی به رفرش نبود و کامیت کافی بود 

@app.put("/users/{user_id}/{field_name}/{field_value}")
def edit_user(user_id:int , field_name:str, field_value:str , db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None :
        raise HTTPException(status_code=404 , detail="user not found")
    if field_name == "email" :
        user.email = field_value
    elif field_name == "name" :
        user.name = field_value
    db.commit()
    db.refresh(user) 
    # if i didn't use refresh here , only changed field of user will be returned .
    # but now , all of 3 fileds (id,name,email) of that user will be returned .
    return user


@app.delete("/users/{user_id}")
def remove_user(user_id:int , db:Session=Depends(get_db)):
    
    # 1_ first find user in db 
    user = db.query(User).filter(User.id == user_id).first()
    # if user not found :
    if user is None :
        raise HTTPException(status_code=404 , detail="user not found")
    
    db.delete(user)
    # bc of changes (deletion) , we have to commit changes
    db.commit()
    # but we DONT CLOSE IT . bc it will be close in get_db function .
    return {"message" : "user deleted successfully"}




'''
Disadvantage of sqlite database :
1_ in sqlite we had to write query . 
2_ in case of using sqlite we had to change code completely if we wanted to change database .  


'''