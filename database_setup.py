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
	username = Column(String, unique=True)
	password = Column(String)
	day_of_birth = Column(Integer) #multiple choice
	month_of_birth = Column(Integer) #multiple choice
	year_of_birth = Column(Integer) #multiple choice
	gender = Column(String)  #multiple choice
	hometown = Column(String)
	profession = Column(String)
	about_me = Column(String)
	profile_pic = Column(String, unique=True)
	course = relationship("Hospital", uselist=True)

	
	def set_photo(self, profile_pic):
		self.profile_pic = profile_pic

class Hospital(Base):
	__tablename__ = 'hospital'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	line_time = Column(Integer) #in minutes
	availability = Column(String) #multiple choice
	service = Column(Integer) #multiple choice
	area = Column(String) #multiple choice
	city = Column(Integer) #multiple choice
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship("User")

	def __getitem__(self, item):
		return getattr(self, item)