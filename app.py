from flask import Flask, render_template, request, url_for, redirect, session
import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.permanent_session_lifetime = timedelta(days=30)



TODO_LIST = [
    {'id':1, 'title':'Add Context', 'detail':'Add context to discord bot ai chat with name of server, etc.', 'status':'complete', 'deadline':'22/12/2026'},
    {'id':2, 'title':'Edit System Prompt', 'detail':'Make system prompt a constant variable', 'status':'pending', 'deadline':'22/11/2026'},
]

"""
    id = unique id for each user for accessing notes
    title = Title of Task todo
    detail = Detail of Task todo
    status = Status of Task (complete, pending, overtime)
    deadline = Date and time to finish/do task
"""

WELCOME_MSGS = [
    'What are your plans for today?',
    'What do you want to do today?',
    'Start tracking your tasks!!',
    'Plan your tasks before you forget..',
    'Stay Disciplined. Write them down'
]

USERS = {
    1: {'first-name': "Joseph",
        'last-name': "Paul",
        'email': 'jotextech@gmail.com',
        'password': 'NewJoe@2009'
        }
}


import time, random
@app.route("/")
def home():
    current_time = int(time.strftime("%H"))
    greeting = 'Good Day'
    if current_time <= 11:
        greeting = 'Good Morning'
    elif current_time <= 16:
        greeting = 'Good Afternoon'
    elif current_time <= 24:
        greeting = 'Good Evening'

    global WELCOME_MSGS
    wlc_msg = random.choice(WELCOME_MSGS)

    if "user_id" in session:
        return render_template(
             'index.html',
             f_name=session.get("user_first_name"),
             greeting=greeting,
             lists=TODO_LIST,
             wlc_msg=wlc_msg)
    
    return render_template('index.html', f_name="User", greeting=greeting, lists=[], wlc_msg=wlc_msg)

@app.route('/delete_todo', methods=['POST'])
def delete_todo():
    target_id = request.form.get('id')
    global TODO_LIST
    TODO_LIST = [todo for todo in TODO_LIST if todo['id'] != target_id ]

@app.route('/new-todo', methods=["POST"])
def new_todo():
    pass

import re
import string
@app.route('/signup', methods=["GET", "POST"])
def signup_page():
    if request.method != 'POST':
        form_data = {'first_name': '', 'last_name': '', 'username': '', 'email': '', 'password': ''}
        return render_template('signup-page.html', form_data=form_data)

    data = request.form
    first_name = data.get('first_name', '').strip()
    last_name = data.get('last_name', '').strip()
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    password = data.get('password', '').strip()
    form_data = {'first_name': first_name, 'last_name': last_name, 'username': username, 'email': email, 'password': password}
    error = ''

    while True:
        # First Name check
        if not first_name:
            error = "First Name is Required"
            break
        elif len(first_name) <= 2 or not isinstance(first_name, str):
            error = "First Name is invalid"
            break

        # Last Name check
        elif not last_name:
            error = "Last Name is Required"
            break
        elif len(last_name) <= 2 or not isinstance(last_name, str):
            error = "Last Name is Invalid"
            break

        # Username check
        elif not username:
            error = "Username is Required"
            break
        elif len(username) < 3:
            error = "Invalid Username"
            break
        elif username in 'Users_db_list':
            error = "This username exists already"
            break
            
        # Email Check
        elif not email:
            error = "Email is Required"
            break
        elif not email or not '@' in email or len(email) <= 7:
            error = 'Invalid Email'
            break

        # Password Check
        elif not password:
            error = 'Password is Required'
            break
        elif len(password) < 4:
            error = "Password is too short"
            break
        found = False
        for i in password:
            if i in string.punctuation:
                found = True
                break
            elif i in string.digits:
                found = True
                break
        if found is False and error == '':
            error = "Your Password is too weak"
            break

    if error:
        return render_template('signup-page.html', error_msg=error, form_data=form_data)
    else:
        global USERS
        last_id = [i for i in USERS.keys()]
        new_user_id = last_id[-1]+1

        USERS[new_user_id] = {'first-name': first_name,
                        'username': username,
                        'last-name': last_name,
                        'email': email,
                        'password': password
                                                }

        session.permanent = True

        session["user_id"] = new_user_id
        session["user_first_name"] = first_name
        session["user_last_name"] = last_name
        session["user_email"] = email

        return redirect(url_for(home))


@app.route('/signin')
def signin_page():
    pass

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for(home))

@app.route('/dashboard')
def account():
    return render_template('pass.html')

if __name__ == "__main__":
    app.run(debug=True)

