import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Diccionario base con carpetas por defecto y sus extensiones
categorias = {
    "Texto": [".txt", ".doc", ".docx"],
    "Imagen": [".jpg", ".gif", ".bmp", ".png"],
    "Video": [".avi", ".mp4", ".mwv", ".mpeg"],
    "Ejecución o del sistema": [".exe", ".bat", ".dll", ".sys"],
    "Audio": [".mp3", ".wav", ".wma"],
    "Archivos comprimidos": [".zip", ".rar", ".tar"],
    "Lectura": [".pdf", ".epub", ".azw", ".ibook"],
    "Imagen de disco": [".iso", ".mds", ".img"]
}

ruta_seleccionada = ""

def seleccionar_carpeta():
    global ruta_seleccionada
    ruta_seleccionada = filedialog.askdirectory()
    if ruta_seleccionada:
        etiqueta_ruta.config(text=f"📂 Carpeta seleccionada:\n{ruta_seleccionada}", fg="green")

def organizar_archivos():
    if not ruta_seleccionada:
        messagebox.showerror("Error", "Por favor selecciona una carpeta primero.")
        return

    ruta_organizados = os.path.join(ruta_seleccionada, "Archivos organizados")
    os.makedirs(ruta_organizados, exist_ok=True)

    rutas_categorias = {}
    for categoria in categorias:
        ruta_cat = os.path.join(ruta_organizados, categoria)
        os.makedirs(ruta_cat, exist_ok=True)
        rutas_categorias[categoria] = ruta_cat

    lista_archivos = os.listdir(ruta_seleccionada)

    for archivo in lista_archivos:
        archivo_ruta = os.path.join(ruta_seleccionada, archivo)
        if os.path.isfile(archivo_ruta):
            ext = os.path.splitext(archivo)[1].lower()
            for categoria, extensiones in categorias.items():
                if ext in extensiones:
                    shutil.move(archivo_ruta, os.path.join(rutas_categorias[categoria], archivo))
                    break

    messagebox.showinfo("Éxito", "¡Archivos organizados correctamente!")

def editar_categorias():
    categoria = simpledialog.askstring("Editar categoría", "Nombre de la categoría a editar:")
    if categoria and categoria in categorias:
        nuevas_ext = simpledialog.askstring("Nuevas extensiones", "Escribe las extensiones separadas por comas:")
        if nuevas_ext:
            lista_ext = [ext.strip() if ext.strip().startswith('.') else f".{ext.strip()}" for ext in nuevas_ext.split(',')]
            categorias[categoria] = lista_ext
            actualizar_vista_categorias()
            messagebox.showinfo("Actualizado", f"Extensiones actualizadas para '{categoria}'.")
    else:
        messagebox.showerror("Error", "Categoría no encontrada.")

def actualizar_vista_categorias():
    for widget in frame_categorias.winfo_children():
        widget.destroy()
    
    for categoria, extensiones in categorias.items():
        ext_texto = ", ".join(extensiones)
        label = tk.Label(frame_categorias, text=f"• {categoria}: {ext_texto}", anchor="w", justify="left", bg="#f0f0f0", font=("Segoe UI", 9))
        label.pack(fill="x", padx=10, pady=2)

# -------------------- Interfaz --------------------

ventana = tk.Tk()
ventana.title("Organizador de Archivos")
ventana.geometry("550x600")
ventana.configure(bg="#f0f0f0")

titulo = tk.Label(ventana, text="Organizador de Archivos 📁", font=("Segoe UI", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=15)

etiqueta_ruta = tk.Label(ventana, text="📍 Ninguna carpeta seleccionada", font=("Segoe UI", 10), fg="gray", bg="#f0f0f0")
etiqueta_ruta.pack()

frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=15)

btn_seleccionar = tk.Button(frame_botones, text="📂 Seleccionar carpeta", font=("Segoe UI", 11), command=seleccionar_carpeta)
btn_seleccionar.grid(row=0, column=0, padx=10)

btn_organizar = tk.Button(frame_botones, text="🚀 Organizar archivos", font=("Segoe UI", 11), bg="#4caf50", fg="white", command=organizar_archivos)
btn_organizar.grid(row=0, column=1, padx=10)

btn_editar = tk.Button(ventana, text="🛠️ Editar categorías", font=("Segoe UI", 10), command=editar_categorias)
btn_editar.pack(pady=(5, 0))

label_categorias = tk.Label(ventana, text="📦 Categorías activas:", font=("Segoe UI", 11, "bold"), bg="#f0f0f0")
label_categorias.pack(pady=(20, 0))

frame_categorias = tk.Frame(ventana, bg="#f0f0f0")
frame_categorias.pack(padx=15, pady=(5, 20), fill="both", expand=True)

actualizar_vista_categorias()

creditos = tk.Label(ventana, text="Desarrollado por Yony Chaparro", font=("Segoe UI", 8), fg="gray", bg="#f0f0f0")
creditos.pack(side="bottom", pady=10)

ventana.mainloop()
