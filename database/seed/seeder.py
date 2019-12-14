#!/usr/bin/env python

from database import Session
from database.model import User
from database.seed.users import seed_users

class Seeder():
    def __init__(self):
        self._session = Session()

    def _add_seed_data(self, entities):
        for entity in entities:
            self._session.add(entity)

    def seed(self):
        self._add_seed_data(seed_users())
        self._session.commit()