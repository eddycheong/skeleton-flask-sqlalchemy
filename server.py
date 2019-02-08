#!/usr/bin/env python

from database import Base, Session, Engine
from database import seed

Base.metadata.create_all(Engine)

seed.seeding()
