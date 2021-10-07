class bebidas:

    def __init__(self,nombre, azucar, agua, cafeina, sodio, proteina, potasio, grasasat):
        self.nombre = nombre
        self.azucar = azucar
        self.agua = agua
        self.cafeina = cafeina
        self.sodio = sodio
        self.proteina = proteina
        self.potasio = potasio
        self.grasasat = grasasat


bebida1 = bebidas("Coca Cola", 25, 15, 9, 50, 11, 20, 13)
print(bebida1.agua)

bebida2 = bebidas("Sprite", 32, 14, 8, 23, 3, 17, 29)
print(bebida2.agua)

bebida3 = bebidas("Manzanita", 28, 5, 19, 40, 31, 10, 7)
print(bebida3.agua)

bebida4 = bebidas("Seven UP", 48, 12, 2, 17, 41, 5, 7)
print(bebida4.agua)

bebida5 = bebidas("Pepsi", 36, 25, 14, 30, 31, 8, 7)
print(bebida5.agua)




