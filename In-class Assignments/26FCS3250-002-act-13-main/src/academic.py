'''
CS3250 - Software Development Methods and Tools
Instructor: Thyago Mota
Student:
Description: Activity 13 - SQLAlchemy
'''

from sqlalchemy import *
from sqlalchemy.engine import *
from sqlalchemy.orm import *

class Base(DeclarativeBase):
    pass

class Course(Base): 
    __tablename__ = "courses"
    prefix = Column(String, primary_key=True)
    number = Column(Integer, primary_key=True)
    title = Column(String)
    sections = relationship("Section", cascade="delete")

class Section(Base): 
    __tablename__ = "sections"
    prefix = Column(String, ForeignKey("courses.number"), primary_key=True)
    number = Column(Integer, ForeignKey("courses.number"), primary_key=True)
    seq = Column(Integer, primary_key=True)
    semester = Column(String)
    year = Column(Integer)
    course = relationship("Course", foreign_keys=[Course.prefix, Course.number])
    # instructor = Column(Integer, ForeignKey("instructors.id"))

# class Instructor(Base):
#     __tablename__ = "instructors"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     sections = relationship("Section")

if __name__ == "__main__": 

    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine) # creates all tables from your model classes
    Session = sessionmaker(engine)
    session = Session()
    with session: 

        # creates some objects to test your relationships
        # tmota = Instructor(id=1, name='Thyago Mota')
        # tle = Instructor(id=2, name='ThieNgo Le')
        cs2050 = Course(prefix='CS', number=2050, title='Computer Science 2')
        sec001 = Section(prefix='CS', number=2050, seq=1, instructor=1)
        sec002 = Section(prefix='CS', number=2050, seq=2, instructor=2)
        # session.add(tmota)
        # session.add(tle)
        session.add(cs2050)
        session.add(sec001)
        session.add(sec002)
        session.commit()

        # run some queries to test if the objects were persisted
        print("Sections of CS 2050:")
        cs2050 = session.query(Course).filter(Course.prefix=='CS', Course.number==2050).one()
        for section in cs2050.sections: 
            print(f"\tsection.seq={section.seq}")
        # print('Sections taught by Thyago Mota:')
        # tmota = session.query(Instructor).filter(Instructor.name=='Thyago Mota').one()
        # for section in tmota.sections: 
        #     print(f"\tsection.seq={section.seq}")
        
        # delete a course and see if sections are also deleted
        print("Attempt to delete object 'cs2050'")
        try: 
            session.delete(cs2050)
            print("\tSuccess!")
        except Exception: 
            print("\tCouldn't delete object 'cs2050'!")
        print("Attemp to retrieve sections")
        try: 
            sections = session.query(Section).all()
            for sections in sections: 
                print(f"\tsection.seq={section.seq}")
        except Exception: 
            print("\tSections do not exist anymore!")