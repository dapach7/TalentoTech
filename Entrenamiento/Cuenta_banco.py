class Cuentadebanco:
    def __init__(self,titular,numero_de_cuenta,saldo, movimientos=list):
        self.titular = titular
        self.numero_de_cuenta = numero_de_cuenta
        self.saldo = saldo
        self.movimientos = movimientos
        
    def Mostrarsaldo(self):
        print(f"Titular de la cuenta {self.titular} / Numero de cuenta {self.numero_de_cuenta} / El saldo de su cuenta es: ${self.saldo}")
    
    def ingresos(self):
        y = int(input("Cual es el valor a ingresar:$ "))
        if y >= 0:
            self.saldo = self.saldo + y
            print(f"Su nuevo saldo es:$ {self.saldo}")
            self.movimientos.append(+y)
        else:
            print("Valor no valido")

    def retirar(self):
        w = int(input("Ingrese el valor a retirar: "))
        if w <= self.saldo:
            self.saldo = self.saldo - w
            print(f"Su nuevo saldo es:$ {self.saldo}")
            self.movimientos.append(-w)
        else:
            print("No puedes retirar ese valor")
    def movientos(self):
        print("Estos fueron los movimentos realizados: ")
        for i in self.movimientos:
            if i < 0:
                print(f"$ {i}")
            else:
                print(f"$ +{i}")
        print(f"Total en cuenta actualmente:$ {self.saldo}")



titular = "LUIS DAZA PACHECO"
num_cuenta = "1892 2155 1221 12"
saldo = int(1000000)
mov =[]

cuenta = Cuentadebanco(titular,num_cuenta,saldo,mov)
cuenta.Mostrarsaldo()
cuenta.ingresos()
cuenta.Mostrarsaldo()
cuenta.retirar()
cuenta.Mostrarsaldo()
cuenta.movientos()

    

        

        

