from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils import JsonConfigParser

database_config = JsonConfigParser().config["database"]

Engine = create_engine(database_config["connection_url"], connect_args={'check_same_thread': False})
Session = sessionmaker(bind=Engine)

