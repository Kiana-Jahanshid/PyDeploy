from sqlalchemy import Column , Integer , String , Float ,  Boolean , ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Student(Base) :
    __tablename__ = "students"
    id = Column(Integer , primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    average = Column(Float)
    graduated = Column(Boolean)
    courses = relationship("Course" , back_populates="owner")



class Course(Base) :
    __tablename__ = "courses"
    id = Column(Integer)
    name = Column(String)
    unit = Column(Integer)
    owner_id = Column(Integer, ForeignKey("students.id"))
    owner = relationship("Student", back_populates="courses")
