
class globalStorage:
    def __init__(self):
        self.default_id = 'user-00001'
        self.lists = {self.default_id : [
            {'id':1, 'title':'Add Context', 'detail':'Add context to discord bot ai chat with name of server, etc.', 'status':'complete', 'deadline':'22/12/2026'},
            {'id':2, 'title':'Edit System Prompt', 'detail':'Make system prompt a constant variable', 'status':'pending', 'deadline':'22/11/2026'},
                 ]
            }
        self.users = {
                    self.default_id : {'first-name': "User",
                                    'last-name': "LastName",
                                    'username': 'fd8f8g88ds9fs98gjhs89f0h09j0sgg9h-0j98sa97',
                                    'email': 'jotextech@gmail.com',
                                    'password': 'NewJoe@2009'
                                }
                    }
TodoList = globalStorage().lists
Users = globalStorage().users
df_id = globalStorage().default_id