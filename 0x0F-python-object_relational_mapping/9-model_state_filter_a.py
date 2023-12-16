#!/usr/bin/python3
""""""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_an_a = session.query(State).filter(
        State.name.like('%a%')
        ).order_by(State.id).all()
    for state in states_with_an_a:
        print("{}: {}".format(state.id, state.name))
    session.close()
