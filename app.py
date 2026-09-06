from flask import Flask, render_template, request

app = Flask(__name__)

TODO_LIST = [
    {'id':1, 'title':'Add Context', 'detail':'Add context to discord bot ai chat with name of server, etc.', 'status':'complete', 'deadline':'22/12/2026'},
    {'id':2, 'title':'Edit System Prompt', 'detail':'Make system prompt a constant variable', 'status':'pending', 'deadline':'22/11/2026'},
]

WELCOME_MSGS = [
    'What are your plans for today?',
    'What do you want to do today?',
    'Start tracking your tasks!!',
    'Plan your tasks before you forget..',
    'Stay Disciplined. Write them down'
]

"""
    id = unique id for each user for accessing notes
    title = Title of Task todo
    detail = Detail of Task todo
    status = Status of Task (complete, pending, overtime)
    deadline = Date and time to finish/do task
"""

LoggedIn = False
FirstName = 'Joseph'

import time, random
@app.route("/", methods=['GET'])
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

    return render_template('index.html', f_name=FirstName, greeting=greeting, lists=TODO_LIST, wlc_msg=wlc_msg)

tasks_bp = app
@tasks_bp.route('/create', methods=["POST"])
def new_todo():
    global TODO_LIST
    id = TODO_LIST[-1]['id']+1

@tasks_bp.route('/', methods=["POST"])
def edit_todo():
    id = request.form.get('')

@tasks_bp.route('/', methods=["POST"])
def change_status():
    pass

@app.route('/delete_todo', methods=['POST'])
def delete_todo():
    target_id = request.form.get('id')
    global TODO_LIST
    TODO_LIST = [todo for todo in TODO_LIST if todo['id'] != target_id ]



@app.route('/signup')
def signup_page():
    return render_template('signup-page.html')

@app.route('/signin')
def signin_page():
    pass

@app.route('/Account')
def account():
    return render_template('pass.html')

if __name__ == "__main__":
    app.run(debug=True)
