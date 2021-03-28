from collections import namedtuple
import sys
import time

# Creación de la clase Usuario
class Usuario:

    def __init__(self, usuario):
        self.usuario = usuario
        self.contactos = []
        self.grupos = []



#Creación de la clase Grupo
class Grupo:

    def __init__(self,grupo):
        self.grupo = grupo
        self.integrantes = []
        self.mensajes = []



#Creación de la clase Chat
class Chat:

    def __init__(self, chat):
        self.chat = chat
        #self.integrantes = [] esto no se
        self.mensajes = []

#Creación de la clase Menu
class Menu:

#Init
    def __init__(self):
        usuario_actual = ''
# Creación menú inicio
    def menu_de_inicio(self):
        print(f"\n***** Menú de inicio *****\n\n[1] Crear usuario\n[2] Iniciar sesión\n[0] salir"
            "\n\n"
            "Indique su opción (0, 1 o 2): ")
        opcion = input()
        if opcion == "0":
            self.salir()
        elif opcion == "1":
            self.crear_usuario()
        elif opcion == "2":
            self.iniciar_sesion()
        else:
            print("Ha elegido una opción invalida. Por favor vuelva a intentarlo.")
            self.menu_de_inicio()
#Creación Salir
    def salir(self):
        sys.exit("Has dedicido salir de DCConecta2."
                "¡Esperamos verte nuevamente!")

#Creación crear_usuario
    def crear_usuario(self):
        print(f"\n¡Que bueno que quieras sumarte a DCConecta2!\n ¿Que nombre deseas tener?")
        nombre_usuario = str(input())
        lista_usuarios_str = []
        for usuario in lista_usuarios:
            lista_usuarios_str.append(usuario.usuario)
        if (nombre_usuario not in lista_usuarios_str and \
            len(nombre_usuario)>2 and len(nombre_usuario)<16 and \
            "," not in nombre_usuario):   

                lista_usuarios.append(Usuario(nombre_usuario))
                print ("\nFelicitaciones, has sido registrado con éxito.")                   
                with open("usuarios.csv") as csv:
                    usuarios_csv = csv.readlines()
                    usuarios_csv.append(f"{nombre_usuario}\n")

                with open("usuarios.csv","w") as csv:
                    for usuario in usuarios_csv:
                        csv.write(usuario)
                
                self.menu_de_chats()

        else:
            print("-- Este usuario ya está registrado o no cumple"
              " con los requisitos :( -- \nVolverás al menú de inicio.")
            self.menu_de_inicio()

#Creación iniciar_sesion
    def iniciar_sesion(self):
        print(f"\nIngrese su nombre de usuario:")
        nombre_usuario_sesion = input()
        with open("usuarios.csv") as csv: #Usar os.path.join
            lista_usuarios_2 = csv.readlines()
            lista_usuarios_2.pop(0)
            for indice in range(len(lista_usuarios_2)):
                lista_usuarios_2[indice] = lista_usuarios_2[indice].strip('\n')

        if  nombre_usuario_sesion in lista_usuarios_2:
            print(f"\nHa ingresado con exito.\nCargando Menú de Chats...")
            for usuario in lista_usuarios:
                if nombre_usuario_sesion == usuario.usuario:
                    self.usuario_actual = usuario
            self.menu_de_chats()
        else:
            print(f"El nombre de usuario es invalido. :(\nVolviendo al Menú de Inicio.")
            self.menu_de_inicio()

#Creación menu chats. Menú de contactos en proceso. Menu de grupos no empezado.
    def menu_de_chats(self):
        print(f"\n***** Menú de chats *****\n\n[1] Menú de Contactos\n[2]"
            " Menú de grupos\n[0] Volver"
            "\n\n"
            "Indique su opción (0, 1 o 2): ")
        opcion = input()
        if opcion == "0":
            self.menu_de_inicio()
        elif opcion == "1":
            self.menu_de_contactos()
        elif opcion == "2":
            self.menu_de_grupos()
        else:
            print("Ha elegido una opción invalida. Por favor vuelva a intentarlo.")
            self.menu_de_chats()
        
