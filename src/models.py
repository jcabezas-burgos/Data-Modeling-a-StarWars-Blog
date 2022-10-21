import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
   
    id = Column(Integer, primary_key=True)
    UserName = Column(String(100))
    FirstName = Column(String(50))
    LastName = Column(String(50))
    Email = Column(String(50))
    Favorites = relationship ("Favorite")

class Favorite(Base):
    __tablename__ = "Favorite"
    id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    Userid = Column(Integer, ForeignKey("User.id"))
     
    

class Vehicle(Base):
    __tablename__ = "Vehicle"
   
    id = Column(Integer,primary_key=True )
    Name = Column(String(250))
    Model = Column(String(250))
    Crew = Column(Integer)
    vehicle_class = Column(String(100))
    Pilots = Column(String(100))

class People(Base):
    __tablename__ = "People"
   
    id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    Heigth = Column(Integer) 
    HairColor = Column(String(250))
    SkinColor = Column(String(250))
    eye_color = Column(String(250))
    Birth_Year = Column(String(250))

class Planets(Base):
    __tablename__ = "Planets"
   
    id = Column(Integer, primary_key=True)
    Name = Column(String(250))
    Climate = Column(String(250))
    Gravity = Column(String(250)) 
    Residents = Column(String(250))

## Draw from SQLAlchemy base
render_er(Base, "diagram.png")