from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from utils import JsonConfigParser

config = JsonConfigParser().config
database_config = config["database"]

Base = declarative_base()
Engine = create_engine(database_config["connection_url"], connect_args={'check_same_thread': False})
Session = sessionmaker(bind=Engine)