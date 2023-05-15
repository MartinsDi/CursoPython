class Pessoas:
    def __int__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self, nome=0):
        return self.nome

    def getIdade(self, idade=0):
        return self.idade

    def cadastra(self):
        n = str(input('Nome: '))
        self.setNome(n)
        i = int(input('Idade: '))
        self.setIdade(i)
        print(self.apresentação())

    def apresentação(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}'
