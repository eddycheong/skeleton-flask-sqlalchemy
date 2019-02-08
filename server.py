#!/usr/bin/env python

from database import Base, Session, Engine
from database.seed import Seeder 

# Creates all of the tables
Base.metadata.create_all(Engine)

seeder = Seeder()
seeder.seed()