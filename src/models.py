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
    name = Column(String(50))
    email = Column(String(50), nullable=True)
    phonenumber = Column(String(50), nullable=True)
    address = Column(String(50), nullable=True)
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
    name = Column(String(50))
    birthYear = Column(String(50))
    height = Column(String(50))
    mass = Column(String(50))
    gender = Column(String(50))
    hairColor = Column(String(50))
    skinColor = Column(String(50))
    homeworld = Column(String(50))
    categoryID = Column(Integer, ForeignKey('category.categoryID'))
    favoritos = relationship(Favoritos)

class Planets(Base): 
    __tablename__ = 'planets'
    planetID  = Column(Integer, primary_key=True)
    name = Column(String(50))
    population = Column(String(50))
    rotationPeriod = Column(String(50))
    orbitalPeriod = Column(String(50))
    diameter = Column(String(50))
    gravity = Column(String(50))
    terrainGlasslands = Column(String(50))
    surfaceWather = Column(String(50))
    climate = Column(String(50))
    categoryID = Column(Integer, ForeignKey('category.categoryID'))
    favoritos = relationship(Favoritos)

class Category(Base): 
    __tablename__ = 'category'
    categoryID = Column(Integer, primary_key=True)
    name = Column(String(50))
    planets = relationship(Planets)
    characters = relationship(Characters)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
