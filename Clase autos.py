class Autos:

    def __init__(self,nombre, fiabilidad, espacio, comodidad, ahorro, seguridad):
        self.nombre = nombre
        self.fiabilidad = fiabilidad
        self.espacio = espacio
        self.comodidad = comodidad
        self.ahorro = ahorro
        self.seguridad = seguridad

auto1 = Autos("Honda", 66, 52 ,53 ,69 ,79 )
print (auto1.nombre, auto1.espacio)

print("")

auto2 = Autos("Nissan", 59, 42 ,63 ,77 ,38 )
print (auto2.nombre, auto2.espacio)

print("")

auto3 = Autos("Ford", 61, 22 ,73 ,49 ,79 )
print (auto3.nombre, auto3.espacio)

print("")

auto4 = Autos("Tsuru tuneado", 86, 62 ,83 ,89 ,80)
print (auto4.nombre, auto4.espacio)

print("")

auto5 = Autos("Toyota", 36, 29 ,55 ,65 ,70 )
print (auto5.nombre, auto5.espacio)


