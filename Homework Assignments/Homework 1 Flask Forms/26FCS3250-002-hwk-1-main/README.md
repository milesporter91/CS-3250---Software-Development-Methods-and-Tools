# Overview

In class, you were introduced to Flask, a lightweight framework for building web applications in Python. You can find the official Flask documentation [here](https://flask.palletsprojects.com/en/stable/). In this homework assignment, you’ll enhance a simple web app by incorporating templates and web form processing.

The web app you’ll create consists of just two pages:

A page displaying a list of recipes:

![pics/pic1.png](pics/pic1.png)

A page where users can create new recipes using a simple form:

![pics/pic2.png](pics/pic2.png)

Once submitted, the new recipe is added to the list:

![pics/pic3.png](pics/pic3.png)

# Setup

Start by creating a virtual environment named **.venv.** Then, install the required packages:

```
flask
flask-wtf
```

Set the **FLASK_APP** environment variable to **src/app** from the project’s root directory.

# Templates

Templates allow you to separate HTML from Python logic. For example, the following template renders the values of title and user:

```
<!DOCTYPE html>
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        <h1>Hello, {{ user }}!</h1>
    </body>
</html>
```

Use the **render_template** function to pass values to the template:

```
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="CS 3250", user="Thyago")
```

Templates also support conditional statements:

```
<!DOCTYPE html>
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        {% if user %}
            <h1>Hello, {{ user }}!</h1>
        {% else %}
            <h1>Hello, World!</h1>
        {% endif %}
    </body>
</html>
```

And loops:

```
<!DOCTYPE html>
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body>
        {% if user %}
            <h1>Hello, {{ user }}!</h1>
            <p>Classes that you will be teaching this semester:</p>
            {% for class in classes %}
                <p>{{ class }}</p>
            {% endfor %}
        {% else %}
            <h1>Hello, World!</h1>
        {% endif %}
    </body>
</html>
```

To render this with values:

```
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="CS 3250", user="Thyago", classes=['CS2050', 'CS3250'])
```

Templates can also extend other templates using:

```
{% extends "parent.html" %}
```

# Forms

Forms allow users to submit data to your web app. Flask-WTF is a Flask extension that simplifies form handling. Install it with:

```
pip3 install flask-wtf
```

Here’s an example of a form with a text field and a submit button:

```
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    user = StringField('User', validators=[DataRequired()])
    submit = SubmitField('Sign In')
```

Flask-WTF supports various field types: **IntegerField**, **StringField**, **DateField**, **SelectField**, **SubmitField**, and more. Refer to the Flask-WTF documentation for details.

# Instructions 

## TO-DO #1

In [templates/index.html](templates/index.html), use a for loop to render the recipe list using the recipes parameter. Add a conditional to alternate row styles:

* Use the class **even_row** if **loop.index** is even.
* Use **odd_row** otherwise.

These classes are defined in [static/style.css](static/style.css).

## TO-DO #2

In [src/app/forms.py](src/app/forms.py), complete the recipe form by adding the missing fields: **title**, **type**, and **tags**.

**title** and **type** should be required fields. 

Use appropriate field types. For example, **type** should be a **SelectField** with options: 'breakfast', 'appetizer', 'side dish', 'main course', and 'dessert'. 

## TO-DO #3

In [src/app/routes.py](src/app/routes.py), complete the line that appends a new recipe by including the missing fields from the form object.

## TO-DO #4

In [templates/recipes_create.html](templates/recipes_create.html), complete the form rendering by adding the missing fields.

# Submission

Once all TO-DOs are completed, submit your changes with the commit message:
"final submission". 

# Rubric

This assignment is worth 5 points, distributed as follows:

```
+1 TO-DO #1: for loop implementation
+1 TO-DO #1: conditional statement for row styling
+1 TO-DO #2: form field completion
+1 TO-DO #3: route logic completion
+1 TO-DO #4: form rendering in HTML
```