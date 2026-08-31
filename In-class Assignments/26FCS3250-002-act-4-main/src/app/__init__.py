from flask import Flask, g
import sqlite3

def get_conn(): 
    with app.app_context():
        if 'conn' not in g:
            g.conn = sqlite3.connect('students.db')
        return g.conn

app = Flask("Students App")
app.config['SECRET_KEY'] = 'you-will-never-guess'

from app import routes