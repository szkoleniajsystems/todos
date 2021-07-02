from domain import *

def get_author():
    a=Author('Andrzej','Klusiewicz','klusiewicz@jsystems.pl','https://bi.im-g.pl/im/3a/0a/16/z23110714V,Arnold-Schwarzenegger-w-1974-roku.jpg')
    return a

def get_todos():
    wynik=[]
    wynik.append(ToDo(1,'Kopsnąć się po piwo','Piątek, piąteczek, piątunio',3)  )
    wynik.append(ToDo(2, 'Zamówić pizzę', 'Piątek, piąteczek, piątunio', 2))
    wynik.append(ToDo(2, 'Otworzyć Whiskey', 'Piątek, piąteczek, piątunio', 1))
    return wynik
