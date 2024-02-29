import tkinter as tk; from tkinter import *
import customtkinter as ctk
from tkinter import ttk, messagebox
from Back.consultas import mostrarAll,consultar_id,eliminar,eliminarTodo 
from Front.insertView import insert
from Front.updateView import update
from Front.helpView import help

def interfaz():
    #Creacion y configuracion de la interfaz 
    ventana = tk.Tk()
    ventana.title("CRUD Interfaz")
    
    #Para que la interfaz aparezca en el centro
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 860
    alto_ventana = 600
    x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    y = (alto_pantalla // 2) - (alto_ventana // 2)
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    
    ventana.resizable(False, False) #Hace que la ventana no modifique su tamaño
    
    #Colores
    rojo = "#D52020"
    azul = "#15213C"
    blanco = "#FFFFFF"
    negro = "#333"
    
    #Fuentes usadas
    font_title = ctk.CTkFont(family="Lucida Sans", size=17, weight="bold")
    font_text = ctk.CTkFont(family="Lucida Sans", size=15, weight="bold") 
    
    ventana.config(bg=azul)
    
    def llenar_campos(event):
        seleccionados = tabla.selection()
        if not seleccionados:
            return
        
        item = seleccionados[0]
        
        values = tabla.item(item, "values")
      
        e_id.delete(0, tk.END)
        e_id.insert(0, values[0])
    
    # Creacion de la  tabla
    tabla = ttk.Treeview(ventana, columns=("ID", "Nombre", "Correo", "Contraseña"), show="headings")
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Correo", text="Correo")
    tabla.heading("Contraseña", text="Contraseña")
    tabla.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    for col in tabla["columns"]:
        tabla.column(col, anchor="center")  
    mostrarAll(tabla)

    # Barras de desplazamiento vertical y horizontal
    scroll_y = tk.Scrollbar(ventana, orient="vertical",cursor='hand2',command=tabla.yview)
    scroll_y.grid(row=0, column=1, sticky="ns")
    tabla.configure(yscrollcommand=scroll_y.set)
    scroll_x = tk.Scrollbar(ventana, orient="horizontal",cursor='hand2', command=tabla.xview)
    scroll_x.grid(row=1, column=0, sticky="ew")
    tabla.configure(xscrollcommand=scroll_x.set)
    tabla.bind("<<TreeviewSelect>>", llenar_campos)
    
    #Funcion para actualizar la tabla cada vez que se haga una consulta
    def actualizar_tabla():
        tabla.delete(*tabla.get_children())
        mostrarAll(tabla)
    
    # Funcion para consultar pero para la tabla
    def consultar():
        id_usuario = e_id.get()
        if not id_usuario:
            actualizar_tabla()
            return
        resultado = consultar_id(id_usuario)
        if resultado:
            tabla.delete(*tabla.get_children())
            tabla.insert("", tk.END, text=resultado[0], values=resultado)
        else:
            messagebox.showinfo("Información", 
            "No se encontró ningún registro con el ID proporcionado")
    
    #Funcion para eliminar pero para la tabla
    def eliminar_registro():
        id_usuario = e_id.get() 
        if id_usuario: 
            try:
                id_usuario = int(id_usuario)
            except ValueError:
                messagebox.showerror("Error", "Por favor ingresa un ID válido para eliminar")
                return
            ids_en_tabla = [int(tabla.item(item)['values'][0]) for item in tabla.get_children()]
            if id_usuario in ids_en_tabla:
                if messagebox.askyesno("Eliminar", "¿Estás seguro que quieres eliminar este registro?"):
                    eliminar(id_usuario)
                    actualizar_tabla()
                    messagebox.showinfo("Éxito", "Usuario {} eliminado exitosamente".format(id_usuario))
                    e_id.delete(0, tk.END)  
            else:
                messagebox.showerror("Error", "El ID especificado no existe en la tabla")
        else:
            messagebox.showerror("Error", "Por favor ingresa un ID válido para eliminar")
    
    #Funcion para eliminar o vaciar todos los registros de la tabla
    def eliminarAll():
        if messagebox.askyesno("Eliminar", "¿Estás seguro que quieres eliminar este registro?"):
            eliminarTodo()
            actualizar_tabla()
            messagebox.showinfo("Éxito", "Usuarios eliminados exitosamente")
        else:
            messagebox.showerror("Error al eliminar los datos")
    

            
    
    #Labels
    label_main = tk.Label(ventana,
                          text="Para poder eliminar o buscar un registro, ingresa un ID:",
                          padx=10,
                          bg=azul,
                          font=font_title,
                          fg=blanco)
    label_main.place(x =170 , y =280)
    
    #Inputs
    e_id = ctk.CTkEntry(
        master=ventana, 
        width=150,
        height=40, 
        placeholder_text="Ingrese un id", 
        placeholder_text_color=negro,
        bg_color=azul,
        fg_color=blanco,
        text_color=rojo,
        font=font_text,
        border_color=rojo,)
    e_id.place(x =360 , y =330)
    
    #Botones
    btn_search = ctk.CTkButton(
        master= ventana,
        text= "Buscar",
        font= font_text,
        text_color=blanco,
        bg_color=azul,
        hover= True,
        hover_color= rojo,
        height=40,
        width= 120,
        border_width=2,
        corner_radius=10,
        border_color= blanco,
        command=consultar)
    btn_search.place(x =210 , y =330)
    
    btn_delete = ctk.CTkButton(
        master= ventana,
        text= "Eliminar",
        font= font_text,
        text_color=blanco,
        hover= True,
        hover_color= rojo,
        height=40,
        width= 120,
        border_width=2,
        corner_radius=10,
        border_color= blanco,
        command=eliminar_registro)
    btn_delete.place(x =540 , y =330)
    
    btn_insert = ctk.CTkButton(
        master= ventana,
        text= "Insertar",
        font= font_text,
        text_color=blanco,
        hover= True,
        hover_color= rojo,
        height=40,
        width= 120,
        border_width=2,
        corner_radius=10,
        border_color= blanco,
        command=insert)
    btn_insert.place(x =540 , y =400)
    
    btn_update = ctk.CTkButton(
        master= ventana,
        text= "Modificar",
        font= font_text,
        text_color=blanco,
        hover= True,
        hover_color= rojo,
        height=40,
        width= 120,
        border_width=2,
        corner_radius=10,
        border_color= blanco,
        command=update)
    btn_update.place(x =210 , y =400)
    
    btn_uptable = ctk.CTkButton(
        master= ventana,
        text= "Actualizar Tabla",
        font= font_text,
        text_color=blanco,
        hover= True,
        hover_color= rojo,
        height=40,
        width= 120,
        border_width=2,
        corner_radius=10,
        border_color= blanco,
        command=actualizar_tabla)
    btn_uptable.place(x =360 , y =400)
    
    btn_reset = ctk.CTkButton(
        master= ventana,
        text= "Vaciar registros",
        font= font_text,
        text_color=blanco,
        hover= True,
        hover_color= rojo,
        height=40,
        width= 120,
        border_width=2,
        corner_radius=10,
        border_color= blanco,
        command=eliminarAll)
    btn_reset.place(x =360 , y =470)
    
    btn_help = ctk.CTkButton(
        master= ventana,
        text= "Ayuda",
        font= font_text,
        text_color=blanco,
        hover= True,
        hover_color= rojo,
        height=40,
        width= 120,
        border_width=2,
        corner_radius=10,
        border_color= blanco,
        command=help)
    btn_help.place(x =210, y =470)
    
    btn_export = ctk.CTkButton(
        master= ventana,
        text= "Exportar",
        font= font_text,
        text_color=blanco,
        hover= True,
        hover_color= rojo,
        height=40,
        width= 120,
        border_width=2,
        corner_radius=10,
        border_color= blanco)
    btn_export.place(x =540, y =470)
    
    Labelby = ctk.CTkLabel(
        master=ventana,
        text="Creado por Shinji",
        font= font_text,
        text_color=blanco,
        )
    Labelby.place(x=365 ,y=560)
    
    ventana.mainloop() #Mandar a llamar la interfaz