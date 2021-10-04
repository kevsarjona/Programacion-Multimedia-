print ("CONTROLES")
print ("1 = caminar")
print ("2 = correr")
print ("3 = respirar")
print ("4 = hablar")
print ("5 = comer")
print ("6 = dormir")

print ("")
  
numero = int(input("Dime un numero de acuedo ala accion que quieres que ejecute:  "))

class Humano:

    manos = 2
    pies = 2
    ojos = 2
    cabeza = 1
    nariz = 1
    orejas = 2
    dedos = 20
    boca = 1
    altura = 1.72
    peso = 80
    color = "moreno"
    consciencia = True
    organos = True
    
    def caminar(self):
        print("El humano esta caminando")
        
    def correr(self):
        print("El humano esta corriendo")
        
    def respirar(self):
        print("El humano esta respirando")
        
    def hablar(self):
        print ("El humano esta hablando")
        
    def comer(self):
        print ("El humano esta comiendo")

    def dormir(self):
        print ("El humano esta durmiendo")

Kevin = Humano()

if numero == 1:
  Kevin.caminar()
elif numero == 2:
    Kevin.correr()
elif numero == 3:
    Kevin.respirar()
elif numero == 4:
    Kevin.hablar()
elif numero == 5:
    Kevin.comer()
elif numero == 6:
    Kevin.dormir()





    
        
