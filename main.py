# from fastapi import Depends
# from auth import hash_password, verify_password, create_access_token, get_current_user
# from schemas import UserCreate, UserLogin, UserResponse
# from models import User
# from fastapi.security import OAuth2PasswordRequestForm
# from fastapi import FastAPI

# app = FastAPI()
# from database import Base, engine
# # Create all database tables
# Base.metadata.create_all(bind=engine)

# from fastapi import FastAPI, Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session

# from auth import hash_password, verify_password, create_access_token, get_current_user
# from schemas import UserCreate, UserLogin, UserResponse
# from models import User
# from database import get_db

# app = FastAPI()












# 1)fastapi se hi api bnate hai fastapi se fastapi class lete hai uska object ya instance banat ehai usme hi opertaionkrte hai like route spefic me spefic func run ho ye sb 
#2) depends ka mtlb  user get me hmesh aham user ka token==token joki horna cahahiye se cimapr eni kr skte kyuki token private chij hai TimeoutErrorham nek func banate hai usme foken rteurn krte hai or jb jb compare krna hota hai depend(tokenfunc) se cmaore kr lete hai
# ese apn apne token ke code ko reuse as well safe rkh skate hia
# 3)httpsexcat[tion ye class got hai jb exception show hota hai tb ky show kre mtln kbhi agr user ni hai to exception shwo kro user niot und us time ye use hota hai]
# raise HTTPException(status_code=400, detail="Bad request")
# 4)manulaly nuebr yad krha ki 404 mtln not found o bhi muskul hai to sttsus ek trh ki libbry hoti hai to store rkheti hai konse number se konsa error arise hoag to manualky
# sttsus_code ==404 krne s ebtetr hai status use krna 
# raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad request")









from fastapi import FastAPI, Depends, HTTPException, status



# 1)OAuth2PasswordRequestForm classhoti hai fatsapi me automatic userne jo login passowrd dla hai usse reda krne ke liye hoi hI
# Depends() tells FastAPI: “Use OAuth2PasswordRequestForm to read login data”
# OAuth2PasswordRequestForm helps FastAPI automatically read the username and password when a user logs in.

from fastapi.security import OAuth2PasswordRequestForm



# 1)Session = Database se baat karne ka tool jisse hum data read, write, update, delete karte hain.
# sqlarcahemy - linrry hoti hai dbs e baat krne ke liye python us ekrta hai
# orm -baiscally object rletainal manager ptthon obje ko databse table ya vise versa tarsnalt map krne ke liye us ehota hai
# python me ham sql quiry likhkr ni chal skte badheg akma
# to ye baiscally python me hi hm qutry likhte hai inetrnalky wo sql wury me change ho jata hai with help of or
# from sqlalchemy.orm import Session

# def get_users(db: Session):
#     return db.query(User).all() 
# jaise app banate the ftsapi se or uskei help s espn route or sb banate the wias ehi
# session ki help se ham db banate hai or the usme sbhiopertiaonkrte hai queires related python lnauangue em

from sqlalchemy.orm import Session
# modles file se user class ko import kiya hai jisse kbhi situation aye ki table ka data read upadte write krna ai to nee dhogi table ki
# user is table
# #
from models import User       # <-- IMPORT MODEL FIRST
# from database import Base, engine, get_db means:
# database.py file se table-banane ka class (Base), database connection (engine), aur database session (get_db) ko import kar rahe ho.
from database import Base, engine, get_db 
# auth file se ham hash_passowrd,verify passwrd,craete access login ,get crrent user func ko imporr kr rhe hai 
# in hash passowrd in case of
# hash apssowrd -paaaord ko dircelt save nakkr ehashed form me convert krta hai then save krta hai sb me
# verify passowrd - chcek krta hai jo user ne pasword enter kiya wo hash apssowrd jo db me store hai suke barabaer hai ya nahi 
# if sb sahi hai mtlbn mtln passorwd match kr gya veirfy apssowrd me to hri access  token generate krke dedeta hai
# get cuurnet suer mtlb current user ko acces token dedeta hai tkne verify krke token dedte ahai curnet suer ko
from auth import hash_password, verify_password, create_access_token, get_current_user
# validraon ke liye use hota hai pydantic modle em ki jo bhi data server se ara hao ya user send kr rha hai uska spefic format hoga validtaion check ki trh
# ni shai format m e hua to eoror ayega woi scheme me defiend hI
# AS A respons emodle dfeien dhota hai sbhi get,pupost login signup memoryview
from schemas import UserCreate, UserLogin, UserResponse

# Create all database tables (AFTER models are imported)
# Ye line models ko dekh kar database me tables banati hai.
# ham modle me bs table ka format dfeiend krte hai pr  table formed ho +data jye usme eksi helps e hota hai automaiac
# Jitne tables Base ke metadata me hai, un sabko iss database (engine) me create kar do.”
# bas emtlb jisko rfeer krke ham table banate hai
# metadata me bhut sari tale format defin hota hai
# create all mtln jitne bhi table meta datab me hai ,base ka refer lekr banado
# bind engine rka mtlb respetuc jis database s econnect kr eho sume bana doBase.metadata.create_all(bind=engine)
# route oprtion sb kuch app object ke baisi pr bhi hota hai joki fatsapi ko rer krk banta hai
# “Mera FastAPI application bana do aur ise app naam ke variable me rakh do.”
app = FastAPI()
# . data: UserCreate
# ✔ WHAT

