from flask import Blueprint, session, redirect, url_for, jsonify, render_template, request

todo_bp = Blueprint('todo', __name__)

from app_factory.global_storage import TodoList

"""
    id = unique id for each user for accessing notes
    title = Title of Task todo
    detail = Detail of Task todo
    status = Status of Task (pending, complete, overtime)
    deadline = Date and time to finish/do task
"""
app = todo_bp

@app.route('/signin')
def signin_page():
    pass

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('app_factory.routes.main.home'))

@app.route('/dashboard')
def account():
    return render_template('pass.html')

@app.route('/new-todo', methods=["POST"])
def new_todo():
    pass

@app.route('/delete_todo', methods=['POST'])
def delete_todo():
    target_id = request.form.get('id')
    global TodoList
    TodoList = [todo for todo in TodoList if todo['id'] != target_id ]


@app.route('/update-status', methods=['POST'])
def inlineChangeStatus():
    statuses = ['pending', 'complete', 'overtime']
    data = request.get_json()
    task_id = int(data.get('id'))
    task_status = data.get('status')
    if 'user_id' in session:
        TodoList.get(session.get('user_id'), [])

    if task_status == statuses[0]:
        task_status = statuses[1]
    elif task_status == statuses[1]:
        task_status = statuses[2]
    elif task_status == statuses[2]:
        task_status = statuses[0]
    else:
        task_status = task_status


    return jsonify({
        "success": True,
        "new_status": TodoList[task_id]['status']
    })