#Creación menu de contactos
    def menu_de_contactos(self):
        print(f"\n***** Menú de contactos *****\n\n[1] Ver contactos\n[2] Añadir contactos\n"
            "[0] Volver"
            "\n\n"
            "Indique su opción (0, 1 o 2): ")
        opcion = input()
        if opcion == "0":
            self.menu_de_chats()
        elif opcion == "1":
            self.ver_contactos()
        elif opcion == "2":
            self.añadir_contacto()
        else:
            print("Ha elegido una opción invalida. Por favor vuelva a intentarlo.")
            self.menu_de_contactos()       

#Creación Ver Contactos
    def ver_contactos(self):
        print(f"\n***** Ver contactos *****\n\nSelecciona un usuario para ver tus conversaciones,"
            "\no 0 para volver al menú de contactos:"
            "\n")
        lista_ver_contactos = []
        for indice in range(len(self.usuario_actual.contactos)):
            lista_ver_contactos.append([indice + 1,self.usuario_actual.contactos[indice]])
        for contacto in lista_ver_contactos:
            usuario = contacto[1]
            print(f"[{contacto[0]}] {usuario.usuario}")
        print("\nIngresa un valor: ")
        opcion = input()
        if str(opcion) == "0":
            self.menu_de_contactos()
        integrantes_del_chat = [self.usuario_actual.usuario]
        for indice in range(len(lista_ver_contactos)):
            if opcion == str(lista_ver_contactos[indice][0]):
                integrantes_del_chat.append(lista_ver_contactos[indice][1].usuario)
        print(f"\n***** Tu historial con {integrantes_del_chat[1]} *****\n")
        for mensaje in lista_mensajes_chats:
            if mensaje.emisor in integrantes_del_chat and mensaje.receptor in integrantes_del_chat:
                print(f"|{mensaje.fecha_emision}| {mensaje.emisor}: {mensaje.contenido}")
        print(f"\n***** Fin del historial con {integrantes_del_chat[1]} *****")
        print("\nAgregar mensaje: ")
        nuevo_mensaje = str(input())
        while nuevo_mensaje != "\\\\volver":

            fecha = time.strftime("%Y/%m/%d %H:%M:%S")
            mensaje_completo = Mensaje(integrantes_del_chat[0],integrantes_del_chat[1],
                            fecha,nuevo_mensaje)
            lista_mensajes_chats.append(mensaje_completo)
            print(f"\n|{mensaje_completo.fecha_emision}|\
 {mensaje_completo.emisor}: {mensaje_completo.contenido}")

            with open("mensajes.csv") as csv:
                mensajes_csv = csv.readlines()
                mensajes_csv.append(f"regular,{mensaje_completo.emisor},\
{mensaje_completo.receptor},{fecha},{nuevo_mensaje}\n")


            with open("mensajes.csv","w") as csv:
                for mensaje in mensajes_csv:
                    csv.write(mensaje)

            nuevo_mensaje = str(input())

        if nuevo_mensaje == "\\\\volver":
            self.menu_de_contactos()

#Creación añadir contacto
    def añadir_contacto(self):
        print("\nIngrese el nombre de usuario que desea agregar: ")
        nombre_usuario_agregar = input()
        lista_de_usuarios_str = []
        contactos_actuales = []
        for contacto in self.usuario_actual.contactos:
            contactos_actuales.append(contacto.usuario)
        if nombre_usuario_agregar not in contactos_actuales:
            for usuario in lista_usuarios:
                lista_de_usuarios_str.append(usuario.usuario)
                if usuario.usuario == nombre_usuario_agregar:
                    self.usuario_actual.contactos.append(usuario)
                    usuario.contactos.append(self.usuario_actual)

                    with open("contactos.csv") as csv:
                        contactos_csv = csv.readlines()
                        contactos_csv.append(f"{self.usuario_actual.usuario},{usuario.usuario}\n")


                    with open("contactos.csv","w") as csv:
                        for contacto in contactos_csv:
                            csv.write(contacto)

                    print("\nEl usuario ha sido añadido con éxito.")
                    self.menu_de_contactos()


            if nombre_usuario_agregar not in lista_de_usuarios_str:
                print("\nLo lamentamos, el usuario que ingresaste no existe.")
                self.menu_de_contactos()
        elif nombre_usuario_agregar in contactos_actuales:
            print("\nEl contacto que deseas agregar ya está dentro de tu lista.")
            self.menu_de_contactos()

