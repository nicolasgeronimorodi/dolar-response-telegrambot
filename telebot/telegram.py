import logging
from pprint import pprint
import sqlite3

import requests

from telebot.db import SQL
from telebot.models import Message, Update
####



def send_message(msg, chatid, token):
    """ Manda mensaje a un usuario 

    token: es lo que debe estar en el .env
    """
    assert type(chatid) == int
    assert type(msg) == str
    assert type(token) == str

    BASE_URL = f"https://api.telegram.org/bot{token}"
    fullmsg = f"sendMessage?text={msg}&chat_id={chatid}"
    # query params
    rsp = requests.get(f"{BASE_URL}/{fullmsg}")
    logging.debug("Message sent %s", rsp.text)


def get_chat_id(username, token):
    """ have pull en base a un username 
    token: es lo que debe estar en el .env
    """

    BASE_URL = f"https://api.telegram.org/bot{token}"
    rsp = requests.get(f"{BASE_URL}/getUpdates")
    for r in rsp.json()["result"]:
        msg = r.get("message")
        if msg["from"]["username"] == username:
            id_ = msg["chat"]["id"]
            print(f"Chatid is: {id_}")
            return


def get_updates(token):
    """ Obtiene todos los mensajes desde telegram
    API information: https://core.telegram.org/bots/api#getupdates
    Ejemplo de rsp.json()["result"]:
    [
    {'message': {'chat': {'first_name': 'Xavier',
                        'id': 222,
                        'last_name': 'Petit',
                        'type': 'private',
                        'username': 'xpetit'},
                'date': 1628086187,
                'from': {'first_name': 'Xavier',
                        'id': 3333,
                        'is_bot': False,
                        'language_code': 'en',
                        'last_name': 'Petit',
                        'username': 'xpetit'},
                'message_id': 7,
                'text': 'pepe'},
    'update_id': 478400752},
    ...
    ...
    ]
    """
    BASE_URL = f"https://api.telegram.org/bot{token}"
    rsp = requests.get(f"{BASE_URL}/getUpdates")

    # pprint(rsp.json()["result"]) # debug

    return rsp.json()["result"]


def register_message(sql: SQL, data, tkn):
    """
    Recibe un mensaje, lo guarda en la base y envia 
    un response.
    {'chat': {'first_name': 'Xavier',
                      'id': 44444,
                      'last_name': 'Petit',
                      'type': 'private',
                      'username': 'xpetit'
             },
     'date': 1628087051,
     'from': {'first_name': 'Xavier',
                      'id': 4444,
                      'is_bot': False,
                      'language_code': 'en',
                      'last_name': 'Petit',
                      'username': 'xpetit'},
     'message_id': 15,
     'text': 'dame info'}


     CONSIGNA 1: Se removió la ejecucion de la funcion send_message
    """
    msg = Message(sql)
    msg.add(data["chat"]["id"], data["message_id"], data["text"])


#########################################################################################
def get_updates_Offset(token, sql: SQL):
    """
   CONSIGNA2:
    Se vale de un objeto de Update y el metodo (nuevo) last_update para obtener el ultimo update y utilizarlo como OFFSET
    de la request
    """
    update=Update(sql)
    offset=update.last_update()
    BASE_URL = f"https://api.telegram.org/bot{token}"
    rsp = requests.get(f"{BASE_URL}/getUpdates?offset={offset}")
    print(rsp.json()["result"])




def get_chatid(token):
    """
    Codigo factoreado en base a modulo dolar_Response.get_chatid_and_Send_Dolar_Response
    No es el mismo de arriba que venía ya resuelto de antemano.
    """
    result_Data = get_updates(token)
    for result in result_Data:
        result_message_Data=result["message"]
        #breakpoint()
        chat_Data=result_message_Data["chat"]
        chatid=chat_Data["id"]
        return chatid




def check_if_photo(token):

    """"
    CONSIGNA 3: Chequea si hay foto la response de getUpdates. Esta funcion es llamada en modulo main  
    """
    result_Data=get_updates(token)
    for res in result_Data:
        message_data=res["message"]
        message_data_keys=message_data.keys()
        if "photo" in message_data_keys:
            isphoto=True
            
        else:
            isphoto=False
        return isphoto

def check_if_photo_in(update):
    """
    CONSIGNA 1. Usado en main.register_message. Similar a la funcion de arriba pero esta analiza cada update del cuerpo de updates
    """
    message_data=update["message"]
    message_data_keys=message_data.keys()
    if "photo" in message_data_keys:
            isphoto=True
    else:
        isphoto=False
    return isphoto



            




















