def cifrado_p_columna():
    mensaje = input("Ingrese el mensaje a cifrar: ").lower().replace(" ", "")
    n = int(input("Ingrese la clave (número de columnas) para el cifrado por columnas: "))
    mensaje_cifrado = ""

    if len(mensaje) > n * n:
        print("El número de caracteres del mensaje excede el límite de la matriz.")
        return
   
    matriz = [["*"] * n for _ in range(n)]
    index = 0

    for i in range(n):
        for j in range(n):
            if index < len(mensaje):
                matriz[i][j] = mensaje[index]
                index += 1

    print("Matriz de cifrado:")
    for fila in matriz:
        print(" ".join(fila))
    
    for j in range(n):
        for i in range(n):
            mensaje_cifrado += matriz[i][j]

    print("Mensaje cifrado con método de columnas:", mensaje_cifrado)

if __name__ == "__main__":
    cifrado_p_columna()
