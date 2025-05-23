# Abre o arquivo para ediçao, caso não exista é criado
with open("arquivoteste.txt","a+") as cadastro:
    nome = input("Nome: ")
    idade = input("Idade: ")
    sexo = input("Sexo: ")

    cadastro.write(f"nome:{nome}\n")
    cadastro.write(f"idade:{idade}\n")
    cadastro.write(f"sexo:{sexo}\n")

# Abre o arquivo para leitura
with open("arquivoteste.txt","r") as cadastro:
    print(20*"-")
    print(cadastro.read())
    print(20 * "-")

# Puxa dados do arquivo e cria um dicionário organizado
clientes = {}
with open("arquivoteste.txt","r") as cadastro:
    lista = []
    for i in cadastro.readlines():
        lista.append(i.split("\n")[0])

    for c in range(0,len(lista),3):
        clientes.update({
            lista[c:c+3][0].split(":")[1]:{
                lista[c:c+3][0].split(":")[0]:lista[c:c+3][0].split(":")[1],
                lista[c:c+3][1].split(":")[0]:lista[c:c+3][1].split(":")[1],
                lista[c:c+3][2].split(":")[0]:lista[c:c+3][2].split(":")[1]}
        })

print(clientes["Marcus"])
print(clientes["Lucas"])
print(clientes["Marcela"])





