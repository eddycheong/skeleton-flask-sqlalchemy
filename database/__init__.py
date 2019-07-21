import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read('alembic.ini')
connection_url = config['alembic']['sqlalchemy.url']

Engine = create_engine(connection_url, connect_args={'check_same_thread': False})
Session = sessionmaker(bind=Engine)

