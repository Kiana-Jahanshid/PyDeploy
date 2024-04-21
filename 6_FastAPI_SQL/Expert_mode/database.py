from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql:///./university.db"
#SQLALCHEMY_DATABASE_URL  =  "postgresql://root:VNBfwH6bUSEcOi8PyWzi3LLb@university-db:5432/postgres"

#SQLALCHEMY_DATABASE_URL  =  "postgresql://root:VNBfwH6bUSEcOi8PyWzi3LLb@university-db:5432/postgres"
# Create the SQLAlchemy engine
Engine = create_engine(SQLALCHEMY_DATABASE_URL)
# Create a SessionLocal class
# Each instance of the SessionLocal class will be a database session. 
# The class itself is not a database session yet.
# But once we create an instance of the SessionLocal class, 
# this instance will be the actual database session.
SessionLocal = sessionmaker(autocmmit=False , autoflush=False , bind=Engine)
# Create a Base class
Base = declarative_base() # returns a class



