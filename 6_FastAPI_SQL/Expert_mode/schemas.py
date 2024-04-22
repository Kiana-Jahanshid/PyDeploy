from pydantic import BaseModel , ConfigDict
'''
Create initial Pydantic models / schemas :

Notice that SQLAlchemy models define attributes using =, and pass the type as a parameter to Column, like in:
name = Column(String)
while Pydantic models declare the types using :, the new type annotation syntax/type hints:
name: str


before creating an item, we don't know what will be the ID assigned to it, 
but when reading it (when returning it from the API) we will already know its ID.

when reading a student, we can now declare that courses will contain the items that belong to this student.
'''


class CourseBase(BaseModel): #schema
    name: str
    unit: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase): # Pydantic models (schemas) that will be used when reading data, when returning it from the API.
    id: int
    owner_id: int
    # class Config: # internal Config class : is used to provide configurations to Pydantic
    #     orm_mode = True  # will tell the Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).
'''
Notice it's assigning a value with = , like:
orm_mode = True
It doesn't use : as for the type declarations before.
This is setting a config value, not declaring a type.
------------------------------------------------------

This way, instead of only trying to get the id value from a dict, as in:
id = data["id"]

it will also try to get it from an attribute, as in:
id = data.id


'''


class StudentBase(BaseModel): # schema
    firstname: str
    lastname: str
    average: float
    graduated :bool

class StudentCreate(StudentBase): # variables in this class won't be sent from the API when reading a user. and  won't be in other Pydantic models , like password that we may dont want to be returned .
    pass 

class Student(StudentBase): # Pydantic models (schemas) that will be used when reading data, when returning it from the API.
    id: int
    courses: list[Course] = []

    # class Config:
    #     orm_mode = True