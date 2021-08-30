import requests
class Dolar:

    def get_oficial_Compra(self):
        rsp=requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        json_Dolar=rsp.json()
        oficial_Data=json_Dolar[0]["casa"]
        oficial_Compra=oficial_Data["compra"]
        return oficial_Compra
    def get_oficial_Venta(self):
        rsp=requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        json_Dolar=rsp.json()
        oficial_Data=json_Dolar[0]["casa"]
        oficial_Venta=oficial_Data["venta"]
        return oficial_Venta
    def get_blue_Compra(self):
        rsp=requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        json_Dolar=rsp.json()
        dolar_blue_Data=json_Dolar[1]["casa"]
        dolar_blue_compra=dolar_blue_Data["compra"]
        return dolar_blue_compra
    def get_blue_Venta(self):
        rsp=requests.get("https://www.dolarsi.com/api/api.php?type=dolar")
        json_Dolar=rsp.json()
        dolar_blue_Data=json_Dolar[1]["casa"]
        dolar_blue_Venta=dolar_blue_Data["venta"]
        return dolar_blue_Venta     