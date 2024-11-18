import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# Función para generar claves RSA
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

# Función para cifrar texto usando AES
def encrypt_with_aes(plaintext, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = sym_padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return iv, ciphertext

# Función para descifrar texto usando AES
def decrypt_with_aes(ciphertext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(decrypted_padded) + unpadder.finalize()
    return plaintext.decode()

# Función principal para procesar un archivo
def process_file(file_path, output_folder):
    # Leer el archivo
    with open(file_path, 'r') as file:
        plaintext = file.read().strip()

    print(f"\nProcesando archivo: {file_path}")

    # Generación de claves
    start_time = time.time()
    private_key, public_key = generate_keys()
    print(f"Tiempo para generar claves: {time.time() - start_time:.4f} segundos")

    # Generar una clave simétrica para AES
    aes_key = os.urandom(32)  # Clave de 256 bits para AES

    # Cifrar la clave simétrica con la clave pública RSA
    start_time = time.time()
    encrypted_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"Tiempo para cifrar clave AES con RSA: {time.time() - start_time:.4f} segundos")

    # Guardar la clave AES cifrada en un archivo
    encrypted_key_path = os.path.join(output_folder, f"{os.path.basename(file_path)}_encrypted_key.txt")
    with open(encrypted_key_path, "wb") as key_file:
        key_file.write(encrypted_key)

    # Cifrar el texto con AES
    start_time = time.time()
    iv, ciphertext = encrypt_with_aes(plaintext, aes_key)
    print(f"Texto cifrado (AES): {ciphertext[:50]}... (truncado)")
    print(f"Tiempo para cifrar texto: {time.time() - start_time:.4f} segundos")

    # Guardar el texto cifrado en un archivo
    ciphertext_path = os.path.join(output_folder, f"{os.path.basename(file_path)}_ciphertext.txt")
    with open(ciphertext_path, "wb") as cipher_file:
        cipher_file.write(iv + ciphertext)

    # Descifrar la clave simétrica con la clave privada RSA
    start_time = time.time()
    decrypted_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"Tiempo para descifrar clave AES con RSA: {time.time() - start_time:.4f} segundos")

    # Descifrar el texto con AES
    start_time = time.time()
    decrypted_text = decrypt_with_aes(ciphertext, decrypted_key, iv)
    print(f"Texto descifrado: {decrypted_text[:50]}... (truncado)")
    print(f"Tiempo para descifrar texto: {time.time() - start_time:.4f} segundos")

    # Guardar el texto descifrado en un archivo
    decrypted_text_path = os.path.join(output_folder, f"{os.path.basename(file_path)}_decrypted.txt")
    with open(decrypted_text_path, "w") as decrypted_file:
        decrypted_file.write(decrypted_text)

# Configuración de la carpeta de salida
output_folder = "resultados_PGP"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Lista de archivos para procesar
file_paths = [
    "10.txt", "100.txt", "1000.txt", "10000.txt", "100000.txt", "1000000.txt", "10000000.txt"
]

# Procesar cada archivo
for file_path in file_paths:
    try:
        process_file(file_path, output_folder)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
