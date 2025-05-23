"""
A Associação mostra que duas classes podem funcionar de forma associada sem depender totalmente
uma da outra.
"""

class Mago:

    def __init__(self,nome):
        self.__nome = nome
        self.__poder = None
        self.__efeito = None

    # =========Getters==========
    @property
    def nome(self):
        return self.__nome

    @property
    def poder(self):
        return self.__poder

    @property
    def efeito(self):
        return self.__efeito

    # ==========Setters==========
    @poder.setter
    def poder(self,entrada):
        self.__poder = entrada

    @efeito.setter
    def efeito(self, entrada):
        self.__efeito = entrada

class Elemento:
    def __init__(self,elemento):
        self.__elemento = elemento

    # =========Getters==========
    @property
    def elemento(self):
        return self.__elemento

class Magia:
    def __init__(self,tipo):
        self.__tipo = tipo

    # =========Getters==========
    @property
    def tipo(self):
        return self.__tipo


import Modulos.ncores as ncores
# from associacao1_poo import Mago, Elemento, Magia

# Instânciando objetos e definindo valor dos atributos
mago_fogo = Mago('Firônio')
tipo_elemento = Elemento('Fogo')
tipo_magia = Magia('Explosão')

mago_gelo = Mago('Gelônio')
tipo_elemento2 = Elemento('Gelo')
tipo_magia2 = Magia('Espinhos')

# Atributo poder recebe tudo que contem dentro da classe Elemento, isso cria uma relação entre classes.
# Atributo efeito recebe tudo que contem dentro da classe Magias, isso cria uma relação entre classes.
mago_fogo.poder = tipo_elemento
mago_fogo.efeito = tipo_magia

# Atributo poder recebe diretamente o retorno do metodo "elemento". Isso cria uma relação entre classes.
# Atributo efeito recebe diretamente o retorno do metodo "tipo". Isso cria uma relação entre classes.
mago_gelo.poder = tipo_elemento2.elemento
mago_gelo.efeito = tipo_magia2.tipo

# Mostrando dados sem precisar acessar a classe Elemento ou Magias diretamente.
print(f'Mago {ncores.red}{mago_fogo.nome}{ncores.reset} tem a habilidade de lançar magias de {ncores.red}{mago_fogo.efeito.tipo}{ncores.reset} do elemento {ncores.red}{mago_fogo.poder.elemento}{ncores.reset}')
print(f'Mago {ncores.blue}{mago_gelo.nome}{ncores.reset} tem a habilidade de lançar magias de {ncores.blue}{mago_gelo.efeito}{ncores.reset} do elemento {ncores.blue}{mago_gelo.poder}{ncores.reset}')

