class Gatos:
    '''
    Atributo são características, variáveis que armazenam dados do objeto
    Método Construtor
    '''
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade


    # Métodos são funções dentro da classe que descrevem os comportamentos do objeto
    def mia(self): # self referencia a classe em que está identada
        print(f'miau')

    def briga(self, n1, n2):
        patadas = n1 + n2
        print(f'Houve {patadas} patadas'.format(n1, n2))
        return patadas


Gatos_1 = Gatos('Wendy','Siamesa', '7 anos') # Objeto é uma instância da classe - exemplo concreto
print(Gatos_1.nome)
print(Gatos_1.raca)
print(Gatos_1.idade)
# acessar o método
Gatos_1.mia()
Gatos_1.briga(2,5)
