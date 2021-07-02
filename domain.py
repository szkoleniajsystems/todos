class Author:
    '''Obiekt tej klasy jest przesylany do widoku /about'''
    first_name=None
    last_name=None
    email=None
    pic_url=None
    def __init__(self,fn,ln,e,pu):
        self.first_name=fn
        self.last_name=ln
        self.email=e
        self.pic_url=pu

class ToDo:
    todo_id=None
    todo_name=None
    todo_description=None
    todo_priority=None
    def __init__(self,id,n,d,p):
        self.todo_id=id
        self.todo_name=n
        self.todo_description=d
        self.todo_priority=p
