#!/usr/bin/env python

from database import Base, Session, Engine
from database import seed

# Creates all of the tables
Base.metadata.create_all(Engine)

# Seed the database
seed.seeding()