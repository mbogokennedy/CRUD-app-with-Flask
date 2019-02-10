from flask import render_template

from app import app
from app.data import courses

Courses = courses()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/courses')
def courses():
    return render_template("courses.html", courses = Courses)

@app.route('/course/<string:id>/')
def course(id):
    return render_template("course.html", id = id)

