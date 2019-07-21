from sqlalchemy import Column, Integer, String
from database.model import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)