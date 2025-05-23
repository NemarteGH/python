"""
A agregação mostra que duas classes podem existir
separadamente, mas só funcionam corretamente quando executadas em conjunto.
"""

class Carrinho:
    def __init__(self):
        self.produtos = [] # 2. Objeto da classe Produto é inserido na lista

    def addproduto(self, produto): # 1. Objeto da classe Produto chega aqui
        self.produtos.append(produto)

    def listaprodutos(self): # 3. Objeto da classe Produto é listado usando próprios atributos.
        for prod in self.produtos:
            print (f'{prod.item} | {prod.preco}')  # 4. Não existe atributo "item" ou "preco" na classe Carrinho, mesmo assim conseguimos usalos, pois recebemos um objeto da classe Produto que possui tais atributos.

class Produto:
    def __init__(self,item,preco):
        self.item = item
        self.preco = preco

# from agregação1_poo import Produto, Carrinho

# Instanciando carrinho.
cart = Carrinho()

# Instanciando produtos
produto1 = Produto('Maça',1.99)
produto2 = Produto('Banana',2.99)
produto3 = Produto('Tomate',1.25)
produto4 = Produto('Uva',7.00)

# Enviando o objeto para outra classe atraves do metodo addproduto
# Os objetos vão nesse formato "<agregação1_poo.Produto object at 0x000002602BCC4B90>"
# Esses objetos são acompanhados de todos os seus atributos
cart.addproduto(produto1)
cart.addproduto(produto2)
cart.addproduto(produto3)
cart.addproduto(produto4)

# Listando produtos
cart.listaprodutos()