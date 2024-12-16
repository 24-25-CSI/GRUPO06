def cifrado_p_fila(mensaje):
    # Definimos el número de filas a usar
    filas = 5
    
    # El mensaje se le pone "-" para separar los espacios
    mensaje = mensaje.lower().replace(" ", "-")
    # Calculamos el tamaño del mensaje
    longitud_mensaje = len(mensaje)
    
    # Aseguramos que las columnas sean mínimo de 3
    columnas = max(3, (longitud_mensaje + filas - 1) // filas)
    # Creamos una matriz vacía en la cual almacenaremos nuestro mensaje
    matriz = [["*"] * columnas for _ in range(filas)]
    index = 0
    
    # Llenamos la matriz por columnas
    for j in range(columnas):
        for i in range(filas):
            if index < longitud_mensaje:
                matriz[i][j] = mensaje[index]
                index += 1

    # Mostramos la matriz de cifrado
    print("Matriz de cifrado:")
    for fila in matriz:
        print(" ".join(fila))
    
    # Construimos el mensaje cifrado leyendo por filas
    mensaje_cifrado = "".join("".join(matriz[i][j] for j in range(columnas)) for i in range(filas))
    
    # Mostramos los resultados
    print("Mensaje original:", mensaje)
    print("Mensaje cifrado:", mensaje_cifrado)
    
    return mensaje_cifrado
            
if __name__ == "__main__":
    print("Bienvenido, escriba su mensaje por favor:")
    mensaje = input("mensaje: ")
    resultado = cifrado_p_fila(mensaje)
