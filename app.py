#!/usr/bin/python3
import os

from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
##postgress
engine = create_engine("mysql+pymysql://root:hameed@localhost:3307/recod")


db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=['GET'])
def index():
      
    return render_template("index.html")


@app.route("/add_student", methods=['GET'])
def insert_new_student():
    return render_template("insert_new_student.html")
    

@app.route("/intro", methods=['POST', 'GET'])
def intro():
    if request.method == "POST":

        name = request.form.get("name")
        rollno = request.form.get("rollno")
        session = request.form.get("session")
        email = request.form.get("email")
        subfee = request.form.get("subfee")
        duefee = request.form.get("duefee")
        program = request.form.get("program")
        db.execute("INSERT into fee(name, rollno, session, email, subfee, duefee, program) VALUES (:name, :rollno, :session, :email, :subfee, :duefee, :program)",
                {"name": name, "rollno": rollno, "session": session, "email": email, "subfee": subfee, "duefee": duefee, "program": program})
        db.commit()

        # Get all records again
        students = db.execute("SELECT * FROM fee").fetchall()
        return render_template("intro.html", students=students)
    else:
        students = db.execute("SELECT * FROM fee").fetchall()
        return render_template("intro.html", students=students)




if __name__ == "__main__":
    app.run(debug=True)