peso = 77
estatura = 1.72

imc = peso/(estatura**2)
print(imc)

if imc >= 0 and imc <= 18.5:
    print("Esta bajo de peso")

if imc >= 18.5 and imc <= 24.9:
    print("Esta normal de peso")

if imc >= 25 and imc <= 29.9:
    print("Esta con sobrepeso")

if imc >= 30:
    print("Esta obeso")


