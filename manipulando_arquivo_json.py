#manipular json

import json 

import urllib.request


cadastro_pessoas = {
    "1": {
        "Nome": "Joao",
        "Idade": 35,
        "Sexo": "Masculino",
        "Data Nascimento": "29/12/1985"
    },
    "2": {
        "Nome": "Juca",
        "Idade": 34,
        "Sexo": "Masculino",
        "Data Nascimento": "12/12/1985"
    },
    "3": {
        "Nome": "Leandro",
        "Idade": 50,
        "Sexo": "Masculino",
        "Data Nascimento": "01/01/1970"
    },
    "4": {
        "Nome": "Rita",
        "Idade": 23,
        "Sexo": "Feminino",
        "Data Nascimento": "12/09/1997"
    }
}

for c,v in cadastro_pessoas.items():
    print(c,v)

#converter dicionario - json + manipulação

dados = json.dumps(cadastro_pessoas,indent=4)

with open('arquivos/pessoas.json','w+') as j:
    json.dump(cadastro_pessoas,j, indent=4)

#abrir arquivo json loads para dicionario

with open('arquivos/pessoas.json','r') as f:
    le_json = json.load(f)
    print(le_json)

    for v in le_json.keys():
        print(v)

##### manipulação com internet

url = 'http://api.open-notify.org/astros.json'

pega_json = urllib.request.urlopen(url).read().decode()

#Converter esse dado em dicionario

dic_json = json.loads(pega_json)

for c in dic_json.values():
    print(c)

print(dic_json)

for p in dic_json['people']:
    print(p['name']) #Aqui esta com um filtro

#criar um arquivo com dados capiturados

with open('arquivos/astros.json','w+')as f:
    json.dump(dic_json,f,indent=4)
