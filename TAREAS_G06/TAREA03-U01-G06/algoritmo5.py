def cifrado_vigenere():
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    mensaje = input("Ingrese el mensaje a cifrar: ").lower()
    clave = input("Ingrese la frase clave para el cifrado Vigenère: ").lower()
    mensaje_cifrado = "" 
    clave_repetida = (clave * (len(mensaje) // len(clave) + 1))[:len(mensaje)]
    
    for i in range(len(mensaje)):
        letra_mensaje = mensaje[i]
        letra_clave = clave_repetida[i]
        
        if letra_mensaje in alfabeto:
            posicion_mensaje = alfabeto.index(letra_mensaje)
            posicion_clave = alfabeto.index(letra_clave)
            posicion_cifrada = (posicion_mensaje + posicion_clave) % len(alfabeto)
            mensaje_cifrado += alfabeto[posicion_cifrada]
        else:
            mensaje_cifrado += letra_mensaje

    print("Mensaje cifrado con Vigenère:", mensaje_cifrado)

if __name__ == "__main__":
    cifrado_vigenere()
