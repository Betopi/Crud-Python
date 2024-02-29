import tkinter as tk
from tkinter import messagebox
from Back.consultas import actualizar

def update():
        # Función para modificar un registro existente
    def modifica_registro():
        id = entry_id.get()
        username = entry_nombre.get()
        email = entry_correo.get()
        password = entry_contraseña.get()
        
        if id and username and email and password:
            try:
                actualizar(id, username, email, password)
                messagebox.showinfo("Éxito", "Usuario modificado exitosamente")
                root.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al modificar usuario: {e}")
        else:
            messagebox.showerror("ERROR", "Por favor completa todos los campos")
            
            
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Formulario de actualizar")
    
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    ancho_ventana = 290
    alto_ventana = 180
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)
    root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")


# ID
    label_id = tk.Label(root, text="ID :")
    label_id.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_id = tk.Entry(root)
    entry_id.grid(row=0, column=1, padx=10, pady=5)

    # Nombre
    label_nombre = tk.Label(root, text="Nombre:")
    label_nombre.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_nombre = tk.Entry(root)
    entry_nombre.grid(row=1, column=1, padx=10, pady=5)

    # Correo
    label_correo = tk.Label(root, text="Correo electrónico:")
    label_correo.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_correo = tk.Entry(root)
    entry_correo.grid(row=2, column=1, padx=10, pady=5)

    # Contraseña
    label_contraseña = tk.Label(root, text="Contraseña:")
    label_contraseña.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_contraseña = tk.Entry(root, show="*")
    entry_contraseña.grid(row=3, column=1, padx=10, pady=5)

    # Botón de enviar
    boton_enviar = tk.Button(root, text="Enviar",command=modifica_registro)
    boton_enviar.grid(row=4, columnspan=2, padx=10, pady=10)

    # Ejecutar el bucle principal de la aplicación
    root.mainloop()