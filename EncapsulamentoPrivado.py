class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf  # Encapsulamento Privado

    def __apresentarDocumento(self):  # Encapsulamento Privado
        print(self.__cpf)

    def comprarBebida(self, bebida):
        if bebida == 'Cerveja':
            self.__apresentarDocumento()
        print('Comprado')

Sid = Pessoa('Sid', '18', '0000cpf00fake')
Sid.comprarBebida('Guarana')
Sid.comprarBebida('Cerveja')
