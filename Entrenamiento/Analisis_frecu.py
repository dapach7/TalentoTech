import sys
from collections import defaultdict

def main():
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} [archivo] [tam. max grupo]")
        return

    archivo = sys.argv[1]
    try:
        max_tam_grupo = int(sys.argv[2])
    except ValueError:
        print("El tamaño máximo del grupo debe ser un número entero.")
        return

    total = 0

    for i in range(max_tam_grupo):
        freq = defaultdict(int)

        try:
            with open(archivo, 'r') as f:
                contenido = f.read()
        except FileNotFoundError:
            print(f"No se pudo abrir el archivo: {archivo}")
            return

        # Eliminar espacios en blanco
        contenido = ''.join(contenido.split())

        # Contar las secuencias de longitud i+1
        for j in range(len(contenido) - i):
            sub = contenido[j:j + i + 1]
            freq[sub] += 1

        print(f"\n-- FREC. DE TAM. {i + 1} --")
        count = 0
        for grupo, cantidad in freq.items():
            if cantidad > 1:
                print(f"{grupo}: {cantidad}\t", end='')
                count += 1
                if count % 6 == 0:
                    print()
            total += cantidad
        print()

    print(f"\nTotal de letras: {(total // max_tam_grupo) + 1}")

if __name__ == "__main__":
    main()
