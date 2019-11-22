


class Base(object):
    def __init__(self, y):
        print('eu foi chamado pela class Base')
        print(y)


class Derivada(Base):
    def __init__(self):
        #Base.__init__(self, 10, 15)
        #super().__init__(10) # python 3
        super(Derivada, self).__init__(10) #python 2
        print('eu foi chamado pela class Derivada')

teste =  Derivada()