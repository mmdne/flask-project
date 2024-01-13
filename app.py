from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(100))
    password = db.Column(db.String(50))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.username}"

@app.route("/")
def home():
    name = "mr.Nezafat"
    age = 23
    blogs = {"one":"blog one", "two":"blog two", "three":"blog three"}
    return render_template("pages/index.html", user=name, age=age, blogs=blogs)

@app.route("/about")
def about():
    return render_template("pages/about.html")

@app.route("/login")
def login():
    return render_template("pages/login.html")

@app.route("/after_login/", methods=["POST","GET"])
def after_login():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        user_data = User(username=username, email=email)
        db.session.add(user_data)
        db.session.commit()
    return f"u log in page as username: {username} and email:{email}"

if __name__ == "__main__":
    app.run(debug=True)












