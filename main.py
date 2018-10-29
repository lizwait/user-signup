from flask import Flask, request
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_form_inputs():
    form = jinja_env.get_template('form_inputs.html')

    return form.render()

@app.route("/", methods = ['POST'])
def input_validation():
    form = jinja_env.get_template('form_inputs.html')
    userName = request.form['user-name']
    userPassword1 = request.form['user-password1']
    userPassword2 = request.form['user-password2']
    userEmail = request.form['user-email']

    username_error = ''
    if userName == "" or len(userName) < 3 or len(userName) >20 or (' ' in userName): 
        username_error = "Please enter a valid username."
    
    password_error1 = ''
    if userPassword1 != userPassword2:
        password_error1 = "Please enter matching passwords."

    password_error2 = ''
    if userPassword1 == "" or len(userPassword1) < 3 or len(userPassword1) >20 or (' ' in userPassword1):
        password_error2 = "Please enter valid password."

    email_error = ''
    if userEmail != "":
        if ("@" not in userEmail) or ("." not in userEmail) or (" " in userEmail) or len(userEmail) < 3 or len(userEmail) >20 :
            email_error = "Please enter valid email."

    if username_error == '' and password_error1 == '' and password_error2 == '' and email_error == '':
        welcomePage = jinja_env.get_template('welcome.html')
        return welcomePage.render(userName=userName)

    return form.render(userName=userName, 
    passwordError1=userPassword1, 
    passwordError2=userPassword2, 
    userEmail=userEmail, 
    username_error=username_error,
    password_error2=password_error2,
    password_error1=password_error1,
    email_error=email_error
    )

app.run()