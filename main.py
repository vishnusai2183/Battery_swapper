from flask import Flask, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

# mydatabase connecction
local_server=True
app=Flask(__name__) 
app.secret_key="secretkey"

# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databasename'3306
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost:3307/miniproj'
db=SQLAlchemy(app)

#creating db models
class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
 

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/usersignup")
def usersignup():
    return render_template("usersignup.html")


@app.route("/userlogin")
def userlogin():
    return render_template("userlogin.html")


# testing whether db is connected or not
@app.route("/test")
def test():
    try:
        a=Test.query.all()
        print(a)
        return f'MY DATABASE IS CONNECTED {a} '
    except Exception as e:
            print(e)
            return f'MY DATABASE IS NOT CONNECTED {e}'






app.run(debug=True) 
