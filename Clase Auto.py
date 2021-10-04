print ("CONTROLES")
print ("1 = encender")
print ("2 = apagar")
print ("3 = frenar")
print ("4 = acelerar")
print ("5 = reversa")
print ("6 = claxon")


print ("")
  
numero = int(input("Escoja una accion para que ejecute el auto:  "))

print ("")

class Auto:

    llantas =  4
    volante = True
    puertas = 5
    vidrios = 6
    espejos = 4

    def encender(self):
        print("El auto  esta encendiendo")
        
    def apagar(self):
        print("El auto se apago")
        
    def frenar(self):
        print("El auto se frena")
        
    def acelerar(self):
        print ("El auto acelera")
        
    def reversa(self):
        print ("El auto se hecha de reversa")
        
    def claxon(self):
        print ("Toca el claxon")

Coche = Auto()

if numero == 1:
  Coche.encender()
elif numero == 2:
    Coche.apagar()
elif numero == 3:
    Coche.frenar()
elif numero == 4:
    Coche.acelerar()
elif numero == 5:
    Coche.reversa()
elif numero == 6:
    Coche.claxon()

