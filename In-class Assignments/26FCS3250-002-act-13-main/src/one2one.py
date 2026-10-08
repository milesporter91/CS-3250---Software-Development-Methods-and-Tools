'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Description: An example of an 1-1 association
'''

from sqlalchemy import *
from sqlalchemy.engine import *
from sqlalchemy.orm import *

class Base(DeclarativeBase):
    pass

class President(Base): 
    __tablename__ = "presidents"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    company = relationship("Company")

class Company(Base): 
    __tablename__ = "companies"
    code = Column(Integer, primary_key=True)
    title = Column(String)
    president_id = Column(Integer, ForeignKey("presidents.id"))

if __name__ == "__main__": 

    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine) # creates all tables from your model classes
    Session = sessionmaker(engine)
    session = Session()
    with session: 

        # TODO create (and persist) a president
        pass

        # TODO create (and persist) a company associated with the president above
        

        # TODO run a query to test if the objects were indeed persisted 
        