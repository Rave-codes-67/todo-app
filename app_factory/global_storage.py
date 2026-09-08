
class globalStorage:
    def __init__(self):
        self.lists = {'user-00001' : [
            {'id':1, 'title':'Add Context', 'detail':'Add context to discord bot ai chat with name of server, etc.', 'status':'complete', 'deadline':'22/12/2026'},
            {'id':2, 'title':'Edit System Prompt', 'detail':'Make system prompt a constant variable', 'status':'pending', 'deadline':'22/11/2026'},
                 ]
            }
        self.users = {
                    "user-00001": {'first-name': "Joseph",
                                    'last-name': "Paul",
                                    'username': 'Rave-2009',
                                    'email': 'jotextech@gmail.com',
                                    'password': 'NewJoe@2009'
                                }
                    }
TodoList = globalStorage().lists
Users = globalStorage().users