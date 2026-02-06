from sqlalchemy import Column, Integer, String, Float
#hsmne tools imrt kre hai sqlarchem se jo ki datasbe table banne me helo krneg like column,datatyoes
from database import Base
# es cde me ham tabe dfeine kr rhe hai table (class) tabhi bangea jb wo nase clas sko inheitr rkeghi joki hmne datbas emd efien dkiya ahi esliye imotkrn aor rha AttributeError

# 1️⃣ What it is

# declarative_base() is a function from SQLAlchemy.

# It creates a base class that all your database tables will inherit.

# Base = the parent class for all tables.

# 2️⃣ Why we use it

# SQLAlchemy needs a way to know which classes are tables.

# When you make a class like:

# class Item(Base):
#     ...

# 
# SQLAlchemy sees that Item inherits from Base → so it knows:

# “This is a table, I can create it in the database.”
# tep 1: What is Base?

# In SQLAlchemy, all database tables are Python classes.

# But SQLAlchemy needs to know which classes are tables.

# Base is a special parent class that tells SQLAlchemy:

# “Any class that inherits from me → treat it as a database table.”

# Example:

# class Item(Base):  # Item is now a table because it inherits Base
#     ...


# Without Base, SQLAlchemy won’t know Item is a table


class Item(Base):
    __tablename__ = "items" #table nam set kre ke liye use hita ahi


    id = Column(Integer, primary_key=True, index=True) #column banaya id namka or constsnt sue liye 
# SQLAlchemy uses it to find or update rows easily. primary_key=True
#   
#   index=True

# Creates a database index for this column.

# An index makes searching/filtering by id faster.
    name = Column(String, index=True)
    description = Column(String, nullable=True) #nullabl trye ka mtlb ye coumn emty bhi hiskta ahi
    price = Column(Float)















































# from pydantic import BaseModel
# from typing import Optional


# class ItemCreate(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float


# class ItemUpdate(BaseModel):
#     name: Optional[str]
#     description: Optional[str]
#     price: Optional[float]


# class ItemResponse(BaseModel):
#     id: int
#     name: str
#     description: Optional[str]
#     price: float

#     class Config:
#         orm_mode = True
