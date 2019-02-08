#!/usr/bin/env python

from database import Session
from database.model import User

class Seeder():
    def __init__(self):
        self._session = Session()

    def seed(self):
        self._session.add(User(name="seed_user"))
        self._session.commit()