#!/usr/bin/python3
""""""
import sys
from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
            )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    session.add(new_state)

    new_city = City(name="San Francisco", state_id=new_state)
    new_state.cities.append(new_city)
    session.add(new_city)

    session.commit()

    session.close()
