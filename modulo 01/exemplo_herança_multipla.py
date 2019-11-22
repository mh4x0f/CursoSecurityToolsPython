


class FuncionarioAMD:

    def __init__(self):
        self.__salario = 2000
        self.__cargo  = "Funcionario"
        self.__bonus  = 400

    def getSalario(self):
        return self.__salario + self.getBonus()
    
    def getBonus(self):
        return self.__bonus

    def setBonus(self, bonus):
        self.__bonus = bonus

    def setSalario(self, valor):
        self.__salario = valor

class Funcionario:

    def __init__(self):
        self.__salario = 2000
        self.__cargo  = "Funcionario"

    def getSalario(self):
        return self.__salario
    
    def setSalario(self, valor):
        self.__salario = valor


class Gerente(FuncionarioAMD, Funcionario):
    pass

class Secretaria(Funcionario):
    pass


class Telefonista(Funcionario):
    pass


marcos = Gerente()
gabi = Secretaria()
print("Salario de Marcos: " +  str(marcos.getSalario()))
print("Salario de Gabi: "  + str(gabi.getSalario()))