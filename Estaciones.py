class Estacion:

    def __init__(self, name, parada, coordenadas):
        self.name = name
        self.parada = parada
        self.coordenadas = coordenadas

    def getName(self):
        return self.name

    def getParadas(self):
        return self.parada

    def getCordenada(self):
        return self.coordenadas