from app import app, get_conn
from flask import render_template, redirect, url_for
from app.forms import StudentCreateForm
# TODO #1 list all students 
# * Get a connection
# * Create a cursor 
# * Using the cursor, execute: "SELECT id, name FROM students"
# * Save all students returned by the the cursor
# * Return the output of "render_template", rendering "students.html" with the students returned
@app.route('/students')
def list_students():
   conn = get_conn()
   cursor = conn.cursor()
   cursor.execute("SELECT id, name FROM students")
   students = cursor.fetchall()
   return render_template("students.html", students=students )

# TODO #2 using a form, allow new students to be added
# * Get a StudentCreateForm
# * If the form is validated, get the student's id and name 
# * Get a connection
# * Create a cursor 
# * Using the cursor, insert the new student into the "students" table 
# * Commit changes to the database 
# * Call "redirect" to "list_students" 
# * If the form is NOT validated, return the output of "render_template", rendering "students_create.html" with the form
@app.route('/students/create', methods=['GET', 'POST'])
def create_student():
    form = StudentCreateForm()
    if form.validate_on_submit():
        id = form.data["id"]
        name = form.data["name"]
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO students VALUES ('{id}', '{name}') ")
        return redirect(url_for('list_students'))
        
    else:
        return render_template("students_create.html", form=form)

   
