# classes will become tables of database 

from typing import Optional
from sqlmodel import Field , Session , SQLModel , create_engine , select ,Relationship

# saving user information
# id , name , password , email
class User(SQLModel , table=True): # table= True means : create table from this class
# if a table is existed , there is no need to create it again 
    __table_args__ = {"extend_existing" : True}
    
    id : Optional[int] = Field(default=None , primary_key=True)
    name : str
    email : str 
    password : Optional[str]

    messages : list["Message"] = Relationship(back_populates="user")


#saving all messages (both user & chatbot)
# id , text , type , user_id
class Message(SQLModel , table=True):

    __table_args__ = {"extend_existing" : True}
    id : Optional[int] = Field(default=None , primary_key=True)
    text : str
    type : str 
    # one to many 
    user_id : int  = Field(default=None , foreign_key= "user.id")
    
    user : User = Relationship(back_populates="messages")



# ali = User()
# # show & access all ali's messages 
# ali.messages


# mess= Message()
# # access to message's user id 
# Message.user