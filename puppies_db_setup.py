import os, sys

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	"""Model for Shelters"""
	__tablename__ = 'shelter'
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	address = Column(String(80))
	city = Column(String(50))
	state = Column(String(2))
	email = Column(String(100))
	website = Column(String(500))
	zipcode = Column(String(5))
	sqlite_autoincrement = True

class Puppy(Base):
	"""Model for Puppies"""
	__tablename__ = 'puppy'
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	date_of_birth = Column(Date)
	breed = Column(String(100))
	gender = Column(String(1))
	weight = Column(Float)
	picture = Column(String(500))
	status = String(25)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)
	sqlite_autoincrement = True

class Owner(Base):
	"""Model for Owners"""
	__tablename__ = 'owner'
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	email = Column(String(100))
	date_of_birth = Column(Date)
	gender = Column(String(20))
	password = String(20)
	puppy_id = Column(Integer, ForeignKey('puppy.id'))
	sqlite_autoincrement = True

#Class for owner puppy matches?

		


engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)