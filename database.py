# # # from sqlalchemy import create_engine
# # # # create enine kis trh ka databse cinect ora hai sql mysqll slqie mindi ye sb se rel 
# # # # kaam krta hai or mangekrta hai
# # # # declarative_base modle abnane ke lue base class hai
# # # from sqlalchemy.ext.declarative import declarative_base
# # # # om sqlalchemy.orm import sessionmaker

# # # # sessionmaker = sessions banane ka factory

# # # # Session = database ke saath ek temporary connection jisme hum:
# # # # ✔ Query
# # # # ✔ Insert
# # # # ✔ Update
# # # # ✔ Delete
# # # # kar sakte hain.
# # # from sqlalchemy.orm import sessionmaker
# # # # ) DATABASE URL
# # # # -----------------------------------------
# # # # DATABASE_URL = "sqlite:///./test.db"

# # # # Meaning:

# # # # sqlite = kaunsa database use kar rahe ho

# # # # :/// = SQLAlchemy ka pattern

# # # # ./test.db = current folder me test.db file banega

# # # # So, ye line define karta hai ki hume SQLite database file use karna hai.
# # # # SQLAlchemy Python ka database se baat karne ka framework hai.
# # # # Yani Python aur Database ke beech ka bridge

# # # # Agar PostgreSQL hota:

# # # # postgresql://user:pass@localhost:5432/mydb


# # # # MySQL hota:

# # # # mysql+pymysql://user:pass@localhost/mydb
# # # # DATABASE_URL = "sqlite:///./test.db"
# # # # engine = create_engine(
# # # #     DATABASE_URL,
# # # #     connect_args={"check_same_thread": False}
# # # # )


# # # # post

# # # DATABASE_URL = "postgresql://username:password@localhost/dbname"
# # # engine = create_engine(DATABASE_URL)  # no connect_args needed

# # # # autocommit=False → you control when changes are committed (permanent).

# # # # autoflush=False → you control when changes are sent to DB for queries, but not necessarily saved permanently.
# # # SessionLocal = sessionmaker(
# # #     autocommit=False,#likhte sth canges refkec t cimmnit na ho
# # #     autoflush=False, #database me jo cnges ki req ja rhi hai quires ke liye wo save na ho eprmmany
# # #     bind=engine #bidn btta ahi queiry kaha bejhnu hau jaue bind =enginer hai ro enginer ibjevt datasbe wala url store krta ai sqlite ka
# # # ) 
# # # #dircetly db s einetct ya opetion nii lagaye ham sessionfactory bnate ha furyet yekrte hi
# # # # db = SessionLocal()  # create a session
# # # # new_user = User(name="Alice")
# # # # db.add(new_user)     # add data to session
# # # # db.commit()          # save changes permanently
# # # # db.close()           # close the session

# # # SessionLocal = sessionmaker(
# # #     autocommit=False,
# # #     autoflush=False,
# # #     bind=engine
# # # )
# # # #declarative base function hai sqlarchemy me uss ehmne esse hamne base class banayi
# # # # almost chije cod eme cals shi ahi pr unclases me konsi class table hai ye apn base i help se pta krneg
# # # # jo hi class base ko inehrit krei woi table hogi
# # # Base = declarative_base()
# # from sqlalchemy import create_engine
# # from sqlalchemy.orm import sessionmaker, declarative_base
# # # import os
# # # from dotenv import load_dotenv  #.env fie  raed rkne ke liey

# # # DATABASE_URL = "postgresql://myuser:mypassword@localhost/testdb"
# # # # direct as kr skti hu ya phri bets prtaice hai .env file su ekru amnually banakr pr uske liye dotev isnyall rkna hogaDATABASE_URL = "postgresql://Vaishnavi:gammaedge@01@localhost/testdb"

# # # engine = create_engine(DATABASE_URL)  # no need for connect_args
# # from dotenv import load_dotenv
# # import os
# # load_dotenv()

# # DATABASE_URL = os.getenv("DATABASE_URL")
# # engine = create_engine(DATABASE_URL)

# # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# # Base = declarative_base()
# # # engine.connect()
# # # print("PostgreSQL working ✅")

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from dotenv import load_dotenv  #.env fie ko reda krn eke iye us ehoit hai eska jaise hi ye particau fun call krte hai sb avirb chije load hojati hai python ile me
# import os # #pythom moule syste, ometrction file folder envir bribl read oath etc handl ekrne me hlep krta hai

# # Load .env file
# load_dotenv()

# # DATABASE_URL should be inside .env like:
# # DATABASE_URL=postgresql://username:password@localhost:5432/testdb
# DATABASE_URL = os.getenv("DATABASE_URL")

# # Create engine
# engine = create_engine(DATABASE_URL)
# #connection banata hai db or fatsiak
# # Session factory (DB session)
# SessionLocal = sessionmaker(
#     autocommit=False, #autsav ei hoga db me jsis enrml get wlai ceij bhi db me na cahki jey
#     autoflush=False, #data temp db me kjyega
#     bind=engine #batat hai ki konsi db se conenection bnana hai
# )

# # Base class for models
# Base = declarative_base()
# # get_db() ek database connection banata hai (SessionLocal()),
# # phir API ke kaam hone ke baad usse close kar deta hai.
# # IMPORTANT: This function is required by FastAPI for dependency injection
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()






from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Example .env value (must be correct):
# DATABASE_URL=postgresql://postgres:1234@localhost:5432/testdb
DATABASE_URL = os.getenv("DATABASE_URL")

# Create engine (connects to PostgreSQL)
engine = create_engine(DATABASE_URL)

# Create DB session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all models
Base = declarative_base()

# DB session dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

