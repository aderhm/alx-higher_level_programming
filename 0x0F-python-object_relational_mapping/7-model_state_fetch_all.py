#!/usr/bin/python3
"""This script lists all states via SQLAlchmey"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

engine_str = "".join([
    "mysql+mysqldb://{}:{}@localhost:3306/{}"
]).format(sys.argv[1], sys.argv[2], sys.argv[3])

engine = create_engine(engine_str)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

rows = session.query(State).all()
for row in rows:
    print("{}: {}".format(row.id, row.name))
