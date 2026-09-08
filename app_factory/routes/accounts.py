from flask import Blueprint, render_template, jsonify, request, url_for, redirect, session

accs_bp = Blueprint('accounts', __name__)



import re
import string
@accs_bp.route('/signup', methods=["GET", "POST"])
def signup_page():
    from app_factory.global_storage import Users
    if request.method != 'POST':
        form_data = {'first_name': '', 'last_name': '', 'username': '', 'email': ''}
        return render_template('signup-page.html', form_data=form_data)

    data = request.form
    first_name = data.get('first_name').strip()
    last_name = data.get('last_name').strip()
    username = data.get('username').strip()
    email = data.get('email').strip()
    password = data.get('password').strip()
    form_data = {'first_name': first_name, 'last_name': last_name, 'username': username, 'email': email}
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
            error = "Username is too short"
            break
        elif len(username) > 20:
            error = "Username is too long"
            break
        elif username in session or username in [Users[i]['username'] for i in Users.keys()]:
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
        elif password == username:
            error = "Password is same with username"
            break
        break

    if error:
        return render_template('signup-page.html', error_msg=error, form_data=form_data)

    # Security for user_id
    last_id = [i for i in Users.keys()][-1]
    new_digit_id = int(last_id.split('user-0000')[-1])+1
    new_user_id = f"user-0000{new_digit_id}"

    Users[new_user_id] = {'first-name': first_name,
                    'last-name': last_name,
                    'username': username,
                    'email': email,
                    'password': password
                                            }

    session.permanent = True

    session["user_id"] = new_user_id
    session["user_first_name"] = first_name

    return redirect(url_for('main.home'))

@accs_bp.route('/signin')
def signin_page():
    pass

@accs_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('main.home'))

@accs_bp.route('/dashboard')
def account():
    return render_template('pass.html')
