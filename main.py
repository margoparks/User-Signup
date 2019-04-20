from flask import Flask, request, redirect, render_template
import os
import cgi
import string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup")
def index():
    return render_template("signup.html")

def spaces(text):
    try:
        text.index('')
        return True
    except ValueError:
        return False




@app.route("/signup", methods=['POST'])
def validate_signup():
    username= request.form['username']
    password= request.form['password']
    password2= request.form['password2']
    email = request.form['email']

    username_error=''
    password_error= ''
    password2_error = ''
    email_error = ''


    if '' in username:
        username_error='Field cannot contain blanks'
    else: 
        username_error = ''

    
    if '' in password:
        password_error='Field cannot contain blanks'
    else:
        password_error = ''

    
    if password != password2:
        password2_error = 'Field does not match password'
    else:
        password2_error = ''
    
    ###if spaces(email):
        # email_error='Field cannot contain blanks'
       # email=''
    #else:
        #if '@' and '.' not in email:
            #email_error='Enter a valid email address'
            #email=''

    
    if username_error or password_error or password2_error: 
        return render_template('signup.html', username=username, password=password, password2=password2,
        username_error=username_error, password_error=password_error, password2_error=password2_error )
    else:
        return "success!"

app.run()