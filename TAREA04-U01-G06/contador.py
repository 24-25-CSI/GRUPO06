import os

# Función para contar los caracteres de un archivo
def contar_caracteres(archivo):
    try:
        # Intentamos abrir el archivo en UTF-8 primero
        with open(archivo, 'r', encoding='utf-8') as file:
            contenido = file.read()
            cantidad_caracteres = len(contenido)
            return cantidad_caracteres
    except UnicodeDecodeError:
        # Si ocurre un error de codificación, intentamos con una codificación alternativa
        try:
            with open(archivo, 'r', encoding='latin1') as file:
                contenido = file.read()
                cantidad_caracteres = len(contenido)
                return cantidad_caracteres
        except Exception as e:
            return f"Ocurrió un error al leer el archivo: {e}"
    except FileNotFoundError:
        return "El archivo no se encuentra."
    except Exception as e:
        return f"Ocurrió un error: {e}"

# Función para contar caracteres de todos los archivos .txt en una carpeta
def contar_caracteres_en_carpeta(carpeta):
    total_caracteres = 0
    archivos_txt = [f for f in os.listdir(carpeta) if f.endswith('.txt')]  # Lista de archivos .txt

    for archivo in archivos_txt:
        ruta_completa = os.path.join(carpeta, archivo)
        caracteres = contar_caracteres(ruta_completa)
        if isinstance(caracteres, int):
            print(f"El archivo '{archivo}' tiene {caracteres} caracteres.")
            total_caracteres += caracteres
        else:
            print(f"Error en el archivo '{archivo}': {caracteres}")
    
    return total_caracteres

# Ruta de la carpeta
carpeta = 'C:/Users/Usuario/Desktop/TAREA04-U01-G06/resultados_RIPEMD'

# Contar los caracteres totales en la carpeta
total = contar_caracteres_en_carpeta(carpeta)

# Imprimir el total de caracteres
print(f"El total de caracteres en todos los archivos .txt es {total}.")




