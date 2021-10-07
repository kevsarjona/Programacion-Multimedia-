
class celulares:
    
    def __init__(self,nombre, camfrontal, camprincipal, almacenamiento, memoria,tipo):
        self.nombre = nombre
        self.camfrontal = camfrontal
        self.camprincipal = camprincipal
        self.almacenamiento = almacenamiento
        self.memoria = memoria
        self.tipo = tipo


cel1 = celulares("iphone 13", 15, 80, 256, 16, "Gama Alta")
print("Su cel es un", cel1.nombre)
print ("Clasificacion: ", cel1.tipo)
print ("Camara frontal: ", cel1.camfrontal ,"Mpx","Camara trasera: ", cel1.camprincipal,"Mpx")
print ("Almacenamiento: ", cel1.almacenamiento ,"GB"," Memoria:", cel1.memoria, "GB")

print("")

cel2 = celulares("Galaxy Note 10", 11, 50, 64, 6, "Gama Media")
print("Su cel es un", cel2.nombre)
print ("Clasificacion: ", cel2.tipo)
print ("Camara frontal: ", cel2.camfrontal ,"Mpx","Camara trasera: ", cel2.camprincipal,"Mpx")
print ("Almacenamiento: ", cel2.almacenamiento ,"GB"," Memoria:", cel2.memoria, "GB")

print("")

cel3 = celulares("iphone XR", 13, 60, 128, 8, "Gama Alta")
print("Su cel es un", cel3.nombre)
print ("Clasificacion: ", cel3.tipo)
print ("Camara frontal: ", cel3.camfrontal ,"Mpx","Camara trasera: ", cel3.camprincipal,"Mpx")
print ("Almacenamiento: ", cel3.almacenamiento ,"GB"," Memoria:", cel3.memoria, "GB")

print("")

cel4 = celulares("Moto E7", 10, 50, 64, 6, "Gama Media")
print("Su cel es un", cel4.nombre)
print ("Clasificacion: ", cel4.tipo)
print ("Camara frontal: ", cel4.camfrontal ,"Mpx","Camara trasera: ", cel4.camprincipal,"Mpx")
print ("Almacenamiento: ", cel4.almacenamiento ,"GB"," Memoria:", cel4.memoria, "GB")

print("")

cel5 = celulares("Samsung A15", 13, 45, 45, 4, "Gama Baja")
print("Su cel es un", cel5.nombre)
print ("Clasificacion: ", cel5.tipo)
print ("Camara frontal: ", cel5.camfrontal ,"Mpx","Camara trasera: ", cel5.camprincipal,"Mpx")
print ("Almacenamiento: ", cel5.almacenamiento ,"GB"," Memoria:", cel5.memoria, "GB")




        

