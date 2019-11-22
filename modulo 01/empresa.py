


class Funcionario:

    def __init__(self):
        self.__salario = 2000
        self.__cargo  = "Funcionario"

    def getSalario(self):
        return self.__salario
    
    def setSalario(self, valor):
        self.__salario = valor


class Gerente(Funcionario):
    pass

class Secretaria(Funcionario):
    
    def setSalario(self, novo_valor):
        if (novo_valor < 2000): 
            self.__salario = novo_valor
        else:
            print("secretaria nao pode receber o mesmo que o gerente")


class Telefonista(Funcionario):
    pass


gabi = Secretaria()

gabi.setSalario(2000)
