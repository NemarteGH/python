import json

dados = {
    "nome": "Roberto",
    "idade": "19",
    "sexo": "Masculino",
    "status": "Ativo"
}

with open("jasonfile.json","w") as jsonfile: # Converte dicionário em json e grava no arquivo
    jsonfile.write(json.dumps(dados,sort_keys=True,indent=4))

with open("jasonfile.json","r") as jsonfile: # Converte dicionário em json e mostra de forma organizada
    print(json.dumps(dados,sort_keys=True, indent=4))

with open("jasonfile.json","r") as jsonf: # Converte arquivo json em dicionário e mostra o dicionário
    novosdados = json.load(jsonf)
    print(novosdados)

with open("jasonfile.json","r") as fil:
    print(json.load(fil))
