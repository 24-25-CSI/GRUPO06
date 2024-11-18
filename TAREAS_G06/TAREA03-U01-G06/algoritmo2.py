def cifrado_permutacion_filas():
    mensaje = input("Ingresa el mensaje: ").replace(" ", "")
    n = int(input("Ingresa el tamaño de la matriz (n): "))

    if len(mensaje) > n * n:
        print("El mensaje es demasiado largo para la matriz dada.")
        return
    
    mensaje += '*' * (n * n - len(mensaje))
    
    matriz = [list(mensaje[i * n: (i + 1) * n]) for i in range(n)]
    
    matriz_permutada = matriz[::-1]  
    
    mensaje_cifrado = ''.join(''.join(fila) for fila in matriz_permutada)
    
    print("Matriz de Cifrado:")
    for fila in matriz_permutada:
        print(' '.join(fila))
    print("\nMensaje Original:", mensaje.replace('*', ''))
    print("Mensaje Cifrado:", mensaje_cifrado)

cifrado_permutacion_filas()
