import sqlite3
from pprint import pprint

from telebot import conf, telegram
from telebot.db import SQL
from telebot.models import Message, Update 
from dolar_Response import get_chatid_and_Send_Dolar_Response

options = conf.open_env()
# print(options) # debug
token = options["TELEGRAM_TOKEN"]
db_name = options.get("DBFILE", "telegram.db")
db = SQL(db_name)

db.setup_db([Update.table, Message.table])

def get_updates():
    """ A wrapper que envuelve la funcionalidad
    de obtener updates desde telegram
    """
    updates = telegram.get_updates(token)
    for _upt in updates:
        update = Update(db)
        try:
            update.add(_upt["update_id"])
            telegram.register_message(db, _upt["message"], token)
        except sqlite3.IntegrityError:
            print("Update ya registrado")

        # pprint(_upt) # debug


def register_message():
    """"
    CONSIGNA 1
    Esta funcion NO llama al modulo telegram.register_message para agregar un mensaje a la db.
    Crea objetos updates y msg desde este mismo modulo. Para registrar los mensajes hubo que modificar "models"
     y agregar INSERT or IGNORE a la sql query   

     Filtra mensajes con texto y excluye los que tienen foto con la funcion telegram.check_if_photo_in
 
        """
  
   
    
        
    updates=telegram.get_updates(token)
    updates_List=[]
    for _upt in updates:
        isPhoto=telegram.check_if_photo_in(_upt)
        if isPhoto is False:
            updates_List.append(_upt)
            update=Update(db)
            msg=Message(db)
            
            try:
                update.add(_upt["update_id"])
                breakpoint()
                msg.add(_upt["message"]["chat"]["id"], _upt["message"]["message_id"], _upt["message"]["text"]) #almacenar en variables para hacerlo mas leible
            
            except sqlite3.IntegrityError:
                print("Update registrado")
        else: 
            continue




def get_updates_Offset():
    """
    CONSIGNA 2
    Llama al modulo Telegram donde esta definida la funcion correspondiente.
    """
    telegram.get_updates_Offset(token, db)

def dolar_Response():
    """"
    CONSIGNA 4. Obtiene chatid y recoge mensajes "dolar oficial" o "dolar blue" en el cuerpo del message.
    Si estos strings estan presentes, envía una respuesta con precio de dolar correspondiente.
    """
    get_chatid_and_Send_Dolar_Response(token)




def check_if_photo(token):
    """
    CONSIGNA 3: Si hay photo en el cuerpo de la response, envía un mensaje de rechazo:
    """
 
    isphoto=telegram.check_if_photo(token)
    if isphoto:
        reject_message="Formato no soportado. Por favor enviar solo texto"
        chat_id=telegram.get_chatid(token)
        telegram.send_message(reject_message, chat_id, token)














