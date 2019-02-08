#!/usr/bin/env python
from database import Base, Session, Engine
from database.seed import Seeder
from controller import app

# Creates all of the tables
Base.metadata.create_all(Engine)

seeder = Seeder()
seeder.seed()

if __name__ == "__main__":
    app.run(debug=True)