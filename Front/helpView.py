import tkinter as tk

def help():
    root = tk.Tk()
    root.title("¿Como usar la app?")
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    ancho_ventana = 800
    alto_ventana = 300
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    root.resizable(False, False) #Hace que la ventana no modifique su tamaño

    texto_label3="3º Para buscar un registro coloca un ID y pulsa el botón de Buscar y te mostrara unicamente ese registro.\nSi quieres regresar a la tabla con todos los registros,solo borra el ID y vuelve a presionar el botón de Buscar."

    label1 = tk.Label(root, text=" 1º Para crear la base de datos usa el respaldo para que restaures la DB ya viene todo ahi")
    label1.config(font=("Arial", 10, "bold"))
    label2 = tk.Label(root, text=" 2º Para eliminar un registro solo coloca el id del registro y presiona el boton de eliminar")
    label2.config(font=("Arial", 10, "bold"))
    label3 = tk.Label(root, text=texto_label3,justify="left")
    label3.config(font=("Arial", 10, "bold"))
    label4 = tk.Label(root, text="4º Para insertar o modificar solo presiona su boton correspondiente para que muestre el formulario")
    label4.config(font=("Arial", 10, "bold"))
    label5 = tk.Label(root, text="5º Para mostrar los cambios en la tabla  despues de una modificacion , eliminacion o inserccion solo preiosna \nel boton de actualizar tabla",justify="left")
    label5.config(font=("Arial", 10, "bold"))

    label1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    label2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    label3.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    label4.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    label5.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
    root.mainloop()

