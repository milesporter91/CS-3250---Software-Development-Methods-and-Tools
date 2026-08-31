# Overview

The goal of this activity is to demonstrate how to integrate a **Flask** web application with a database to enable structured, persistent data storage. 

# Setup

Begin by creating a virtual environment and installing the following Python packages: 

```
flask
flask-wtf
```

Next, run [src/init_db.py](src/init_db.py) to create the **students** database and the table with the same name. 

# Instructions

Finish the TO-DOs in [src/routes.py](src/routes.py). 

## TO-DO #1: List All Students

* Get a connection
* Create a cursor 
* Using the cursor, execute: "SELECT id, name FROM students"
* Save all students returned by the the cursor
* Return the output of "render_template", rendering "students.html" with the students returned

## TO-DO #2: Create a New Student

* Get a StudentCreateForm
* If the form is validated, get the student's id and name 
* Get a connection
* Create a cursor 
* Using the cursor, insert the new student into the "students" table 
* Commit changes to the database 
* Call "redirect" to "list_students" 
* If the form is NOT validated, return the output of "render_template", rendering "students_create.html" with the form

