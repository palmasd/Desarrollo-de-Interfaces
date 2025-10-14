# Mi primer hola mundo con PySdie6

- Vamos a crear una ventana que tenga "hola mundo" con PySide6

- Github: https://github.com/palmasd/Desarrollo-de-Interfaces/tree/main

# Objetivo de aprendiza

- Crear un entorno virtual, instalar dependencias y usar la libreria de Pyside6 para crear una ventana simple en el cual obtengamos un simple "hola mundo".
Usaremos una clase ventana y desde el main llamaremos a la ventana.

# Requisitos previos

- Versión de Python utilizada (Python 3.13.7)
- Sistema Opertativo(Windows)
- Herramientas: Github, VS Code, Readme.md, Python

# Creación y activacion del entorno virtual

- Comandos para crear un Entorno virtual: python -m venv venv
- Comandos para activar el entorno virtual: venv\Scripts\activate
- Comandos para desactivar el entorno virtual: deactivate
- Comando para verificar version de python: python --version

# Instalación de dependencias

- Para instalar PySide6 usamos el comando: pip install PySide6
- Comando para crear un txt en donde se guarden las dependencias: pip freeze > requirements.txt
- PySide6 pertenece a la libreria de QT de Widgets la cual es principalmente utilizada para crear interfaces de usuarios, pueden mostrar informacion de estado, recibir entradas del usuario y proporcionar un contenedor para otros widgets que deben agruparse

# Estructura mínima de carpetas y archivos 

proyecto-VentanaQT/
 ├─ venv
 ├─ src/
 │  ├─ main.py          # punto de entrada
 │  └─ ventana.py       # clase Ventana
 ├─ .gitignore
 ├─ requirements.txt
 └─ README.md

 - Separamos la logica en la cual la clase ventana se va a encargar de introducir los datos de la ventana y la clase main se encarga de generar el arranque de la ventana

 # Código fuente(explicacion línea a línea)

 - ventana.py: define una clase Ventana que hereda de QWidget o QMainWindow, configura el título y muestra un QLabel con “Hola Mundo”. Aclara qué es un widget y cómo se añade a la ventana.
 - main.py: crea la QApplication, instancia Ventana, la muestra con .show() y arranca el bucle de eventos con app.exec().

  ```python
 app = QApplication([]) #crea una instancia de QApplication
 ventana1 = Ventana() #crea una instancia de la clase Ventana
 ventana1.show() 3muestra la ventana
 app.exec() #arranca el bucle de eventos

```

sin este bucle de eventos el script se ejecutaria de principio a fin en unos segundos y la ventana apareceria y desapareceria muy rapido que no se veria


# Ejecución y prueba

- comandos para ejecutar: Ctrl + ñ para abrir la terminal y una vez dentro del proyecto ejecutar el comando "python main.py"
- se tiene que ver algo como esto ![alt text](image.png)

# Problemas frecuentes y cómo resolverlos

- No tuve problemas porque seguí la guia en clase 