
class felino:

    def __init__(self,nombre, patas, peso, tipo, sexo):
        self.nombre = nombre
        self.patas = patas
        self.peso = peso
        self.tipo = tipo
        self.sexo = sexo
        

animal1 = felino("Leon", 4, 190, "Carnivoro", "Macho")
print (animal1.nombre, "tiene", animal1.patas ,"patas y pesa", animal1.peso )

print("")

animal2 = felino("Tigre", 4, 200 , "Carnivoro", "Macho" )
print (animal2.nombre, "tiene", animal2.patas,"patas y pesa", animal2.peso )

print("")

animal3 = felino("Leopardo", 4, 31,"Carnivoro", "Macho" )
print (animal3.nombre, "tiene", animal3.patas,"patas y pesa", animal3.peso )

print("")

animal4 = felino("Jaguar", 4, 96, "Carnivoro", "Hembra")
print (animal4.nombre, "tiene", animal4.patas,"patas y pesa", animal4.peso )

print("")

animal5 = felino("Puma", 4, 88,"Carnivoro", "Hembra")
print (animal5.nombre, "tiene", animal5.patas,"patas y pesa", animal5.peso )





