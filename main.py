#install fastapi
import os
from fastapi import FastAPI, HTTPException,status,Response,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
#install uvicorn
from fastapi import Body
from pydantic import BaseModel
from random import randrange
from datetime import datetime
from zoneinfo  import ZoneInfo
#install psycopg
#import psycopg
#import time
#get database connection
from database import Base, engine,get_db

#get table model from model
from models import Base,Post,Questions,Answers
# Uncomment the following line if you want to use psycopg2 instead of psycopg8888
#install pydantic
#rom pydantic import model_dump
#install pydantic
from typing import Optional
from routers.gemairouters import generate_geminirouter
from routers.posts import postrouter
from routers.getquestions import questionsrouter
from routers.users import userrouter  
from routers.auth import authrouter     
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
#from config import settings
from fastapi.staticfiles import StaticFiles
#from flask import Flask, jsonify,redirect    


app = FastAPI()
@app.on_event("startup")
def on_startup():
    # Cloud SQL socket is ready now
    Base.metadata.create_all(bind=engine)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:8000",  "http://localhost:8000",
    "http://www.swamy-p.xyz", "https://www.swamy-p.xyz","https://pythonproj-swamy-6ac538a29b8b.herokuapp.com"

]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],              # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allows all headers
)



#print("ssetting..." + str(settings.db_host) + " " + str(settings.db_port) + " " + str(settings.db_user) + " " + str(settings.db_password) + " " + str(settings.db_name))
#get db for sqlalchemy


app.include_router(postrouter)
app.include_router(questionsrouter)
app.include_router(userrouter)
app.include_router(authrouter)
app.include_router(authrouter)
app.include_router(generate_geminirouter)

# Get the parent directory (one level up from this file)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
print("Parent Directory: ", PARENT_DIR)
print("Base Directory: ", BASE_DIR)

# Build the path to /frontend/dist
#static_dir = os.path.join(PARENT_DIR, "frontend", "dist")
#print("Static Directory: ", static_dir)
# Serve React static files
#app.mount("/", StaticFiles(directory=static_dir, html=True), name="quiz-app")
#app.mount("/assets", StaticFiles(directory=os.path.join(static_dir, "assets")), name="assets")


@app.get("/")
def root():
    return {"status": "backend running"}

#@app.get("/{full_path:path}")
#async def serve_react_app(full_path: str):
    #index_path = os.path.join(static_dir, "index.html")
    #return FileResponse(index_path)

@app.get("/quiz-app")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}



@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI! 66"}

#db = session
#print("Database connection established successfully"+" "+str(db))

