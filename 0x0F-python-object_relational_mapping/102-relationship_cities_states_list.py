#!/usr/bin/python3
"""This script lists all City objects from the database hbtn_0e_101_usa"""
import sys
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(City).order_by(City.id).all()

    for d in data:
        print("{}: {} -> {}".format(d.id, d.name, d.state.name))

    session.close()
