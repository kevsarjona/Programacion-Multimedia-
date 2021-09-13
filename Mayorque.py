num1= int(input("Numero 1:"))
num2= int(input("Numero 2:"))

def mayorque ():
    if num1==num2:
        print("Son numeros iguales")
    elif num1>num2:
        print(f"Es mayor", num1, "que" ,num2)
    else:
        print("Es mayor", num2, "que" ,num1)

mayorque()
