from flask import Flask, request, redirect, render_template
import os
import cgi
import string
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup")
def index():
    return render_template("signup.html")
        

    
def verify_space(text):
    spaces = False
    for char in text:
        if char.isspace():
            spaces = True
    return spaces



@app.route("/signup", methods=['POST'])
def validate_signup():
    username= request.form['username']
    password= request.form['password']
    password2= request.form['password2']
    email = request.form['email']

    username_error= " "
    password_error= " "
    password2_error = " "
    email_error = " "


 
    if verify_space (username):       
        username_error= "Field cannot contain blanks"
    
   
    if verify_space(password):
        password_error= "Field cannot contain blanks"

   
    if password != password2:
        password2_error = "Field does not match password"
    else:
        password2_error = ''
    
    if email and verify_space(email):
        email_error = "Please enter a valid email!"
    if email and not re.match (r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?", email):
        email_error= "Please enter a valid email"
    
    return render_template("welcome.html", username=username)


    if not username_error and not password_error and not password2_error and not email_error: 
        return render_template("welcome.html", username=username)
    else:
        return render_template('signup.html', username=username, email=email, username_error=username_error, password_error=password_error, password2_error=password2_error,
        email_error=email_error)
         
    
    
        

app.run()