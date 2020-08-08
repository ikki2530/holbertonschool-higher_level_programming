#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""


from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """changes the name of a State object from the database hbtn_0e_6_usa"""
    lh = "localhost"
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
            u, p, lh, d))
    Session = sessionmaker(bind=engine)
    # Updating
    session = Session()
    to_update = session.query(State).filter(State.id == 2).one()
    to_update.name = "New Mexico"
    session.commit()

