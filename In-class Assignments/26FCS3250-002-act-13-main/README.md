# Overview

This activity is a hands-on introduction to Object-Relational Mapping (ORM) using [SQLAlchemy](https://www.sqlalchemy.org/), Python's most widely used ORM library. An ORM lets you work with a relational database through plain Python classes and objects instead of writing raw SQL, mapping tables to classes, rows to instances, and foreign keys to object relationships.

The goal of this activity is to practice modeling and implementing the three core relationship types found in relational databases, and to see how each one is expressed both at the database level (UML class diagrams) and at the ORM level (SQLAlchemy model classes):

- **One-to-one** ([one2one.py](src/one2one.py)) - a `President` and the `Company` they run.
- **One-to-many** ([one2many.py](src/one2many.py)) - a `Department` and its `Employee`s.
- **Many-to-many** ([many2many.py](src/many2many.py)) - `Employee`s and `Project`s, linked through an association table.
 
By completing this activity, you should be able to:

1. Define SQLAlchemy model classes using the Declarative ORM (`DeclarativeBase`, `Column`, `relationship`).
2. Translate a UML class diagram with association multiplicities (`1`, `N`) into foreign keys and `relationship()` mappings.
3. Create an engine, open a session, and persist objects to a SQLite database.
4. Navigate relationships from either side of an association (e.g. `employee.department` vs. `department.employees`).
5. Query persisted objects back out of the database and confirm relationships were saved correctly.

## Project Structure

```
act-13/
├── src/                  # Starter files with TODOs for you to complete
│   ├── one2one.py
│   ├── one2many.py
│   ├── many2many.py
│   └── academic.py       # Bonus: cascading deletes and a commented-out 1-many extension
├── pics/                 # Rendered UML diagrams
└── *.wsl                 # PlantUML source for the class diagrams
```

Each `.wsl` file contains a PlantUML diagram describing the relationship's multiplicity (e.g. `Department "1" o--> "N" Employee`), and its matching `.py` file in `src/` implements that diagram as SQLAlchemy models with an association exercise left as a `TODO`.

## Getting Started

1. Create and activate a virtual environment

2. Install SQLAlchemy:
   ```
   pip3 install sqlalchemy
   ```
3. Open each file in `src/` in order (`one2one.py` → `one2many.py` → `many2many.py`) and fill in the `TODO` sections:
   - Create and persist the required objects.
   - Associate them according to the relationship type.
   - Write a query that proves the objects and their relationships were saved.

4. Run each script directly:
   ```
   python src/one2one.py
   ```
   Each run creates (or reuses) a local `app.db` SQLite file. Delete it between runs if you want to start from a clean database.

## Bonus

[academic.py](src/academic.py) extends the one-to-many idea to a `Course`/`Section` relationship and introduces `cascade="delete"`, showing how deleting a parent object can automatically delete its dependents. It also has a commented-out `Instructor` class you can uncomment to practice adding a second one-to-many relationship (`Instructor` → `Section`) to the same model.
