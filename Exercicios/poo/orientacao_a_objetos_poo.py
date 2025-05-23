
class Pessoa:

    empresa = 'Classic Móveis ltda'

    def __init__(self, nome, idade, cor, cargo='', status='Ativo', salario=None):

        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.cargo = cargo
        self.status = status
        self._salario = salario

        print(19*"▬▬▬")
        print(f"Usuário cadastrado na empresa: ++ {self.empresa} ++")
        print(19*"▬▬▬")

    def aumento_salarial (self,qtd):
        self._salario += qtd
        return self._salario

    def promover(self,novocargo):
        self.cargo = novocargo
        return f"{self.cargo} ==>Cargo Atualizado<=="

    def demitir(self):
        self.status = 'Demitido'

    @classmethod
    def mudarcompania (cls,novacompania):
        cls.empresa = novacompania
        return f"Empresa alterada para [+]{novacompania}[+]"

    @staticmethod
    def geraid():
        return __import__('random').randint(10000,20000)


    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self,valor_de_salario):
        if isinstance(valor_de_salario, str):
            self.salario = "++++ Sálario Não pode ser string ++++"
        else:
            self.salario = valor_de_salario

victoria = Pessoa('Victória',23, 'Branca','Atendente',salario=1400)
mario = Pessoa('Mário',34,'Pardo','Recepcionista',salario=1.500)

print(f'Atributo de instância ===> {mario.cargo}')
print(f'Atributo de classe ===> {Pessoa.empresa}')
print(f"Método de classe ===> {Pessoa.mudarcompania('Metáis HS ltda')}")
print(f'Método estático ===> {Pessoa.geraid()}')
print(f'Atributo protegido ===> {victoria.salario}')

