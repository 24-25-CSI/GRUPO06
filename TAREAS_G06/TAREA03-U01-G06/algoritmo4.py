def cifrado_desplazamiento():
    mensaje = input("Ingresa la cadena de caracteres: ")
    desplazamiento = int(input("Ingresa el desplazamiento (n): "))
    
    alfabeto_mayus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfabeto_minus = 'abcdefghijklmnopqrstuvwxyz'
    
    alfabeto_cifrado_mayus = alfabeto_mayus[desplazamiento:] + alfabeto_mayus[:desplazamiento]
    alfabeto_cifrado_minus = alfabeto_minus[desplazamiento:] + alfabeto_minus[:desplazamiento]
    
    mensaje_cifrado = []
    for letra in mensaje:
        if letra in alfabeto_mayus:
            mensaje_cifrado.append(alfabeto_cifrado_mayus[alfabeto_mayus.index(letra)])
        elif letra in alfabeto_minus:
            mensaje_cifrado.append(alfabeto_cifrado_minus[alfabeto_minus.index(letra)])
        else:
            mensaje_cifrado.append(letra)
    
    mensaje_cifrado = ''.join(mensaje_cifrado)
    
    print("Alfabeto Original (Mayúsculas): ", alfabeto_mayus)
    print("Alfabeto Cifrado (Mayúsculas):  ", alfabeto_cifrado_mayus)
    print("Alfabeto Original (Minúsculas): ", alfabeto_minus)
    print("Alfabeto Cifrado (Minúsculas):  ", alfabeto_cifrado_minus)
    print("Mensaje Original:               ", mensaje)
    print("Mensaje Cifrado:                ", mensaje_cifrado)

cifrado_desplazamiento()
