print ("CONTROLES DE TV")
print ("1 = encender")
print ("2 = apagar")
print ("3 = subir volumen")
print ("4 = bajar volumen")
print ("5 = cambiar canal")
print ("6 = mute")


print ("")
  
numero = int(input("Escoja una accion para que ejecute el auto:  "))

print ("")

class Television:

    botones = True
    Volumen = "Mayor o menor"
    pantalla = 1
    bocinas = True

    def encender(self):
        print("La Tv se prendio")
        
    def apagar(self):
        print("La Tv se apago")

    def subir_volumen(self):
        print("La Tv se sube el volumen")

    def bajar_volumen(self):
        print("La Tv se baja el volumen")

    def cambiar_canal(self):
         print("La Tv cambia de canal")
        
    def mute(self):
        print("La Tv se silencia")

Tv = Television()

if numero == 1:
  Tv.encender()
elif numero == 2:
    Tv.apagar()
elif numero == 3:
    Tv.subir_volumen()
elif numero == 4:
    Tv.bajar_volumen()
elif numero == 5:
    Tv.cambiar_canal()
elif numero == 6:
    Tv.mute()

        
