#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""


from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """adds the State object “Louisiana” to the database hbtn_0e_6_usa"""
    lh = "localhost"
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
            u, p, lh, d))
    Session = sessionmaker(bind=engine)
    # Adding Louisiana
    session = Session()
    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    print(new.id)
