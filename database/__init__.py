from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Engine = create_engine('sqlite:///sqlalchemy_example.db')
Session = sessionmaker(bind=Engine)