from pydantic import BaseModel
# oydantic lienbry hoti hai jo data avlidtaion ceck etc ke liye use hiti hai usk aapn basemodel le rhe hai claass
# in future essi basmdel calss ko dyn me rkehte hue regefnec lekr aon
# structure if data baanyenge  incoming,outgoing data k valiafte ceck krnege
# ems ekuch filed option bhi hoti ai

# BaseModel is a class from the Pydantic library.

# Pydantic is a Python library for data validation and parsing.

# BaseModel is like a template for your data.

# 2️⃣ Why we use it

# To define the structure of data in Python (like what fields it has and their types).

# Automatically checks the types of your data (e.g., string, int, float).

# Can also provide default values, and make fields optional.

# Used a lot in APIs, especially FastAPI, to ensure incoming/outgoing data is correct.
from typing import Optional

# typing tool mes e ahmne optimal ko liye joki batata hai KeyboardInterruptcertian filed jsime ham optional use kr rhe hai model ke ander wo optionl hai ay to jo dts tyep 
# mention hai usme ho ya phr none nahi ho

# What it is

# Optional is a tool from Python’s typing module.

# It’s used to tell Python (and tools like Pydantic) that a value can be either a certain type OR None.


#ham jitne bhi mdole ya item anaygea ab basmeodl koas a temokare lekr hi abnayega to ye aoltacmmaticalyy cehck krlega validtaio etc
# bacsially ham basecmodle ko inehrit kr rhe hai
# datadatabse me sav ehone ke paihle basmeodle ek modles se hokr jyega agr koi bhi sisue aya hai toe oror show hogu
# We are creating a Pydantic model called ItemCreate.

# BaseModel = parent class from Pydantic that provides validation, type checking, and parsing.

# Why

# This model is used when creating a new item, e.g., via an API request.

# Ensures the data has the correct fields and types before saving to the database.

# How

# By inheriting from BaseModel, this class automatically gets features like:

# Data validation

# Default values

# Conversion (e.g., strings to floats if possible)

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
class ItemUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
#     Key difference from Create/Update models:

# ItemResponse → used for output (data going to the client).

# Includes id, which doesn’t exist in ItemCreate.

# All fields are typed, optional fields are handled automatically.
# jo as a resonse client ko data jats hai wo bhi validse hta hai paihle mdoel ka su ekrke 
class ItemResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
#pydantuc keal dicetnry ke sth wor krte ha pr yaha pr apn ko object ke th deal krne prt hai
# to te line ye batati ai ki pydnatic tum obejct ke st bhi deal kro
    class Config:
        orm_mode = True
