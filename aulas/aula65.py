
class Pessoa:
  def __init__(self, nome, idade):
    self.__nome = nome
    self.__idade = idade

  def get_nome(self):
    return self.__nome

  def set_nome(self, nome):
    self.__nome = nome

  def get_idade(self):
    return self.__idade

  def set_idade(self, idade):
    self.__idade = idade

  def apresentar(self):
    print(f'Nome: {self.get_nome()}, Idade: {self.get_idade()}')


pessoa = Pessoa('Wellinton', 30)
pessoa.apresentar()