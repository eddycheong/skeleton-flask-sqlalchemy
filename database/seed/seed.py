#!/usr/bin/env python

from database import Session
from database.model import User

session = Session()

def seeding():
    session.add(User(name="test_user"))
    session.add(User(name="test_another"))
    session.commit()