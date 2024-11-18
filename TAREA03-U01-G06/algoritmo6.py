
cipher_matrix = {
    'a': 'QA', 'b': 'QS', 'c': 'QD', 'd': 'QF', 'e': 'QG',
    'f': 'WA', 'g': 'WS', 'h': 'WD', 'i': 'WF', 'j': 'WG',
    'k': 'EA', 'l': 'ES', 'm': 'ED', 'n': 'EF', 'o': 'EG',
    'p': 'RA', 'q': 'RS', 'r': 'RD', 's': 'RF', 't': 'RG',
    'u': 'TA', 'v': 'TS', 'w': 'TD', 'x': 'TF', 'y': 'TG', 'z': 'TG'
}

def encrypt_message(message):
    encrypted_message = ""


    for char in message.lower():
        if char in cipher_matrix:
            encrypted_message += cipher_matrix[char]
        else:
            encrypted_message += "**" 
    
    return encrypted_message


message = input("Ingrese el mensaje a cifrar: ")
encrypted_message = encrypt_message(message)


print("\nMatriz de Cifrado:")
for key, value in cipher_matrix.items():
    print(f"{key.upper()} -> {value}")

print("\nMensaje Original:", message)
print("Mensaje Cifrado:", encrypted_message)
