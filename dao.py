import psycopg2 as pg
from domain import *

def get_author():
    a=Author('Andrzej','Klusiewicz','klusiewicz@jsystems.pl','https://bi.im-g.pl/im/3a/0a/16/z23110714V,Arnold-Schwarzenegger-w-1974-roku.jpg')
    return a

def get_todos():
    wynik=[]
    with pg.connect(host="localhost", port=5432, database="szkolenie", user="szkolenie",
                    password="jsystems") as connection:
        cursor = connection.cursor()
        cursor.execute('select * from todos order by todo_priority desc')
        for w in cursor:
            t=ToDo(w[0],w[1],w[2],w[3])
            wynik.append(t)
    return wynik


def get_todo(id):
    with pg.connect(host="localhost", port=5432, database="szkolenie", user="szkolenie",
                    password="jsystems") as connection:
        cursor = connection.cursor()
        cursor.execute(f'select * from todos where todo_id={id}')
        w=cursor.fetchone()
        print(w)
        t=ToDo(w[0],w[1],w[2],w[3])
        return t
    #return ToDo(1,'Jakieś zadanie przykładowe','opis który może być bardzo długi ale nie musi',2)

get_todo(1)
#przerwa do 14:48