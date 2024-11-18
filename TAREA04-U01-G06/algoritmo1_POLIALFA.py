import os
import time
import random
import string


def generate_key(length):
    """Genera una clave alfabética aleatoria de la longitud especificada."""
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


def vigenere_encrypt(text, key):
    """Cifra un texto usando el cifrado de Vigenère."""
    encrypted_text = []
    key = key.upper()
    text = text.upper()
    key_index = 0
    for char in text:
        if char.isalpha():
            text_pos = ord(char) - ord('A')
            key_pos = ord(key[key_index]) - ord('A')
            encrypted_char = chr((text_pos + key_pos) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)


def vigenere_decrypt(encrypted_text, key):
    """Descifra un texto cifrado usando el cifrado de Vigenère."""
    decrypted_text = []
    key = key.upper()
    encrypted_text = encrypted_text.upper()
    key_index = 0
    for char in encrypted_text:
        if char.isalpha():
            encrypted_pos = ord(char) - ord('A')
            key_pos = ord(key[key_index]) - ord('A')
            decrypted_char = chr((encrypted_pos - key_pos) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)


def process_file(file_path, output_folder):
    """Procesa un archivo, generando la clave, cifrado y descifrado, y almacenando los resultados."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Generar clave
    start_time = time.time()
    key = generate_key(len(text))
    key_time = time.time() - start_time

    # Cifrar texto
    start_time = time.time()
    encrypted_text = vigenere_encrypt(text, key)
    encrypt_time = time.time() - start_time

    # Descifrar texto
    start_time = time.time()
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    decrypt_time = time.time() - start_time

    # Guardar resultados
    base_name = os.path.basename(file_path).split('.')[0]
    with open(os.path.join(output_folder, f"{base_name}_key.txt"), 'w', encoding='utf-8') as file:
        file.write(key)

    with open(os.path.join(output_folder, f"{base_name}_encrypted.txt"), 'w', encoding='utf-8') as file:
        file.write(encrypted_text)

    with open(os.path.join(output_folder, f"{base_name}_decrypted.txt"), 'w', encoding='utf-8') as file:
        file.write(decrypted_text)

    return key_time, encrypt_time, decrypt_time


def main():
    tamanos_palabras = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    input_folder = "archivos_iniciales"
    output_folder = "respuesta_POLIALFABETICO"

    # Crear carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    for tamano in tamanos_palabras:
        file_path = os.path.join(input_folder, f"{tamano}.txt")
        if os.path.exists(file_path):
            print(f"Procesando archivo: {file_path}")
            key_time, encrypt_time, decrypt_time = process_file(file_path, output_folder)
            print(f"Tiempos para {tamano}.txt - Clave: {key_time:.10f}s, Cifrado: {encrypt_time:.10f}s, Descifrado: {decrypt_time:.10f}s\n")
        else:
            print(f"Archivo no encontrado: {file_path}")


if __name__ == "__main__":
    main()
