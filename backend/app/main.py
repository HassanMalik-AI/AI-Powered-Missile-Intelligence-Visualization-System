# Fastapi entry point
from fastapi import FastAPI,Depends
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from app import models
from app.database import Base,engine


app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.get('/')
async def root():
    return {'message' : 'Welcome to the AI-Powered Missile Intelligence Dashboard'}



