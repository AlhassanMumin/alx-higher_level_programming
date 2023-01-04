#!/usr/bin/python3
# Lists all State objects from the database hbtn_0e_6_usa.
# Usage: ./8-model_state_fetch_first.py <mysql username> /
#                                     <mysql password> /
#                                     <database name>
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(sys.argv[1], sys.argv[2],
                            sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).all():
        if 'a' in state.name or 'A' in state.name:
            session.delete(state)
    session.commit()
