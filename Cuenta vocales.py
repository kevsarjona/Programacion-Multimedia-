palabras = input("Introduce una palabra")
string = palabras.lower()

print (string)
count = 0

vocales = ["a", "e", "i", "o", "u"]
for char in string:
    if char in vocales:
        count = count+1

print ("Tu palabra tiene", count, "vocales")
