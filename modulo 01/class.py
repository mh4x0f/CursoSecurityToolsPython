

class Veiculo:
    __rodas = 4
    __conbustivel = 0
    __velocidade = 10

    def __init__(self, teste=40):
        print("instanciando a class ")
        self.__teste = teste

    @staticmethod
    def VerifcarVeiculo():
        print("verifacando veiculo")

    def getTeste(self):
        return self.__teste

    def getRodas(self):
        return self.__rodas

    def setRodas(self, novo_valor):
        self.__rodas = novo_valor

    def getVelocidade(self):
        return self.__velocidade

    def mostrarVelocidade(self):
        print(self.getVelocidade())

    def mostrarRodas(self):
        print(self.getRodas())

Veiculo().VerifcarVeiculo()
carro = Veiculo(50)
carro.setRodas(6)
carro.mostrarVelocidade()
carro.mostrarRodas()
