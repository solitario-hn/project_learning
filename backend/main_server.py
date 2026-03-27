from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select




class Session(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id:int=Field(index=True)
    session_id: str=Field(index=True)
    expired_at:datetime
    updated_at:datetime=Field(default_factory=datetime.utcnow)

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email:str=Field(unique=True,index=True)
    password: str



engine = create_engine("sqlite:///database.db")

def get_session():
    with Session(engine) as session:
        yield session



app = FastAPI()
@app.on_event("startup")
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.post("/signup")
def signup(): 
    
 print("hello")
 return


@app.get("/")
def root():
    return {"hello anaya"}

# @app.post("/login")


# @app.post("/logout")

# @app.get("/profile")



#setting up CORSMiddleware
origins=["http://127.0.0.1:8000/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
aach