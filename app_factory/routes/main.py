from flask import Blueprint, render_template, jsonify, request, url_for, redirect, session
from app_factory.global_storage import TodoList

main_bp = Blueprint('main', __name__)

WELCOME_MSGS = [
    'What are your plans for today?',
    'What do you want to do today?',
    'Start tracking your tasks!!',
    'Plan your tasks before you forget..',
    'Stay Disciplined. Write them down'
]


import time, random
@main_bp.route('/')
def home():
    current_time = int(time.strftime("%H"))
    greeting = 'Good Day'
    if current_time <= 3:
        greeting = "Night Owl"
    elif current_time <= 11:
        greeting = 'Good Morning'
    elif current_time <= 16:
        greeting = 'Good Afternoon'
    elif current_time <= 24:
        greeting = 'Good Evening'

    global WELCOME_MSGS
    wlc_msg = random.choice(WELCOME_MSGS)

    if "user_id" in session:
        first_name = session.get("user_first_name")

        user_id = session.get("user_id", None)
        todo_lists = TodoList.get(user_id, [])

        return render_template(
             'index.html',
             f_name=first_name,
             greeting=greeting,
             lists=todo_lists,
             wlc_msg=wlc_msg,
             logged_in=True)
    else:
        return render_template('index.html', f_name="User", greeting=greeting, lists=TodoList.get('user-00001'), wlc_msg=wlc_msg, logged_in=False)
