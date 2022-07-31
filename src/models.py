import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    idUser = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    userPassword = Column(String(250), nullable=False)

class CharacterFavs(Base):
    __tablename__ = 'characterFavs'
    userID = Column(Integer, ForeignKey('user.id'), primary_key=True)
    characterUid = Column(Integer, ForeignKey('characters.uid'), primary_key=True)

class Characters(Base):
    __tablename__ = 'characters'
    characterUid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)
    gender = Column(String(250))
    created = Column(Integer) 
    edited = Column(Integer)
    homeworld = Column(String(250), ForeignKey('planets.uid'))

class PlanetFavs(Base):
    __tablename__ = 'planetFavs'
    userID = Column(Integer, ForeignKey('user.id'), primary_key=True)
    planetUid = Column(Integer, ForeignKey('planets.id'), primary_key=True)

class Planets(Base):
    __tablename__ = 'planets'
    planetUid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    created = Column(Integer) 
    edited = Column(Integer) 

class VehicleFavs(Base):
    __tablename__ = 'vehicleFavs'
    userID = Column(Integer, ForeignKey('user.id'), primary_key=True)
    characterUid = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    vehicleUid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    manufacturer = Column(String(250))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(250))
    films = Column(Integer)
    pilots = Column(Integer)
    created = Column(Integer)
    edited = Column(Integer)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')