import random
import datetime
import sys

class Tarjeta:
    def __init__(self, tipo_tarjeta):
        self.tipo_tarjeta = tipo_tarjeta
    def num_tarjeta_generador(self):
        if self.tipo_tarjeta == "visa":
            numero_tarjeta  = "4"
            espacio = 0
            for numero in range(14):
                espacio += 1
                if espacio == 4 or espacio == 7 or espacio == 11:
                    numero_tarjeta += " "
                numero_tarjeta += str(random.randint(0,9))
            return numero_tarjeta
        elif self.tipo_tarjeta == "mastercard":
            numero_tarjeta = "51"
            espacio = 0
            for numero in range(14):                
                espacio += 1
                if espacio == 3 or espacio == 7 or espacio == 11:
                    numero_tarjeta += " "
                numero_tarjeta += str(random.randint(0,9))
            return numero_tarjeta
    
    def cvv_generador(self):
        cvv = ""
        for i in range (3):
            cvv += str(random.randint(0,9))
        return cvv
    
    def fecha_generator(self):
        dato = datetime.datetime.now()
        año = dato.year
        return f"Fecha de vencimiento: {(random.randint(1,12)):02}/{año + random.randint(3,5)}"

def registro(nombre, cedula, diccionario, lista, tarjeta, cvv, fecha):
    lista.append(cedula)
    diccionario[cedula] = {"d_personales": [nombre,cedula], "d_tarjeta":(tarjeta, cvv, fecha)}


lista_cedulas = []
dicc_usuarios ={}
conjunt_tarjeta = {}

print("**********SISTEMA DE CREACIÓN DE TARJETAS**********")
Nombre = input(str("Introuzca su 1er nombre y 1er apeliido: ")).upper()
cedula = input(str("Introduzca su numero de cedula sin puntos: "))
tipo = input(str("Desea Visa o Mastercard: ")).lower()

try:
    if cedula in lista_cedulas:
        print("YA TIENES UNA TARJETA, ES UNA POR PERSONA")
    else:
        print("*****************************************************")
        print(f"Señor {Nombre} estos son los datos de su tarjeta:\n")
        print(f"Tipo de tarjeta: {tipo}")
        generator = Tarjeta(tipo)
        num_tarjet = generator.num_tarjeta_generador()
        
        if num_tarjet in conjunt_tarjeta:
            num_tarjet = generator.num_tarjeta_generador()
            conjunt_tarjeta.add(num_tarjet)
        else:
            conjunt_tarjeta.add(num_tarjet)
            print(f"El numero de su tarjeta es: {num_tarjet}")
            print(f"El codigo CVV es: {generator.cvv_generador()}")
            print(f"Fecha de vencimiento: {generator.fecha_generator()}")
            regis = registro(Nombre,cedula,dicc_usuarios,lista_cedulas,generator.num_tarjeta_generador(),generator.cvv_generador(),generator.fecha_generator())

except Exception as e:
    print("ERROR")
    sys.exit()





















