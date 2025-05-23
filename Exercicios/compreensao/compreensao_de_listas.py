# Dados de exemplo
dados1 = ['Maria', 'Luciana']
dados2 = [1,2,3,4,5,6,7,8,9]
dados3 = (('chave','valor'),('chave2','valor2'))

# Compreensão de lista
lista1 = [variavel *2 for variavel in dados2] # Operação simples
lista2 = [variavel - 1 for variavel in dados2] # Operação simples
lista3 = [(variavel,variavel2) for variavel in dados2 for variavel2 in range(2)] # Iterando sobre cada valor
lista4 = [v.replace('a','@') for v in dados1] # Substituindo letras
lista5 = [(valor,chave) for chave,valor in dados3] # Trocando de posição
lista6 = [v for v in range(0,100) if v % 2 == 0 if v < 50] # Apresenta 2 condições que são verificadas uma após a outra
lista7 = [v if v % 2 == 0 else 'impar' for v in range(0,100)] # Usando if e else juntos
lista8 = [v if v % 2 == 1 and v < 30 else 'par' for v in range(1,100)] # Usando if com and e else

# Mostra saida da compreensão
print(lista8)