# data = user ke body se jo data aa raha hai
# UserCreate = schema (validate karta hai)

@app.post("/register", response_model=UserResponse)
def register_user(data: UserCreate, db: Session = Depends(get_db)):
    # check duplicate
    user_exists = db.query(User).filter(User.username == data.username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already exists")
# 🟧 8. hashed = hash_password(data.password)
# ✔ WHAT

# User ka password encrypt (hash) kar raha hai.
    hashed = hash_password(data.password)
    new_user = User(username=data.username, email=data.email, password=hashed)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
# User username + password deta hai → (data)

# Database me check hota hai → (db.query)

# Agar match → user ko entry pass (token) milta hai

# User future API me token dikha kar access leta hai

@app.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}




# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session

# import models
# import schemas
# from database import engine, SessionLocal


# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/items/", response_model=schemas.ItemResponse)
# def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     db_item = models.Item(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# @app.get("/items/{item_id}", response_model=schemas.ItemResponse)
# def get_item(item_id: int, db: Session = Depends(get_db)):
#     item = db.query(models.Item).filter(models.Item.id == item_id).first()
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")

#     db_item.name = item.name
#     db_item.description = item.description
#     db_item.price = item.price
#     db.commit()
#     return db_item


# @app.patch("/items/{item_id}")
# def patch_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
#     db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")

#     for key, value in item.dict(exclude_unset=True).items():
#         setattr(db_item, key, value)

#     db.commit()
#     return db_item


# @app.delete("/items/{item_id}")
# def delete_item(item_id: int, db: Session = Depends(get_db)):
#     db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")

#     db.delete(db_item)
#     db.commit()
#     return {"message": "Item deleted"}
# When Python runs your .py files, it compiles them into bytecode (a faster format).
# These compiled files are saved inside a folder named:

# __pycache__/


# 🟩 2. Depends
# ✅ WHAT

# Depends FastAPI ka dependency injection tool hai.

# Dependency injection = function ko automatically kuch cheeze provide karna.
from fastapi import FastAPI, Depends, HTTPException
# fastapi se fatspai class lete ahi suse object abnate hai usske bad usme hi sbhi route ke acc konsa 
# end pint work krega func define krte hai ye auto matic route se content leleta hai acc tp schmeas smjhakr 
# depends ka Ek function ka output automatically 
# doosre function me pass karna.from fastapi import FastAPI, Depends, HTTPException
# 👉 Kya hai?

# HTTPException ek class hai jo proper HTTP error response bhejti hai.

# 👉 Kyun use hoti hai?

# Jab data na mile

# Jab invalid request aaye

# Jab unauthorized access hofrom sqlalchemy.orm import Session
# status cod ek use krti hai agr sttsus vode kuch spefic hai to ye msg show krdo
# kyuki intenrla sevre rerro jo most of situ me aajta ArithmeticErrorusse better erro ke acc ststus cod eaye or uske aacc 
# main screen me msg show ho sue rko
# porduction me
# 👉 Kyun zaroori hai?

# Database connection reuse karne ke liye

# Authentication check

# Common logic likhne ke liye
# Depends common cheez inject karta ha
db: Session = Depends(get_db)

from sqlalchemy.orm import Session
# orm=sqlcarme ka wo pat jo nrml ovject ko db table row mr cnevyr kra ahai ya db ko python objec ki trh use krne ka trieka
# sqlalchemy me jo db conection ka logic jsi class ki help se likhai hai wo class
# session hai sqlalcemy vakge hai orm module
import models #import models ka matlab hai: database ke tables
# (models.py) ko use karna,jo bhi chije format structure define hau ahi table ka models.py file me usse import krke as a module use kr rhe hai jisse
# . lagakr usme rhen wale table func varible sbko use kr ske dircet
import schemas

# schemas.py hota kya hai?

# schemas.py FastAPI project ka wo file hota hai jisme hum Pydantic models define karte hain:

# ✔ Request data validation ke liye
# ✔ Response format define karne ke liye
# ✔ API me kaunsa field aayega, kaunsa nahi
# ✔ User se aane wale JSON ko check karne ke liye
# import schemas
# enginer fatsapi d ke mid ke conection ul ko mage krtaai
# ou can get a database connection by doing:

# db = SessionLocal()


