




class Veiculo:
    __rodas = None

    def setRodas(self, valor):
        raise NotImplementedError


class Carro(Veiculo):
    

    def getRodas(self):
        return self.__rodas

carro  = Carro()
carro.setRodas(4)
print(carro.getRodas())