import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Customers(Base): 
    __tablename__ = 'customers'
    # Here we define columns for the table.
    customerID = Column(Integer, primary_key=True)
    name = Column(String(250))
    email = Column(String(250), nullable=True)
    phonenumber = Column(String(100), nullable=True)
    address = Column(String(250), nullable=True)
    isActive = Column(Boolean) 

class Favoritos(Base): 
    __tablename__ = 'favoritos'
    favoritoID = Column(Integer, primary_key=True)
    customer_ID = Column(Integer, ForeignKey('customers.customerID'))
    characterID = Column(Integer, ForeignKey('characters.characterID'))
    planetID = Column(Integer, ForeignKey('planets.olanetID'))
    isActive = Column(Boolean) 
    customer = relationship(Customers)

class Characters(Base): 
    __tablename__ = 'characters'
    characterID = Column(Integer, primary_key=True)
    name = Column(String(250))
    birthYear = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    gender = Column(String(250))
    hairColor = Column(String(250))
    skinColor = Column(String(250))
    homeworld = Column(String(250))
    categoryID = Column(Integer, ForeignKey('category.categoryID'))
    favoritos = relationship(Favoritos)

class Planets(Base): 
    __tablename__ = 'planets'
    planetID  = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(String(250))
    rotationPeriod = Column(String(250))
    orbitalPeriod = Column(String(250))
    diameter = Column(String(250))
    gravity = Column(String(250))
    terrainGlasslands = Column(String(250))
    surfaceWather = Column(String(250))
    climate = Column(String(250))
    categoryID = Column(Integer, ForeignKey('category.categoryID'))
    favoritos = relationship(Favoritos)

class Category(Base): 
    __tablename__ = 'category'
    categoryID = Column(Integer, primary_key=True)
    name = Column(String(250))
    planets = relationship(Planets)
    characters = relationship(Characters)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