# A session = a temporary connection to read/write data.
from database import engine, SessionLocal
# enginer sqlarcemy ka object hota hai conection maage krne me helo krta hai ksi typ ke daatabse dse connect rk rhe hai mondodb sqlie s esme hota ahi
#databse me session naname ka trka hota hai jsise crud oeprtion kr ske ye sssionlocal ek function hota hai jsise ham sesision object baante ahi in firie
# ror phi crud operyion ye s manage krte hai 
# db = SessionLocal()
# SessionLocal = function (factory) 
# jo har request ke liye naya database session banata hai.
# 👉 Session = Database se baat karne wala connection object
# database.py file se woh 2 cheeze import karo jo database 
# connection manage karti hain — engine aur SessionLocal.”

# 2. What is engine?
# 🔹 Simple definition:

# engine = database se connection banane wali machine

# SQLAlchemy engine tells:

# Which database to use (SQLite, MySQL, etc.)

# How to connect to it

# Example (inside database.py):

# engine = create_engine("sqlite:///./test.db")


# This line says:

# "SQLite database test.db se connect karne ke liye ek engine banao."

# 🔥 Why do we need engine?

# To create the database tables:

# models.Base.metadata.create_all(bind=engine)


# Without engine, tables cannot be created
# models.Base.metadata.create_all(bind=engine)
 #app object hai fastapi class ki uski help e hi endpoint route middleware or sb kuch 
#  fucntinayng pefroma krte hai
# app = FastAPI()



# Route function ko database tak access lane ke liye ek DB session ki zaroorat hoti hai.
# Har API request ke liye ek fresh session diya jata hai, jisse safe, isolated aur thread-safe DB operations ho sake.
# Session na ho to koi bhi CRUD operation possible nahi hai
# Ye function ek new DB session banata hai, route ko deta hai, aur kaam khatam hote hi session close kar deta hai.
# def get_db():
#     db = SessionLocal() #//db namke varibelmes sesiion store kiya
#     try:
#         yield db #allow kiya ki kahi bhi db mtln sesison ko es function ke bahar mtlb route me sue kr skte hai kyuki
#         # dircet route ke baisisc pr func run ni hora inetrmideratu sesiion ki need hogi
#         # har bar jb jb reuqets krnega user kisi chij ki tb 
#     finally:
#         db.close() 
#         # //har sessio  ka req cmplte ya oitput ane ke bad clsoe hona jjruri hai to 
#         # finally hamehs work kreg

# @app.post("/items/", response_model=schemas.ItemResponse)
# def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     db_item = models.Item(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item

# @app.get("/items/{item_id}", response_model=schemas.ItemResponse)
# def get_item(item_id: int, db: Session = Depends(get_db)):
#     item = db.query(models.Item).filter(models.Item.id == item_id).first()
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")

#     db_item.name = item.name
#     db_item.description = item.description
#     db_item.price = item.price
#     db.commit()
#     return db_item

# # item.dict(exclude_unset=True)
# # 👉 exclude_unset=True ka matlab:

# # Jo fields user NEHI bhejta, unko ignore karo.
# @app.patch("/items/{item_id}")
# def patch_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
#     db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")

#     for key, value in item.dict(exclude_unset=True).items():
#         setattr(db_item, key, value)

#     db.commit()
#     return db_item


# @app.delete("/items/{item_id}")
# def delete_item(item_id: int, db: Session = Depends(get_db)):
#     db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
#     if not db_item:
#         raise HTTPException(status_code=404, detail="Item not found")

#     db.delete(db_item)
#     db.commit()
#     return {"message": "Item deleted"}
# w

# SessionLocal returns a fresh session each time.

# Example:

# db = SessionLocal()
# now db can make queries
# get_db() creates a new database session and gives it to your API route using yield.
# After the route finishes, FastAPI automatically closes the session using
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------- JWT PROTECTED ROUTES ---------------------------- #
# Receives item data

# Checks user is logged in

# Creates a database object

# Saves it

# Returns final item
@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)   # <-- Added
):
#     ➡️ User ne jo data bheja, usko dictionary banao
# ➡️ Fir us dictionary ko Item model ke andar bhar do
# ➡️ Aur ek naya Item object create ho jayega
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def get_item(
    item_id: int,
    db: Session = Depends(get_db),
#     HOW

# FastAPI:

# Token dekhta hai

# Token verify karta hai

# Agar sahi → current user deta hai

# Agar galat → 401 Unauthorized
    current_user: models.User = Depends(get_current_user)   # <-- Added
):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# @app.get("/")
# def home():
#     return {"message": "yuhu!!,Welcome to the API!"}
@app.api_route("/", methods=["GET", "HEAD"])
def home():
    return {"message": "yuhu!!,Welcome to the API!"}

@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: schemas.ItemCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)   # <-- Added
):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item.name
    db_item.description = item.description
    db_item.price = item.price
    db.commit()
    return db_item


@app.patch("/items/{item_id}")
def patch_item(
    item_id: int,
    item: schemas.ItemUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)   # <-- Added
):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
# Ye loop automatically db_item ki har updated field ko assign karta hai, bina manually likhe (db_item.name = ...)
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)

    db.commit()
    return db_item


@app.delete("/items/{item_id}")
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)   # <-- Added
):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted"}
