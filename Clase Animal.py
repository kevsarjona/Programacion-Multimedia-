print ("ESPECIES")
print ("1 = aves")
print ("2 = reptiles")
print ("3 = ranas")
print ("4 = insectos")
print ("5 = arañas")
print ("6 = cangrejos")

print ("")
  
numero = int(input("Escoja su especie:  "))

class Animal:

    patas = True
    ojos = True
    consciencia = False
    organos = True
    
    def aves(self):
        accion_aves = ("volar , nadar, planear y saltar") 
        print ("Su especie puede", accion_aves)
    def reptiles(self):
        accion_reptiles = ("vivir lejos del agua y buscar comida adicional") 
        print ("Su especie puede", accion_reptiles)
    def ranas(self):
        accion_ranas = ("saltar, cantar y nadar") 
        print ("Su especie puede", accion_ranas)
    def Insectos(self):
        accion_insectos = ("parásito de otros organismos") 
        print ("Su especie es ", accion_insectos)
    def Arañas(self):
        accion_arañas = ("producir seda para hacer sus telarañas que sirven paea su alimento") 
        print ("Su especie puede", accion_arañas)
    def Cangrejos(self):
        accion_cangrejos = ("desplazarse por el fondo del mar, tranistar afuera del agua y trepar palmeras") 
        print ("Su especie puede", accion_cangrejos)

Especie = Animal()

if numero == 1:
  Especie.aves()
elif numero == 2:
    Especie.reptiles()
elif numero == 3:
    Especie.ranas()
elif numero == 4:
    Especie.Insectos()
elif numero == 5:
    Especie.Arañas()
elif numero == 6:
    Especie.Cangrejos()

