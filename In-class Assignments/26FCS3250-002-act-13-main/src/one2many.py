'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Description: An example of an 1-many association
'''

from sqlalchemy import *
from sqlalchemy.engine import *
from sqlalchemy.orm import *

class Base(DeclarativeBase):
    pass

class Employee(Base): 
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dep_code = Column(Integer, ForeignKey("departments.code"))
    department = relationship("Department")

class Department(Base): 
    __tablename__ = "departments"
    code = Column(String, primary_key=True)
    description = Column(String)
    employees = relationship("Employee", back_populates='department')

if __name__ == "__main__": 

    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine) # creates all tables from your model classes
    Session = sessionmaker(engine)
    session = Session()
    with session: 

        # TODO create (and persist) 3 departments
        it = Department(code="IT", description="Information Technology")
        hr = Department(code="HR", description="Human Resources")
        session.add(it)
        session.add(hr)
        session.commit()
        

        # TODO create (and persist) 3 employees
        joe = Employee(id=1, name="Joe", dep_code="IT")
        mary = Employee(id=2, name="Mary", dep_code="HR")
        rick = Employee(id=3, name="Rich", dep_code="HR")
        session.add(joe)
        session.add(mary)
        session.add(rick)  
        session.commit()
        

        # TODO run an employee query to test if the objects were indeed persisted 
        employee = session.query(Employee).filter(Employee.id==1).one()
        print(employee)

        # TODO run a department query to test if the objects were indeed persisted 
        
        it = session.query(Department).filter(Department.code=="IT").one()
        for employee in it.employees:
            print(employee)
