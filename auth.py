# # from datetime import datetime, timedelta
# # from fastapi import Depends, HTTPException
# # from fastapi.security import OAuth2PasswordBearer
# # from jose import JWTError, jwt
# # from passlib.context import CryptContext
# # from sqlalchemy.orm import Session
# # from database import get_db

# # import models
# # from database import SessionLocal

# # SECRET_KEY = "YOUR_SECRET_KEY_CHANGE_THIS"
# # ALGORITHM = "HS256"
# # ACCESS_TOKEN_EXPIRE_MINUTES = 60

# # oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # def get_db():
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# # # Password Hashing
# # def hash_password(password: str):
# #     return pwd_context.hash(password)

# # def verify_password(plain, hashed):
# #     return pwd_context.verify(plain, hashed)

# # # Create JWT Token
# # def create_access_token(data: dict):
# #     to_encode = data.copy()
# #     to_encode["exp"] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
# #     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# # # Get Current User from Token
# # def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
# #     try:
# #         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
# #         username = payload.get("sub")
# #     except JWTError:
# #         raise HTTPException(status_code=401, detail="Invalid token")

# #     user = db.query(models.User).filter(models.User.username == username).first()

# #     if not user:
# #         raise HTTPException(status_code=401, detail="User not found")

# #     return user
# from datetime import datetime, timedelta
# from fastapi import Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from sqlalchemy.orm import Session
# from database import get_db
# import models

# SECRET_KEY = "YOUR_SECRET_KEY_CHANGE_THIS"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Password Hashing
# def hash_password(password: str):
#     return pwd_context.hash(password[:72])

# def verify_password(plain, hashed):
#     return pwd_context.verify(plain[:72], hashed)

# # Create JWT Token
# def create_access_token(data: dict):
#     to_encode = data.copy()

#     # EXPIRY
#     to_encode["exp"] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

#     # REQUIRED FIELD FOR JWT USER IDENTIFICATION
#     to_encode["sub"] = data.get("username")

#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# # Get Current User from Token
# def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username = payload.get("sub")
#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid token")
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")

#     user = db.query(models.User).filter(models.User.username == username).first()

#     if not user:
#         raise HTTPException(status_code=401, detail="User not found")

#     return user




# from datetime import datetime, timedelta
# # datetime → current date & time get krne ke liye
# # timedelta → time add/subtract krne ke liye (expiry time banane ke liye)

# from fastapi import Depends, HTTPException
# # Depends → dependency inject krne ke liye (db, auth, etc.)
# # HTTPException → error response bhejne ke kaam aata hai

# from fastapi.security import OAuth2PasswordBearer
# # OAuth2PasswordBearer → token receive/check krne ka FastAPI ka system
# # Login ke baad token bhejne ke liye yeh use hota hai

# from jose import JWTError, jwt
# # JWTError → token invalid hai toh yeh error aata hai
# # jwt → token create aur verify krne ke liye

# from passlib.context import CryptContext
# # CryptContext → password hash karne ka tool (secure banata hai)
# # plain password ko hash me convert aur verify krne ke liye

# from sqlalchemy.orm import Session
# Session → database se read/write krne ka connection
# Query, add, commit sab Session se hota hai

# import hashlib
# # hashlib → hashing functions (MD5, SHA)
# # kabhi kabhi simple hash operations ke liye use hota hai

# from database import get_db
# # get_db → database session dene wala function
# # har API call ko fresh DB connection milta hai

# import models
# models → database tables ka structure
# Models ke through data save/update hota hai















from datetime import datetime, timedelta #date time set krne ke liye
from fastapi import Depends, HTTPException #depend automatic chije me help krta hai jais abr abr token likhrk comapr eke n se m=better dpend(funcname jsime token rteurn hai),ttps exception jb koi eror sue rnot fudn typ aye
from fastapi.security import OAuth2PasswordBearer #usne ne jko logind etail di usenrma passowr dusme se usernmae passowrd shai form me niklane ke liye auth krne ke liye
from jose import JWTError, jwt #jose librmodula hai jisse hm jwt me error ya jwt token manage banat etc krte hai
from passlib.context import CryptContext 
#pasosrwd haisng secruity ke liye crypto hash+verify don krnyi hai
from sqlalchemy.orm import Session #datas eor python ke bich connection banata hai jise hm bina sql ki qury ke hm just pytho anaungue ki help s equey lagate hai dtabase me har bar mw seesion craeate hota hai ahr reiwtes ke sth
import hashlib 
# module func jiski help s edircet hash bnjata hai
# 2-Line Meaning
# hashlib
# hashlib texts/passwords ko unique, irreversible secure code (hash) me convert karta hai.
# Ham use isiliye karte hain kyunki bcrypt 72 bytes limit se bada password handle nahi kar sakta — toh pehle SHA256 se short kar dete hain.
from database import get_db
import models

SECRET_KEY = "YOUR_SECRET_KEY_CHANGE_THIS" #bina eske token na red ho skta hai na kuch ye jsike pas hoga wo fake token aban skta ai
ALGORITHM = "HS256" #algoithum jo token banane read krne me us ehogi hai
ACCESS_TOKEN_EXPIRE_MINUTES = 60 #token ki duartion

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") #tokne es url s emilehha e path se jobh milega uskom verify kre baerae ftoeknke gform me mileg aaag echaalkr oauth2scshme ka suej tokne retrive krn eke liye rknege

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# pasword hash krne ke lye bycript algo use horhi future me algoun cahneg hogi to hash value bhi auto cahnge hojye autoam ye  hi abta hia

# -------------------------------
# PASSWORD HASHING (FIXED)
# -------------------------------
# SHA256 output = fixed 64 characters
def hash_password(password: str):
    """
    bcrypt only supports <= 72 bytes.
    If password is longer, first compress it using SHA256.
    """
    if len(password.encode()) > 72:
        password = hashlib.sha256(password.encode()).hexdigest()

    return pwd_context.hash(password)
# 👉 Final encrypted password return hota hai.


def verify_password(plain: str, hashed: str):
    """
    Same logic: shorten long passwords before verifying.
    """
    if len(plain.encode()) > 72:
        plain = hashlib.sha256(plain.encode()).hexdigest()

    return pwd_context.verify(plain, hashed)


# -------------------------------
# JWT TOKEN GENERATION (FIXED)
# -------------------------------
# Line	Meaning
# data.copy()	User data duplicate
# "sub" set	Token kis user ka hai
# "exp" set	Token kab expire hoga
# jwt.encode(...)	Final JWT token create
def create_access_token(data: dict):
    to_encode = data.copy()

    # JWT requires "sub" for the username
    if "sub" not in to_encode:
        to_encode["sub"] = data.get("username")

    # Set expiry
    to_encode["exp"] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# -------------------------------
# GET CURRENT USER FROM TOKEN
# -------------------------------

# Token header se lo

# Token decode karo

# Usse username nikalo

# DB me user dhundo

# Agar sab sahi → user return, warna 401 error




def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(models.User).filter(models.User.username == username).first()

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user
