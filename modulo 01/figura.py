

class Figura:

    def __int__(self):
        self.__color = ""
        self.__nome  = ""
    
    def getNome(self):
        return self.__nome
        

    def setNome(self, nome):
        self.__nome = nome

    def Area(self):
        pass
    
    def getCor(self):
        return self.__color
    
    def setCor(self, color):
        self.__color = color


class Quadrado(Figura):
    __lado  = 3
    
    def getLado(self):
        return self.__lado



    def Area(self):
        return self.getLado() * self.getLado()


class Circulo(Figura):
    __raio  = 3
    
    def getRaio(self):
        return self.__raio

    def Area(self):
        return self.getRaio() * self.getRaio() * 3.14


qua = Quadrado()
qua.setNome("Quadrado")
cir = Circulo()
cir.setNome("Circulo")

lista_de_figuras = [qua, cir]

for figura in lista_de_figuras:
    print(figura.getNome() + " area: " +  str(figura.Area())) 