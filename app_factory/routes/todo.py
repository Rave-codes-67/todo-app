from flask import Blueprint, session, redirect, url_for, jsonify, render_template, request

todo_bp = Blueprint('todo', __name__)

from app_factory.global_storage import TodoList, df_id

"""
    id = unique id for each user for accessing notes
    title = Title of Task todo
    detail = Detail of Task todo
    status = Status of Task (pending, complete, overtime)
    deadline = Date and time to finish/do task
"""

def get_id():
    return session.get('user_id')

@todo_bp.route('/new-todo', methods=["GET", "POST"])
def new_todo():
    if request.method == 'GET':
        return
    data = request.form
    title = data.get('title')
    detail = data.get('details')
    deadline = data.get('deadline')
    status = data.get('status')
    # Check if 'user_id' is in session to decide whether user is signed in to know where to save it
    if 'user_id' in session:
        # Get the user id and use it to get the last id from database then add 1 to it to make the new id
        # And if there's no existing todo; set the id to 1
        id = TodoList[get_id()][-1]['id']+1 if len(TodoList[get_id()]) > 1 else 1
        TodoList[get_id()].append({'id': id, 'title': title, 'detail': detail, 'status': status, 'deadline': deadline})
    else:
        # If user is not signed in, Just add it to the default template todo
        id = TodoList[df_id][-1]['id']+1 if len(TodoList[df_id]) > 1 else 1
        TodoList[df_id].append({'id': id, 'title': title, 'detail': detail, 'status': status, 'deadline': deadline})


@todo_bp.route('/delete_todo', methods=['POST'])
def delete_todo():
    target_id = request.form.get('id')
    global TodoList
    TodoList = [todo for todo in TodoList if todo['id'] != target_id ]


@todo_bp.route('/update-status', methods=['POST'])
def inlineChangeStatus():
    statuses = ['pending', 'complete', 'overtime']
    data = request.get_json()
    task_id = int(data.get('id'))
    task_status = data.get('status')

    if task_status == statuses[0]:
        new_status = statuses[1]
    elif task_status == statuses[1]:
        new_status = statuses[2]
    elif task_status == statuses[2]:
        new_status = statuses[0]
    else:
        new_status = task_status


    lists = []
    if 'user_id' in session:
        lists = TodoList.get(get_id())
    else:
        lists = TodoList.get(df_id)

    for item in lists:
        if item['id'] == task_id:
            item['status'] = new_status
            break
                
    return jsonify({
        "success": True,
        "new_status": new_status
    })
