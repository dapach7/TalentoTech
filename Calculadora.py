import math

class Calculadora:
    def __init__(self, num_uno, num_dos):
        self.num_uno = num_uno
        self.num_dos = num_dos
           
    def suma(self):
        print(f"La suma de {self.num_uno} + {self.num_dos} = {self.num_uno + self.num_dos}")
            
    def resta(self):
        print(f"La resta de {self.num_uno} - {self.num_dos} = {self.num_uno - self.num_dos}")
            
    def multiplicacion(self):
        print(f"La multiplicacion de {self.num_uno} * {self.num_dos} = {self.num_uno * self.num_dos}")   
            
    def division(self):               
        print(f"La division de {self.num_uno} / {self.num_dos} = {round(self.num_uno / self.num_dos,3)}")

    def logaritmo(self):
        print(f"El logaritmo en base 10 de {self.num_uno} es {round(math.log10(),3)}")

    def coseno(self):
        print(f"El coseno de {self.num_uno} es {round(math.cos(self.num_uno,3))}")

    def seno(self):
        print(f"el seno de {self.num_uno} es {round(math.sin(self.num_uno),3)}")

    def tangente(self):
        print(f"el seno de {self.num_uno} es {round(math.tan(self.num_uno),3)}")               
        

print("****BIENVENIDO A LA CALCULADORA*****")
print()
while  True:
    metodo = int(input("Ingrese el metodo:\n *suma (1)\n *resta (2)\n *multipli (3)\n *division (4)\n *logaritmo (5)\n *coseno (6)\n"
    " *seno (7)\n *salir (8)\n Escribe el metodo a ejecutar: --> "))
    if metodo in range(1,5):
        numero_1 = float(input("Ingrese el primer numero: -> "))
        numero_2 = float(input("Ingrese el segundo numero: -> "))
        operador = Calculadora(numero_1,numero_2)

        if metodo == 1:
            operador.suma()
        elif metodo == 2: 
            operador.resta()
        elif metodo == 3:
            operador.multiplicacion()
        elif metodo ==4:
            if numero_2 != 0:
                operador.division()
            else:
                print("ERROR DIVISION ENTRE 0")
    elif metodo in range(5,8):
        numero_1 = float(input("Ingrese el  numero: -> "))
        numero_2 = 1
        operador = Calculadora(numero_1,numero_2)
        if metodo ==5:
            operador.logaritmo()
        elif metodo == 6:
            operador.coseno()
        elif metodo == 7:
            operador.seno()
    elif metodo ==8:
        print("fin del programa")
        break
                
    else:
        print("Ingrese un metodo valido")
        print("***FIN***")

