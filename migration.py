#!/usr/bin/env python
from database import Base, Engine
from database.seed import Seeder

# Create database tables
Base.metadata.create_all(Engine)

# Creates all of the tables
seeder = Seeder()
seeder.seed()