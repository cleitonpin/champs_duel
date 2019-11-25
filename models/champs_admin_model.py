#@@@ IMPORTS @@@
from configs import bd
from datetime import datetime
import time
from views import design_view


def create_tournament():
    created_at = datetime.today()

    name_tournament = input('Nome do torneio => ')
    type_tournament = input('Diga o tipo de torneio que deseja criar => ')
    category_tournament = input('Categoria do torneio => ')
    description = input('Descrição do torneio => ')
    participants = 0
    room_ = input('A sala será aberta ou fechada? ')
    
    if room_ == 'fechada':
        password_room_tournment = input('Insira a senha do torneio => ')
    
        bd.cursor.execute("""
        INSERT INTO tournament(name,category,room,password_tournament,type_tournament,description,created_at,participants)
        values (%s,%s,%s,%s,%s,%s,%s,%s)
        """, (name_tournament, category_tournament,room_.upper(),password_room_tournment, type_tournament, description, created_at,participants))
        bd.connection.commit()

        print('Torneio registrado.')
        time.sleep(1)
        design_view.clear()
        design_view.designLogged()
    elif room_ == 'aberta':
    
        bd.cursor.execute("""
        INSERT INTO tournament(name,category,room,type_tournament,description,created_at,participants)
        values (%s,%s,%s,%s,%s,%s,%s)
        """, (name_tournament, category_tournament, room_.upper(),type_tournament, description, created_at, participants))
        bd.connection.commit()

        print('Torneio registrado.')
        time.sleep(1)
        design_view.clear()
        design_view.designLogged()
    
        




