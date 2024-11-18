import os

# Directorio para guardar los archivos
directorio_salida = "archivos_generados"
os.makedirs(directorio_salida, exist_ok=True)

# Cantidades de palabras para los archivos
cantidades_palabras = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

# Generador de texto general
def generar_texto(cantidad_palabras):
    frases_comunes = [
        "El rápido zorro marrón salta sobre el perro perezoso.",
        "La inteligencia artificial está transformando el mundo.",
        "Aprender nunca termina, y el conocimiento es poder.",
        "Explorar lo desconocido es la esencia de la humanidad.",
        "El sol sale por el este y se pone por el oeste.",
        "La tecnología y la innovación van de la mano.",
        "La naturaleza guarda la clave de nuestra satisfacción estética, intelectual, cognitiva y espiritual.",
        "Los libros son una magia portátil única.",
        "El viaje de mil millas comienza con un solo paso.",
        "La felicidad no es algo hecho; viene de tus propias acciones.",
        "El agua es esencial para la vida y nuestro bienestar.",
        "La música es el lenguaje universal que conecta a las personas.",
        "Cada día es una nueva oportunidad para crecer y aprender.",
        "El respeto por los demás es la base de una sociedad armoniosa.",
        "Las estrellas nos recuerdan lo vasto que es el universo.",
        "Una sonrisa puede cambiar el día de alguien.",
        "La paciencia es la clave para superar los retos de la vida.",
        "Trabajar en equipo es esencial para alcanzar grandes metas.",
        "El tiempo es el recurso más valioso que tenemos.",
        "El esfuerzo constante es el camino hacia el éxito.",
        "La creatividad es la chispa que enciende la innovación.",
        "Viajar expande la mente y alimenta el alma.",
        "El aprendizaje es un tesoro que te acompañará siempre.",
        "La familia es el pilar fundamental de nuestras vidas.",
        "Las pequeñas acciones generan grandes impactos en el mundo."
    ]
    
    # Repetir frases para alcanzar el número de palabras deseado
    texto = " ".join(frases_comunes * (cantidad_palabras // len(frases_comunes) + 1))
    return " ".join(texto.split()[:cantidad_palabras])

# Crear archivos
for cantidad in cantidades_palabras:
    nombre_archivo = f"{cantidad}.txt"
    ruta_archivo = os.path.join(directorio_salida, nombre_archivo)
    contenido_texto = generar_texto(cantidad)
    
    with open(ruta_archivo, "w") as archivo:
        archivo.write(contenido_texto)

print(f"Archivos generados en el directorio: {directorio_salida}")
