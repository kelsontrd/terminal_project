from re import I
import requests

def get_game(id=""):

    if id != "" and not int(id):
        return {"error": "id deve ser um numero"}

    url = f"https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil/{id}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Sorteio não encontrado"}
    
    return response.json()