#Creación menú de grupos
    def menu_de_grupos(self):
        print(f"\n***** Menú de grupos *****\n\n[1] Ver grupos\n[2]"
                " Crear grupo\n[0] Volver"
                "\n\n"
                "Indique su opción (0, 1 o 2): ")
        opcion = input()
        if opcion == "0":
            self.menu_de_chats()
        elif opcion == "1":
            self.ver_grupos()
        elif opcion == "2":
            self.crear_grupo()
        else:
            print("Ha elegido una opción invalida. Por favor vuelva a intentarlo.")
            self.menu_de_grupos()

#Creación crear grupo
    def crear_grupo(self):
        print(f"\n¿Que grupo deseas crear?\nInserta su nombre: ")
        nombre_grupo = str(input())
        print("\nIngrese a los usuarios: (Usando el formato usuario1;usuario2...)\n")
        usuarios_grupo = [input()]
        usuarios_grupo = usuarios_grupo[0].split(";")
        lista_grupos_str = []
        for grupo in lista_grupos:
            lista_grupos_str.append(grupo.grupo)
        lista_usuarios_str = []
        for usuario in lista_usuarios:
            lista_usuarios_str.append(usuario.usuario)

        if (nombre_grupo not in lista_grupos_str and len(nombre_grupo)>0 \
            and "," not in nombre_grupo and len(usuarios_grupo)>1 \
            and usuarios_grupo[0] in lista_usuarios_str \
            and usuarios_grupo[1] in lista_usuarios_str):   

                lista_grupos.append(Grupo(nombre_grupo))
                print ("\nEl grupo ha sido creado con éxito.")                   
                
                with open("grupos.csv") as csv:
                    grupos_csv = csv.readlines()
                    for usuario in usuarios_grupo:
                        grupos_csv.append(f"{nombre_grupo},{usuario}\n")

                with open("grupos.csv","w") as csv:
                    for grupo in grupos_csv:
                        csv.write(grupo)
                
                self.menu_de_grupos()

        else:
            print("-- Este grupo ya está registrado o no cumple"
              " con los requisitos :( -- \nVolverás al menú de grupos.")
            self.menu_de_grupos()

#Ver grupos
    def ver_grupos(self):

        print(f"\n***** Ver grupos *****\n\nSelecciona un grupo para ver las conversaciones,"
            "\no 0 para volver al menú de grupos:"
            "\n")
        lista_ver_grupos = []
        indice = 1
        for grupo in lista_grupos:
            for integrante in grupo.integrantes:
                if integrante == self.usuario_actual:
                    lista_ver_grupos.append([indice,grupo])
                    indice += 1

        for grupo in lista_ver_grupos:
            nombre_grupo = grupo[1]
            print(f"[{grupo[0]}] {nombre_grupo.grupo}")

        print("\nIngresa un valor: ")
        opcion = input()
        if str(opcion) == "0":
            self.menu_de_grupos()

        grupo_actual = " "
        for indice in range(len(lista_ver_grupos)):
            if opcion == str(lista_ver_grupos[indice][0]):
                grupo_actual = lista_ver_grupos[indice][1]

        print(f"\n***** Historial de {grupo_actual.grupo} *****\n")
        for mensaje in grupo_actual.mensajes:
            print(f"{mensaje[3]}, {mensaje[1]}: {mensaje[-1]}")
        print(f"\n***** Fin del historial de {grupo_actual.grupo} *****")
        print("\nAgregar mensaje: ")
        nuevo_mensaje = str(input())
        while nuevo_mensaje != "\\\\volver" and nuevo_mensaje != "\\\\salir":

            fecha = time.strftime("%Y/%m/%d %H:%M:%S")
            mensaje_completo = (f"{fecha}, {self.usuario_actual.usuario}: {nuevo_mensaje}")
            lista_mensajes_grupos.append(mensaje_completo)
            print(f"\n{mensaje_completo}")

            with open("mensajes.csv") as csv:
                mensajes_grupo_csv = csv.readlines()
                mensajes_grupo_csv.append(f"\ngrupo,{self.usuario_actual.usuario},\
{grupo_actual.grupo},{fecha},{nuevo_mensaje}")


            with open("mensajes.csv","w") as csv:
                for mensaje in mensajes_grupo_csv:
                    csv.write(mensaje)

            nuevo_mensaje = str(input())

        if nuevo_mensaje == "\\\\volver":
            self.ver_grupos()

        elif nuevo_mensaje =="\\\\salir":
            grupo_actual.integrantes.remove(self.usuario_actual)
            print(f"El usuario {self.usuario_actual.usuario} ha abandonado el grupo.")
            self.ver_grupos()




