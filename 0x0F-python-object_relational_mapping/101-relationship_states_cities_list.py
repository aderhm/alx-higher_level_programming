#!/usr/bin/python3
"""This script lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa"""
import sys
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import Base
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).order_by(State.id).all()

    for d in data:
        print("{}: {}".format(d.id, d.name))
        for c in d.cities:
            print("\t{}: {}".format(c.id, c.name))

    session.close()
