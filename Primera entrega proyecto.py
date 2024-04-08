import shutil, os


ruta_actual=os.getcwd()                                                     # Ruta donde se guardo este archico y donde se desea hacer una organizacion de archivos    
lista_archivos=os.listdir(ruta_actual)                                      # Lista con los nombres de los archivos que existen en ruta_actual 
crear_carpetas=["Archivos organizados\\Texto", "Archivos organizados\\Imagen", "Archivos organizados\\Video", "Archivos organizados\\Ejecucion o del sistema", "Archivos organizados\\Audio", "Archivos organizados\\Archivos comprimidos", "Archivos organizados\\Lectura", "Archivos organizados\\Imagen de disco"]

# Rutas para organizar los archivos 
a1=os.path.join(ruta_actual,crear_carpetas[0])   # texto
a2=os.path.join(ruta_actual,crear_carpetas[1])   # imagen
a3=os.path.join(ruta_actual,crear_carpetas[2])   # vídeo
a4=os.path.join(ruta_actual,crear_carpetas[3])   # ejecución o del sistema
a5=os.path.join(ruta_actual,crear_carpetas[4])   # audio
a6=os.path.join(ruta_actual,crear_carpetas[5])   # archivo comprimido
a7=os.path.join(ruta_actual,crear_carpetas[6])   # lectura
a8=os.path.join(ruta_actual,crear_carpetas[7])   # imagen de disco

#Archivos a organizar
texto=[".txt",".doc",".docx"]                      # a1
imagen=[".jpg",".gif",".bmp",".png"]               # a2
video=[".avi",".mp4",".mwv",".mpeg"]               # a3
ejecucion=[".exe",".bat",".dll",".sys"]            # a4
audio=[".mp3",".wav",".wma"]                       # a5
archivo=[".zip",".rar",".tar"]                     # a6
lectura=[".pdf",".epub",".azw","ibook"]            # a7
imagen_disco=[".iso",".mds",".img"]                # a8


# Funcion para crear la carpetas en donde se organizaran los archivos
def funcion1():                                                             # Funcion para crear las 8 carpetas en donde se organizaran los archivos  
    global ruta_actual                                                      
    global crear_carpetas 
    global lista_archivos                                                 # Carpetas que se crearan si no existe la carpeta "Archivos organizados"
    if "Archivos organizados" in lista_archivos:
        return
    else:
        os.makedirs(os.path.join(ruta_actual,"Archivos organizados"))
        
        for i in crear_carpetas:
            os.makedirs(os.path.join(ruta_actual,i))
        return    
         

# Funcion para organizar los archivos
def funcion2():
    global a1,a2,a3,a4,a5,a6,a7,a8
    global texto,imagen,video,ejecucion,audio,archivo,lectura,imagen_disco
    global ruta_actual,lista_archivos
    
    
    for filename in lista_archivos:                      # Organiza archivos texto
        for i in texto:
            if filename.endswith(i):                                                                  
                a=os.path.join(ruta_actual, filename)    
                shutil.move(a,a1) 
                
    for filename in lista_archivos:                      # Organiza archivos imagen 
        for i in imagen:
            if filename.endswith(i):                                                                  
                a=os.path.join(ruta_actual, filename)    
                shutil.move(a,a2) 
                
    for filename in lista_archivos:                       # Organiza archivos video
        for i in video:
            if filename.endswith(i):                                                                  
                a=os.path.join(ruta_actual, filename)    
                shutil.move(a,a3) 
                
    for filename in lista_archivos:                      # Organiza archivos de ejecución o del sistema   
        for i in ejecucion:
            if filename.endswith(i):                                                                  
                a=os.path.join(ruta_actual, filename)    
                shutil.move(a,a4)

    for filename in lista_archivos:                       # Organiza archivos audio
        for i in audio:
            if filename.endswith(i):                                                                  
                a=os.path.join(ruta_actual, filename)    
                shutil.move(a,a5)

    for filename in lista_archivos:                       # Organiza archivos archivo comprimido
        for i in archivo:
            if filename.endswith(i):                                                                  
                a=os.path.join(ruta_actual, filename)    
                shutil.move(a,a6)

    for filename in lista_archivos:                       # Organiza archivos archivo lectura
        for i in lectura:
            if filename.endswith(i):                                                                  
                a=os.path.join(ruta_actual, filename)    
                shutil.move(a,a7)

    for filename in lista_archivos:                       # Organiza archivos imagen de disco
        for i in imagen_disco:
            if filename.endswith(i):                                                                  
                a=os.path.join(ruta_actual, filename)    
                shutil.move(a,a8)                



funcion1()
funcion2()
