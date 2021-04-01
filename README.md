# Tarea 0: DCConecta2 :school_satchel:

<!-- Logotipo del proyecto -->
<br />
<p align="center">
    <img src="imagenes\logo_DCC.png" alt="Logo" width="320" height="320">
  </a>
  <h3 align="center">T0: DCConecta2</h3>

  <p align="center">
    prototipo para un nuevo sistema de mensajería llamado DCConecta2.
    <br />
    <br />
  </p>
</p>



<!-- Tabla de contenidos -->
<details open="open">
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#resumen-y-propósito-del-programa">Resumen y propósito del programa ⛱️</a>
      <ul>
        <li><a href="#cosas-no-implementadas">Cosas no implementadas ❌</a></li>
        <li><a href="#cosas-si-implementadas">Cosas si implementadas ✅</a></li>
      </ul>
    </li>
    <li><a href="#ejecución-y-explicación-de-archivos">Ejecución y explicación de archivos 💻</a></li>
    <li>
      <a href="#librerías">librerias 📚</a>
      <ul>
        <li><a href="#librerías-externas">Librerías externas📗</a></li>
        <li><a href="#librerías-propias">Librerías propias📘</a></li>
      </ul>
    </li>
    <li><a href="#supuestos-y-consideraciones-adicionales">Supuestos y consideraciones adicionales 🤔</a></li>
    <li><a href="#referencias-de-código-externo">Referencias de código externo🤑</a></li>
  </ol>
</details>
<!-- Fin tabla de contenidos -->

-------
## Resumen y propósito del programa

Debido a la repentina alza en la demanda de redes sociales se han provocado graves saturaciones y demoras, por lo que el equipo de ayudantes UC ha quedado sin comunicación entre ellos 🙃. Es por esto que se realizó un prototipo para un nuevo sistema de mensajeria solo para ayudantes. Este permite, entre otras cosas, registrarse, iniciar sesión, hablar con los contactos y con los grupos a los que pertenezca.
>
En un futuro se buscará implementar números telefónicos y sincronizar los contactos del telefono con los contactos de DCConecta2, para una mejor experiencia.del usuario. 🧠🦈

### Cosas no implementadas

* Se trató de corregir todos los errores posibles, espero no tener alguno. 🙀

### Cosas si implementadas
(Basado en el archivo <a href="https://docs.google.com/spreadsheets/d/1syXt9wmuk63mAsdMUyX5GLkyqFr3VgKQdCPOHpOz9_g/edit#gid=1192691986">T0: Distribución de Puntaje</a>)
* **Menú de inicio**:
  * **Requisitos**: El menú de Inicio contiene todas las opciones pedidas en el enunciado.
  *  **Iniciar sesión**: El usuario puede ingresar sesión, se verifica que el usuario exista en *usuarios.csv*. Si se ingresa un nombre no válido se informa y se vuelve al Menú de Inicio.
  *  **Registrar usuario**: Al registrar un usuario se verifica: Que se cumplan los requisitos solicitados, que el nombre no exista en *usuarios.csv*. Si ello se cumple, se guarda el nombre de usuario en *usuarios.csv*; caso contrario, se notifica y se vuelve al Menú de Inicio.
  *  **Salir**: Se logra salir correctamente mediante el uso de *sys.exit()*.

* **Flujo de programa**:
  >
  * **Menú de Chats**: El menú cumple con las opciones pedidas y se puede volver al Menú de Inicio.
  >
  *  **Menú de Contactos**: El menú tiene las opciones **[1]** Ver Contactos, **[2]** Añadir Contacto y **[0]** Volver al Menú de Chats.
  >
     * * **[1] Ver Contactos**: Se muestran todos los contactos del usuario de manera correcta. Al seleccionar un contacto, se despliega el historial, se actualiza y se guardan los mensajes escritos en *mensajes.csv* correctamente. Al escribir el parámetro VOLVER_FRASE el usuario vuelve a la opción Ver Contactos.
  >
     * * **[2] Añadir contacto**: El contacto se agrega de manera correcta, verificando que sea válido. De ser así, es guardado en *contactos.csv*; en caso contrario, se notifica y se vuelve al Menú de Contactos.
     * * **[0] Volver al Menú de Chats**: Esto se logra sin problemas.
  >
  *  **Menú de Grupos**: El menú tiene las opciones **[1]** Ver Grupos, **[2]** Añadir Grupo y **[0]** Volver al Menú de Chats.
  >
     * * **[1] Ver Grupos**: Se muestran todos los grupos del usuario de manera correcta. Al seleccionar un grupo, se despliega el historial, se actualiza y se guardan los mensajes escritos en *mensajes.csv* correctamente. Al escribir el parámetro VOLVER_FRASE, el usuario vuelve a la opción Ver Contactos y al escribir el parámetro ABANDONAR_FRASE, el usuario abandona el grupo, se envía un mensaje predeterminado que se guarda en *mensajes.csv*, se actualiza *grupos.csv* y luego vuelve a la opción Ver Grupos.
  >
     * * **[2] Añadir Grupo**: El grupo se agrega de manera correcta, verificando que sea válido, cumpla con las condiciones solicitadas y los usuario existan y cumplan el formato. De ser así, es guardado con los usuarios pertinentes en *grupos.csv*; en caso contrario, se notifica y se vuelve al Menú de Grupos. Ver (2) en <a href="#supuestos-y-consideraciones-adicionales">Supuestos y consideraciones adicionales :thinking: </a>.
  >
     * * **[0] Volver al Menú de Chats**: Esto se logra sin problemas.
  >
  * **Chats**: En los chats (regulares y de grupo) se muestran los mensajes de forma separada y de manera ascendente, mostrando fecha, hora, emisor y el contenido.
  >
  * **Archivos**: Los ***usuarios.csv***, ***contactos.csv***, ***mensajes.csv*** y ***grupos.csv*** se trabajan de manera correcta, respetando el formato. Ver (3) en <a href="#supuestos-y-consideraciones-adicionales">Supuestos y consideraciones adicionales :thinking: </a>
  >
