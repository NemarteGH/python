import Modulos.ncores as ncores

"""
método/atributo Público (Comum sem proteção ou mensagens)
__método/atributo Privado (Onde por convenção tem um underline no inicio mostrando que o método/atributo não deve ser alterado/acessado/modificado.)
_método/atributo Protegido (Onde por convenção tem dois underlines, refornçando que esse método/atributo não deve de maneira alguma ser modificado/alterado/acessado. O python só permite isso se feito utilizando "_nomedaclasse__nomedoatributoou".)
"""

class Database:

    def __init__(self):
        self.dados = {} # Atributo de instância público
        self._criado = 'Criada em 28 de Julho de 2025' # Atributo de instância privado
        self.__empresa = 'Tungstênio ltda' # Atributo de instância protegido

    def addclient(self,ide,nome): # Metodo de instância público
        if 'Clientes' not in self.dados:
            self.dados['Clientes'] = {ide : nome}
            print(f'{ncores.green}Cliente Criado ==> {ncores.reset}{self.dados['Clientes'][ide]}')
        else:
            self.dados['Clientes'].update({ide:nome})
            print(f'{ncores.green}Cliente Criado ==> {ncores.reset}{self.dados['Clientes'][ide]}')

    def _removeclient(self,ide): # Metodo de instância privado
        print(f'{ncores.red}Cliente removido ==> {ncores.reset}{self.dados['Clientes'][ide]}')
        del self.dados['Clientes'][ide]

    def __listacliente(self): # Metodo de instância protegido
        print(15 * f'{ncores.italic}-=')
        for a,b in self.dados['Clientes'].items():
            print (f'{a} | {b} | {self.__empresa}')
        print(15 * '-=')

mydb = Database() # Instanciando o objeto
mydb.addclient(1,'Mauro') # Criando cliente com metodo público (Python não mostra nenhum erro ou mensagem, nem apresenta nenhuma barreira de proteção já que o metodo é público.)
mydb.addclient(2,'Lucas') # Criando cliente com metodo público (Python não mostra nenhum erro ou mensagem, nem apresenta nenhuma barreira de proteção já que o metodo é público.)
mydb.addclient(3,'Gabriel') # Criando cliente com metodo público (Python não mostra nenhum erro ou mensagem, nem apresenta nenhuma barreira de proteção já que o metodo é público.)
mydb._removeclient(1) # Removendo cliente com metodo protegido (Python oculta parcialmente o metodo e recomenda não fazer isso)
mydb._Database__listacliente() # Listando clientes com metodo privado (Python recomenda não fazer isso e só permite com quando usamos uma sintaxe diferente apontando o nome da classe e o nome do metodo "_Classe__metodo-privado").
print(mydb._criado) # Acessando atributo protegido
print(mydb._Database__empresa) # Acessando atributo privado

"""
Em resumo, o encapsulamento serve para "proteger" partes do código para que não sejam editadas/acessadas de forma 
errada por outros desenvolvedores ou por você mesmo. Quando um desenvolvedor vê uma variavel com underline no começo,
ele já entende que é algo que não deve ser alterado/acessado diretamente pois pode atrapalhar todo o funcionamento do 
código.
"""