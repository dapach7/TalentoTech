import math

p = 5
q = 13
m = 2

def rsa(p,q,m):
    n =  p*q
    fi_n = (p-1)*(q-1)
    k = fi_n + 1

    for i in range(2, fi_n ):
        if math.gcd(i,fi_n) == 1:
            d = k//i
            if k == (i*d):
                llave_publica = [i , n]
                llave_privada = [d, n]
                if math.gcd(m, n) == 1  and m < n:
                    mc = (m**i)%n
                    print(f"el mc es {mc}")
                    return [mc,n, d]
                                

def un_rsa(list):
    m = ((list[0]**list[2])) % list[1]
    print(f"el mensaje descifrado m es: {m}")

try:
    loco = rsa(p,q,m)
    un_rsa(loco)
except TypeError:
    print("Escoja otros numeros")