* **General**:
  >
    * **Menús**: Los menús son *a prueba de fuego*:fire: (Aceptan **todo** tipo de error).
  >
    * **Parámetros**: Se utilizan los parámetros dentro del programa y se importa el módulo de forma correcta. Ver (1) en <a href="#supuestos-y-consideraciones-adicionales">Supuestos y consideraciones adicionales :thinking:</a>.
  >
    * **PEP8**: El programa respeta PEP8. Ver (4) en <a href="#supuestos-y-consideraciones-adicionales">Supuestos y consideraciones adicionales :thinking:</a>

-------
## Ejecución y explicación de archivos
El módulo principal de la tarea a ejecutar es  ```main.py```. Se muestran los otros archivos de la carpeta y un resumen de sus existencias:
1. ```clase_menu_e_instanciacion.py```: Contiene la clase Menu (y sus funciones) y la instanciación del programa (el manejo de los archivos .csv).
   >
2. ```clases_y_funciones.py```: Contiene las clases Usuario, Grupo y Chat. Además contiene la función *get_input*.
   >
3. ```parametros.py```: Contiene los parámetros utilizados en el programa.
   >
4. ```imagenes```: Contiene imagenes presentadas en el README.
   
-------

## Librerías

### Librerías externas
La lista de librerías externas que utilicé fue la siguiente:

1. ```collections```: ```namedtuple()```
>
2. ```datatime```: ```datatime()```
>
3. ```sys```: ```sys.exit()``` (No se importó la función especifica para que se entendiera mejor la utilización de la función).
>
4. ```os```: ```os.path.join()``` (No se importó la función especifica para que se entendiera mejor la utilización de la función).

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```clase_menu_e_instanciación.py```: Contiene la clase ```Menu```. En esta clase están todas las funciones que permiten ejecutar el programa que se realicen los comandos pedidos por el usuario. Todos los menús y chats se encuentran en este clase.
>
2. ```clases_y_funciones.py```: Contiene las clases ```Usuario```, ```Grupo``` y ```Chat```. Estas clases permiten almacenar todos los datos de los archivos *.csv*, permitiendo una buena y útil separación de la información. Además se encuentra la función ```get_input()``` que es explicada en <a href="#referencias-de-código-externo">Referencias de código externo🤑</a>

-------
## Supuestos y consideraciones adicionales

* **(1)** Al usar los parámetros VOLVER_CLASE y ABANDONAR_CLASE se debe considerar que utilizan *backslash* por lo que se debe utilizar un *backslash* menos en el input (En vez de escribir '\\volver' se debe escribir solo '\volver')
  >
* **(2)** Al crear un grupo, ya se considera el usuario actual como un integrante por lo que es necesario ingresar mínimo un contacto adicional.
  >
* **(3)** Los string son ingresados a los *.csv* de la manera:
  ```python
    (f"{mensaje a ingresar}\n")
  ```
  Por lo que se debe dejar una linea de código extra al final de cada .csv para no generar errores. De la siguiente manera:

![La linea 82 está vacia.](https://github.com/IIC2233/Nicolasramos411-iic2233-2021-1/blob/main/Tareas/T0/imagenes/imagen_contactos.png)

* **(4)** No se respetó (a propósito) la regla PEP8 'expected 2 blank lines, found 1 [9, 1]' , 'expected 2 blank lines after class or function definition, found 1 [315, 1]' y 'expected an indented block (comment) [371, 1]' en el archivo *clase_menu_e_instanciacion.py* pues consideraba que facilitaban el entendimiento del código.

-------

## Referencias de código externo

Para realizar mi tarea saqué código de:

1. [sys.exit()](https://www.delftstack.com/es/howto/python/python-exit-program/): Con esta función se logra salir del programa de manera exitosa y además permite predeterminar un mensaje de despedida y está implementado en el archivo clase_menu_e_instanciación.py en la línea 28.
>
2. [datetime()](https://www.programiz.com/python-programming/datetime): De esta usé datetime.now() y datetime.now.strftime() las que permiten obtener la fecha y la hora exacta cuando se escribe un mensaje en un chat o en un grupo. Están implementadas en el archivo clase_menu_e_instanciación.py en las líneas 136,137,285,286, 306 y 307.
>
3. get_input(): Función extraida de la materia del curso (AC0) e implementadas en el archivo clases_y_funciones.py en las líneas 32 a 38. Esta permite recibir un input y verificar si el input está dentro de un rango de valores permitido.

💥 Muchas gracias, espero les guste. 💥