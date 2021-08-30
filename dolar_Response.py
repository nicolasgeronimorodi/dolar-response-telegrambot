from telebot import telegram, conf
import dolarsi

options = conf.open_env()
token = options["TELEGRAM_TOKEN"]


def get_chatid_and_Send_Dolar_Response(tkn):
    """"
    CONSIGNA 4
    Esta funcion
    la usamos para obtener el chat id de un mensaje y enviar una respuesta con cotizacion del dolar
    
     """
    result_Data = telegram.get_updates(token) #result_Data es una lista y cada result es un diccionario que en JSON de firefox son los elementos 0,1,2 etc
    for result in result_Data:
        
        result_message_Data=result["message"]#-> tipo diccionario
        
        chat_Data=result_message_Data["chat"]
        chatid=chat_Data["id"]
        #print(chatid)
        message_Info=result["message"]
        breakpoint()
        message_Info_keys=message_Info.keys()
        if "text" in message_Info_keys:
            message_Text_info=message_Info["text"]
            if "dolar oficial" in message_Text_info:

        
                try:
                    
                    dolar=dolarsi.Dolar()
                    oficial_Compra=dolar.get_oficial_Compra()
                    oficial_Venta=dolar.get_oficial_Venta()
                    message=f"El DOLAR OFICIAL cuesta ${oficial_Compra} para la Compra y ${oficial_Venta} para la venta"
                    telegram.send_message(message, chatid, token)
                except KeyError:
                    print("Problemas en la ejecucion")
            if "dolar blue" in message_Text_info:
                try:
                    dolar=dolarsi.Dolar()
                    blue_Compra=dolar.get_blue_Compra()
                    blue_Venta=dolar.get_blue_Venta()
                    message=f"El DOLAR BLUE cuesta ${blue_Compra} para la Compra y ${blue_Venta} para la venta"
                    telegram.send_message(message, chatid, token)
                except KeyError:
                    print("Problemas en la ejecucion")
        else:
            continue
