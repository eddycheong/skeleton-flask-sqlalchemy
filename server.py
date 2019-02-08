#!/usr/bin/env python

from flask import Flask

from database import Base, Session, Engine
from database.seed import Seeder 

# Creates all of the tables
Base.metadata.create_all(Engine)

seeder = Seeder()
seeder.seed()

app = Flask("__name__")

@app.route("/")
def index():
    return "Hello World "

if __name__ == "__main__":
    app.run(debug=True)