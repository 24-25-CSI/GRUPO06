import hashlib
import time
import os

def leer_archivo(ruta):
    """Leer el contenido de un archivo."""
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return archivo.read()

def generar_clave():
    """Generar una clave única para el cifrado."""
    return hashlib.sha256(str(time.time()).encode()).hexdigest()

def cifrar_mensaje(texto, clave):
    """Cifrar un mensaje utilizando RIPEMD160."""
    texto_con_clave = texto + clave
    ripemd = hashlib.new('ripemd160')
    ripemd.update(texto_con_clave.encode('utf-8'))
    return ripemd.hexdigest()

def medir_tiempo(funcion, *args):
    """Medir el tiempo de ejecución de una función."""
    inicio = time.time()
    resultado = funcion(*args)
    tiempo = time.time() - inicio
    return resultado, tiempo

def guardar_resultado(ruta, contenido):
    """Guardar contenido en un archivo."""
    with open(ruta, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

def main():
    tamanos_palabras = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    carpeta_salida = "resultados_RIPEMD"
    
    # Crear carpeta de resultados si no existe
    os.makedirs(carpeta_salida, exist_ok=True)
    
    for tamano in tamanos_palabras:
        ruta_archivo = f"{tamano}.txt"
        print(f"Procesando archivo con {tamano} palabras:")
        
        # Leer archivo
        texto, tiempo_lectura = medir_tiempo(leer_archivo, ruta_archivo)
        print(f"Tiempo para leer el archivo: {tiempo_lectura:.5f} segundos")
        
        # Generar clave
        clave, tiempo_clave = medir_tiempo(generar_clave)
        print(f"Clave generada: {clave}")
        print(f"Tiempo para generar la clave: {tiempo_clave:.5f} segundos")
        
        # Cifrar mensaje
        texto_cifrado, tiempo_cifrado = medir_tiempo(cifrar_mensaje, texto, clave)
        print(f"Texto cifrado: {texto_cifrado}")
        print(f"Tiempo para cifrar el texto: {tiempo_cifrado:.5f} segundos")
        
        # Guardar clave y texto cifrado en archivos separados
        ruta_clave = os.path.join(carpeta_salida, f"clave_{tamano}.txt")
        ruta_cifrado = os.path.join(carpeta_salida, f"cifrado_{tamano}.txt")
        
        guardar_resultado(ruta_clave, clave)
        guardar_resultado(ruta_cifrado, texto_cifrado)
        
        print(f"Clave guardada en: {ruta_clave}")
        print(f"Cifrado guardado en: {ruta_cifrado}")
        print("-" * 50)

if __name__ == "__main__":
    main()
