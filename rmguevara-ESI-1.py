def permutacion_filas():
    try:
        mensaje = input("Ingresa el mensaje: ").replace(" ", "-")
        filas = 5 
        columnas = max(3, -(-len(mensaje) // filas))  #3 columnas

        matriz = filas * columnas
        if len(mensaje) < matriz:
            mensaje += '*' * (matriz - len(mensaje))
        matriz = [list(mensaje[i * columnas: (i + 1) * columnas]) for i in range(filas)]

        # Permutaciín por filas
        matriz_permutada = matriz[::1]
        mensaje_cifrado = ''.join(''.join(fila) for fila in matriz_permutada)
    
        print("Mensaje Original:", mensaje.replace("*", ""))
        print("Matriz de Cifrado:")
        for fila in matriz_permutada:
            print(' '.join(fila))
        print("Mensaje Cifrado:", mensaje_cifrado)

    except Exception as e:
        print(f"Error en la ejecución: {e}")

permutacion_filas()
