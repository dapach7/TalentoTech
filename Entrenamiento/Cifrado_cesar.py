import pandas as pd
import string
import requests
from datetime import datetime 
import matplotlib.pyplot as plt
import random

# Alfabeto español con ñ
alfabeto = "abcdefghijklmnopqrstuvwxyz"
# Cifrado César (para cifrar y descifrar con desplazamiento)
def cifrar_cesar_es(texto, desplazamiento): 
    resultado = ""
    for caracter in texto:
        if caracter.lower() in alfabeto:
            es_mayus = caracter.isupper() 
            indice = alfabeto.index(caracter.lower())
            nuevo_indice = (indice + desplazamiento) % len(alfabeto)
            nuevo_caracter = alfabeto[nuevo_indice]
            resultado += nuevo_caracter.upper() if es_mayus else nuevo_caracter
        else:
            resultado += caracter
    return resultado

# Descifrado llamando cifrado con desplazamiento negativo 
def descifrar_cesar_es(texto_cifrado, desplazamiento):
    return cifrar_cesar_es(texto_cifrado, -desplazamiento)


Lista_palabras = ["Escavacion","Cimentacion","Columnas","vigas","Muros","Repello","Estuco","Pintura","Enchape","Cielo Falso"]
dataset1 = {"Mensaje_Original":Lista_palabras}
df = pd.DataFrame(dataset1)
df["Clave"] = [random.randint(1, 9) for _ in range(10)]
df["Mensaje_cifrado"] = df.apply(lambda row: cifrar_cesar_es((row["Mensaje_Original"]),(row["Clave"])), axis=1 )
df["Mensaje_descifrado"] = df.apply(lambda row: descifrar_cesar_es((row["Mensaje_cifrado"]),(row["Clave"])), axis=1 )   
df
