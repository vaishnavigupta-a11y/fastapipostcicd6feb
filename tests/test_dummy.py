from fastapi.testclient import TestClient
from main import app
from database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# -------------------------------
# 1️⃣ Create Test Database (SQLite)
# -------------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base.metadata.create_all(bind=engine)

# --------------------------------
# 2️⃣ Override get_db dependency
# --------------------------------
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# --------------------------------
# 3️⃣ Dummy Test Cases
# --------------------------------

def test_dummy():
    assert 1 == 1


def test_home_route():
    response = client.get("/")
    assert response.status_code == 200


def test_create_user():
    data = {
        "username": "dummyuser",
        "email": "dummy@example.com",
        "password": "password123"
    }
    response = client.post("/register", json=data)
    assert response.status_code in [200, 201]


def test_login_user():
    data = {
        "username": "dummyuser",
        "password": "password123"
    }
    response = client.post("/login", data=data)
    assert response.status_code == 200
    assert "access_token" in response.json()
