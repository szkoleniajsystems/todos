import psycopg2 as pg
from domain import *
connection_kwargs={
    "host": "localhost",
    "port":5432,
    "database": "szkolenie",
    "user": "szkolenie",
    "password": "jsystems"
}

def get_author():
    a=Author('Andrzej','Klusiewicz','klusiewicz@jsystems.pl','https://bi.im-g.pl/im/3a/0a/16/z23110714V,Arnold-Schwarzenegger-w-1974-roku.jpg')
    return a

def get_todos():
    wynik=[]
    with pg.connect(**connection_kwargs) as connection:
        cursor = connection.cursor()
        cursor.execute('select * from todos order by todo_priority desc')
        for w in cursor:
            t=ToDo(w[0],w[1],w[2],w[3])
            wynik.append(t)
    return wynik


def get_todo(id):
    with pg.connect(**connection_kwargs) as connection:
        cursor = connection.cursor()
        cursor.execute(f'select * from todos where todo_id={id}')
        w=cursor.fetchone()
        print(w)
        t=ToDo(w[0],w[1],w[2],w[3])
        return t


def save_todo(t):
    with pg.connect(**connection_kwargs) as connection:
        cursor=connection.cursor()
        cursor.execute(f"insert into todos(todo_name,todo_description,todo_priority) values ('{t.todo_name}','{t.todo_description}',{t.todo_priority})")
        connection.commit()