#Creación de los usuarios como objetos de la clase Usuario.
with open("usuarios.csv") as csv: #Usar os.path.join
    lista_usuarios = csv.readlines()
    lista_usuarios.pop(0)
    for indice in range(len(lista_usuarios)):
        lista_usuarios[indice] = lista_usuarios[indice].strip('\n')
        lista_usuarios[indice] = Usuario(lista_usuarios[indice])
        
#Creación self.contactos como objetos.  
with open("contactos.csv") as csv: #Usar os.path.join
    lista_contactos = csv.readlines()
    lista_contactos.pop(0)
    for indice in range(len(lista_contactos)):
        lista_contactos[indice] = lista_contactos[indice].strip('\n').split(",")
for indice in range(len(lista_contactos)):
    for usuario in lista_usuarios:
        for usuario_2 in lista_usuarios:
            if lista_contactos[indice][0] == usuario.usuario:
                if lista_contactos[indice][1] == usuario_2.usuario:
                    usuario.contactos.append(usuario_2)
    
# Creación de los grupos como objetos
with open("grupos.csv") as csv: #Usar os.path.join
    lista_grupos_temporal = csv.readlines()
    lista_grupos_temporal.pop(0)

# Crear el grupo como objeto
    for indice in range(len(lista_grupos_temporal)):
        lista_grupos_temporal[indice] = lista_grupos_temporal[indice].strip('\n').split(",")

    lista_grupos = []
    for indice in range(len(lista_grupos_temporal)):
        if lista_grupos_temporal[indice][0] not in lista_grupos:
            lista_grupos.append(lista_grupos_temporal[indice][0])
    for indice in range (len(lista_grupos)):
        lista_grupos[indice] = Grupo(lista_grupos[indice])
        
# Agregar a los integrantes
    for grupo in lista_grupos:
        for indice in range (len(lista_grupos_temporal)):
            for usuario in lista_usuarios:
                if lista_grupos_temporal[indice][0] == grupo.grupo:
                    if lista_grupos_temporal[indice][1] == usuario.usuario:
                        if lista_grupos_temporal[indice][1] not in grupo.integrantes:
                            grupo.integrantes.append(usuario)

#Creación y almacenamiento de los mensajes.
with open("mensajes.csv") as csv: #Usar os.path.join
    lista_mensajes = csv.readlines()
    lista_mensajes.pop(0)
    for indice in range(len(lista_mensajes)):
        lista_mensajes[indice] = lista_mensajes[indice].strip('\n').split(",",maxsplit = 4)
 
#Separación de mensajes de grupo y de chats
lista_mensajes_grupos = []
lista_mensajes_chats = []
for indice in range(len(lista_mensajes)):

#Mensajes de grupo
    if lista_mensajes[indice][0] == "grupo":
        lista_mensajes_grupos.append(lista_mensajes[indice])
        for grupo in lista_grupos:
            if lista_mensajes[indice][2] == grupo.grupo:
                grupo.mensajes.append(lista_mensajes[indice])

#Mensajes de chats. Se usan como Namedtuple

    if lista_mensajes[indice][0] == "regular":
        lista_mensajes_chats.append(lista_mensajes[indice])
    
Mensaje = namedtuple('mensaje',['emisor', 'receptor', 'fecha_emision', 'contenido'])
for indice in range(len(lista_mensajes_chats)):
    mensaje = lista_mensajes_chats[indice]
    lista_mensajes_chats[indice] = Mensaje(mensaje[1],mensaje[2],mensaje[3],mensaje[4])


menu = Menu()
menu.menu_de_inicio()