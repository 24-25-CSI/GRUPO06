# Realice el cifrado de un mensaje por permutación de filas, teniendo como clave 5 filas y 
# la cantidad de columnas que sean necesarias(Garantice al menos 3) Los espacios del mensaje original se sustituyen con el carácter "-".
# Si en la matriz de cifrado sobran espacios, estos deben llenarse con el carácter "*"
# El algoritmo recibe el mensaje al iniciar y debe mostrar los siguientes resultados:
# El mensaje original
# La matriz de cifrado
# El mensaje cifrado
# En caso que se produzca algún error en la ejecución, el mismo debe mostrarse para alertar al usuario
#================================================================
# José Alejandro Jiménez Loor
#================================================================
 
import tkinter as tk
from tkinter import messagebox
import math

def encriptar_mensaje():
    try:
        #Se recibe el mensaje inicial //
        #En caso de estar vacio no lo cuenta y envia una alerta
        mensaje = entry_message.get()
        if not mensaje:
            raise ValueError("El mensaje no puede estar vacío.")

        #Reemplazo los espacios vacios por "-"
        mensajeLimpio = mensaje.replace(" ", "-")

        #Se selecciona el numero de columnas y de filas minimas
        filas = 5
        cols = max(3, math.ceil(len(mensajeLimpio) / filas))

        # Crear la matriz de cifrado
        matrix = []
        for i in range(filas):
            inicio = i * cols
            fin = inicio + cols
            fila = list(mensajeLimpio[inicio:fin])
            if len(fila) < cols:
                fila.extend(['*'] * (cols - len(fila)))
            matrix.append(fila)

        mensaje_encriptado = "".join(
            matrix[fila][col]
            for col in range(cols)
            for fila in range(filas)
            if col < len(matrix[fila])
        )

        text_original.config(state=tk.NORMAL)
        text_original.delete(1.0, tk.END)
        text_original.insert(tk.END, mensaje)
        text_original.config(state=tk.DISABLED)

        text_matrix.config(state=tk.NORMAL)
        text_matrix.delete(1.0, tk.END)
        for fila in matrix:
            text_matrix.insert(tk.END, " ".join(fila) + "\n")
        text_matrix.config(state=tk.DISABLED)

        text_encrypted.config(state=tk.NORMAL)
        text_encrypted.delete(1.0, tk.END)
        text_encrypted.insert(tk.END, mensaje_encriptado)
        text_encrypted.config(state=tk.DISABLED)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
#======================================================================================================#
root = tk.Tk()
root.title("Jajimenezl-ESI")

root.configure(background="lightgreen")
# Etiqueta y campo para el mensaje
label_message = tk.Label(root, text="Mensaje:",bg="lightgreen", fg="black")
label_message.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)

entry_message = tk.Entry(root, width=50)
entry_message.grid(row=0, column=1, padx=5, pady=5)

# Botón para cifrar
button_encrypt = tk.Button(root, text="Cifrar", command=encriptar_mensaje,bg="green", fg="white")
button_encrypt.grid(row=1, column=0, columnspan=2, pady=5)

# Textos para mostrar resultados
label_original = tk.Label(root, text="Mensaje Original:",bg="lightgreen", fg="black")
label_original.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

text_original = tk.Text(root, width=50, height=2, state=tk.DISABLED)
text_original.grid(row=2, column=1, padx=5, pady=5)

label_matrix = tk.Label(root, text="Matriz de Cifrado:",bg="lightgreen", fg="black")
label_matrix.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

text_matrix = tk.Text(root, width=50, height=10, state=tk.DISABLED)
text_matrix.grid(row=3, column=1, padx=5, pady=5)

label_encrypted = tk.Label(root, text="Mensaje Cifrado:",bg="lightgreen", fg="black")
label_encrypted.grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

text_encrypted = tk.Text(root, width=50, height=2, state=tk.DISABLED)
text_encrypted.grid(row=4, column=1, padx=5, pady=5)

root.mainloop()
