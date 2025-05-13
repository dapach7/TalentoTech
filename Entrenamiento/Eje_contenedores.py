lista = ["mazana", "uva", "papaya", "mora"]
tupla = ("mazana", "uva", "papaya", "mora")
conjunto = {"mazana", "uva", "papaya", "mora"}
diccionario = {1:"mazana", 2:"uva", 3:"papaya", 4:"mora"}

print("ejercicio con lista")
for fruta in lista:
    print(fruta)
print("****************")
print("ejercicio con tupla")
for fruta2 in tupla:
    print(fruta2)
print("****************")
print("ejercicio con conjunto")
for fruta3 in conjunto:
    print(fruta3)
print("****************")
print("ejercicio con diccionario")
for key in diccionario:
    print(f"{key} : {diccionario[key]}")
