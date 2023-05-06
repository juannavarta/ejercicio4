class Ventana:
    __titulo = ""
    __Xsi = 0
    __Ysi = 0
    __Xid = 0
    __Yid = 0

    def __init__(self, tit = 'Untitled', xsi = 0, ysi = 0, xid = 500, yid = 500):
        self.__titulo = tit
        self.__Xsi = xsi
        self.__Ysi = ysi
        self.__Xid = xid
        self.__Yid = yid
    def mostrar(self):
        print("Coordenadas Esquina SI ({},{})\nCoordenadas Esquina ID ({},{})".format(self.__Xsi, self.__Ysi, self.__Xid, self.__Yid))
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return (self.__Yid - self.__Ysi)
    def ancho(self):
        return (self.__Xid - self.__Xsi)
    def moverDerecha(self, uni = 0):
        self.__Xsi += uni
        self.__Xid += uni
    def moverIzquierda(self, uni = 0):
        self.__Xsi -= uni
        self.__Xid -= uni
    def subir(self, uni = 0):
        self.__Ysi += uni
        self.__Yid += uni
    def bajar(self, uni = 0):
        self.__Ysi -= uni
        self.__Yid -= uni