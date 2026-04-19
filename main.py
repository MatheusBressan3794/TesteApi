import requests 
import pprint

api_key = ""#chave de acesso da api
link_api = "http://api.weatherapi.com/v1/current.json"#link http da api

parametros = { #parametros para usar essa função da api
    "key": api_key,
    "q": "Araras",
    "lang": "pt"
}

respostas = requests.get(link_api, parametros) #pega informações da api

if respostas.status_code == 200:
    dados_requisicao = respostas.json()
   # pprint.pprint(dados_requisicao) organiza o print pra localizar a informação que você quer

    temperatura = dados_requisicao["current"]["temp_c"]
    descricao = dados_requisicao["current"]["condition"]["text"]

    print("A temperatura é:",temperatura,"ºC")
    print(descricao)