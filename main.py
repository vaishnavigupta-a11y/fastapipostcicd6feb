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
app = FastAPI()



# Route function ko database tak access lane ke liye ek DB session ki zaroorat hoti hai.
# Har API request ke liye ek fresh session diya jata hai, jisse safe, isolated aur thread-safe DB operations ho sake.
# Session na ho to koi bhi CRUD operation possible nahi hai
# Ye function ek new DB session banata hai, route ko deta hai, aur kaam khatam hote hi session close kar deta hai.
def get_db():
    db = SessionLocal() #//db namke varibelmes sesiion store kiya
    try:
        yield db #allow kiya ki kahi bhi db mtln sesison ko es function ke bahar mtlb route me sue kr skte hai kyuki
        # dircet route ke baisisc pr func run ni hora inetrmideratu sesiion ki need hogi
        # har bar jb jb reuqets krnega user kisi chij ki tb 
    finally:
        db.close() 
        # //har sessio  ka req cmplte ya oitput ane ke bad clsoe hona jjruri hai to 
        # finally hamehs work kreg

@app.post("/items/", response_model=schemas.ItemResponse)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}", response_model=schemas.ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}")
def update_item(item_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db_item.name = item.name
    db_item.description = item.description
    db_item.price = item.price
    db.commit()
    return db_item

# item.dict(exclude_unset=True)
# 👉 exclude_unset=True ka matlab:

# Jo fields user NEHI bhejta, unko ignore karo.
@app.patch("/items/{item_id}")
def patch_item(item_id: int, item: schemas.ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)

    db.commit()
    return db_item


@app.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted"}