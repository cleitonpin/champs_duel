from configs import bd
import sys
import os
import time
from models import users_model as Users

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_list():
    
    print('\n## COMANDOS ##\n\n@entrartor + [ID]\n@sair')

def list_tournament():
    
    bd.cursor.execute("SELECT id,name,category,room FROM tournament")
    lists = bd.cursor.fetchall()
    print(lists[0])
    tor  = True
    while tor == True:

        if Users.status == 'logged':
            cls()
            cont = 0
             
            print("ID   NOME    \u200b\u200bCATEGORIA      \u200b\u200bSALA\n")
            
            for cont in lists:
                print(f'{cont[0]}    {cont[1]}    \u200b\u200b{cont[2]}         \u200b\u200b{cont[3]}')
            
            menu_list()
            #print(lists[0][0])
            find = input("\ninforme um comando [@comando] =>  ")
           

            if find == '@sair':
                tor = False
   



        # bd.cursor.execute("SELECT name,id,category FROM tournament where name ilike %s", (find,))
        # search = bd.cursor.rowcount
    
    # if search > 0:
    #     
    #     enter_tournament = input('informe um comando [@comando] => ')
    #     if enter_tournament == '@entrar 1':
    #         print('idjwyhw')
    # else:
    #     print('dont exist')

        

