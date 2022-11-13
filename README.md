## Tabla de contenidos
1. [Info General] (#info-general)
2. [Pasos a seguir para Funcionamiento]
## Info General
***
Nuestro proyecto "INFOVIDEOJUEGOS", es un pequeño modelo de un Blog que esta en desarrollo, actualmente cuenta con la funcionalidad de poder registrar Usuarios y al momento de crearlo, este se guarda automaticamente en una Base de Datos. Asimismo el Blog nos permite poder buscar y ver por pantalla aquellos usuarios que fueron registrados. Tambien cuenta con un apartado donde el usuario podra ver una breve descripcion acerca de los Desarrolladores de dicho proyecto.
***
## Pasos a seguir para Funcionamiento
```
$ Abrir una terminal de VSC (Preferiblemente la terminal Bash).
$ Una vez abierta la terminal ejecutar  el comando git clone https://github.com/IvanPlaza44/Entrega1-Arjona_y_Plaza/tree/main el cual nos ayudar a clonar nuestro reposistorio y ponerlo ene sus computadora de forma local.
$ Crear un entorno virtual  con el comando python -m venv <nombre de tu entorno virtual (se recomienda EntornoVirtual)>.
$ Ejecutaremos nuestro entorno virtual con ayuda del archivo start.sh  y para activarlo en la terminal ejecutaremos el siguiente comando . start.sh o  si no se quiere ocupar este archivo escribiremos en la terminal:
    $   Windows
        $ . <nombre_de_tu _entorno_virtual>/Scripts/activate
    $ Linux
        $ . <nombre_de_tu _entorno_virtual>/bin/activate
$ Instalaremos Django con el comando pip install Django.
$ Levantaremos nuestra  Base de Datos, pra lo cual en temrinal pondremso ele sisguiente codigo  py, python o python3 (depende  de sus computadora)  manage.py makemigrations, al ejecutar este comando nos creara nuesta Base de datos llamada sqlite3.
$ Lavantaremos nuestro servidor de forma local, para esto nosotros ejecutaremos el comando py, python o python3 (depende  de sus computadora)  manage.py runserver
$ Una vez levantado nuestro server encontrara una pagina de inicio, esta sera nuesto index porteriormente si usted le da clic a la leyenda "Menu" vera tres opciones
    $ Iniciar Sesion: Esta opcion nos permitira Iniciar sesion con un usuario y contraseña previamente registrados
    $ Registarse: Nos permitira registrarnos para acceder al blog y asi poder crear y ver los videojuegos.
    $ Acerca de Nosotros: Observaras una pequeña descripción de nosotros.
$ Esperemos te guste nuestro desarrollo.

El supoer admin  es 
user admin
pass 123

>>> VIDEO EXPLICATIVO SOBRE EL USO DEL BLOG <<<     https://www.youtube.com/watch?v=xeZpguLUReQ