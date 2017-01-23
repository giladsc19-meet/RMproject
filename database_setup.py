from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base): 
	__tablename__ = 'user' 
	id = Column(Integer, primary_key=True) 
	first_name = Column(String)
	last_name = Column(String)  
	username = Column(String)
	password = Column(String)
	day_of_birth = Column(Integer) #multiple choice
	month_of_birth = Column(Integer) #multiple choice
	year_of_birth = Column(Integer) #multiple choice
	gender = Column(String)  #multiple choice
	hometown = Column(String)
	proffesion = Column(String)
	about_me = Column(String)
	course = relationship("Course", uselist=True)

class Course(Base):
	__tablename__ = 'course'
	id = Column(Integer, primary_key = True)
	topic = Column(String) #multiple choice
	name = Column(String)
	difficulty = Column(String) #multiple choice
	estimated_time = Column(String) #in minutes
	description = Column(String)
	#file = 
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship("User")
