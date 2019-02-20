from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Engine = create_engine('sqlite:///sqlalchemy_example.db', connect_args={'check_same_thread': False})
Session = sessionmaker(bind=Engine)