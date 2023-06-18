# Prueba_tecnica
Prueba Técnica



## Sección 1: Procesamiento y transferencia de datos

### Objetivo: Crear un proceso con las herramientas disponibles por el usuario

Los ejercicios de programación tienen que incluir los procedimientos de instalación y ejecución de las herramientas a utilizar y los scripts que realizaran los procedimientos. Se puede realizar a través de Dockers. Pueden incluir pruebas unitarias o de integración. Se puede compartir por Github o cualquier repositorio o en un zip.
### Implementación

Primero instale las dependencias necesarias utilizando el siguiente comando
> pip install pandas pymongo mysql-connection-python numpy

Utilizando un entorno virtual generé un archivo requirements.txt con el siguiente comando

> pip freeze > requirements.txt

### 1.1 Carga de la Información

Para cargar incial la información sin depurar utilice MongoDB debido a su felixibilidad con la información corrupta o faltante

### 1.2 Extracción

Extraí la información en formato csv debido a que es uno de los formatos más fáciles de trabajar si se utiliza la librería de pandas

### 1.3 Transformación

Realicé las siguientes transformaciones para cumplir con el esquema propuesto:
- Cambié la columna paid_at en el archivo csv por updated_at utilizando pandas
- De acuerdo al esquema propuesto, las únicas columnas que podrían encontrarse vacías son company_name, y updated_at, por lo tanto procedí a verificar que no se encontraran celdas vacías o con valores de nan de las columnas restantes. Encontrando 3 registros en id que estaban vacíos. Por lo tanto, procedí a utilizar la librería uuid para generar un id al azar a dichos registros. También encontré 4 registros vacíos en la columna de company_name, Todas ellas pertecientes a MiPasajefy, por lo que procedí a asignar el company_id de dicha compañía a dichos regitros.
- De acuerdo a la información del archivo csv, sólo hay dos compañias MiPasajefy y Muebles Chidos, sin embargo encontré registros con valores númericos, por lo cual procedí a cambiar dichos registros por MiPasajefy
-
### 1.4 Dispersión de la información
La dispersión tablas se generaron en base al siguiente diagrama:

![image](https://github.com/alangamboa97/prueba_tecnica/assets/23564068/5cd07233-ce5c-4ae4-aeea-06198df16e3a)



### 1.5 SQL

Las tablas se generaron en base al siguiente diagrama:

![image](https://github.com/alangamboa97/prueba_tecnica/assets/23564068/5cd07233-ce5c-4ae4-aeea-06198df16e3a)







## Seccción 2: Creación de un API

### Implementación

### 1.- Creación de la Clase Conjunto




![conjunto](https://github.com/alangamboa97/prueba_tecnica/assets/23564068/1430c32f-6946-4320-9a7f-0f0cd7a7da51)
### 2.- Instalación de FastAPI

Para instalar FastAPI ejecuta el siguiente comando:

> pip install "fastapi[all]"

Posteriormente se crea una API como se muestra a continuación:
![api](https://github.com/alangamboa97/prueba_tecnica/assets/23564068/b7b7a4e1-b594-4d2f-9b15-597a68f33953)

Para inciar el servidor se ejecuta el siguiente comando:
> uvicorn main:app --reload

La API previamente creada acepta dos direcciones

- DELETE: http://127.0.0.1:8000/extraer/{} dónde dentro de {} se indica el número a extraer del conjunto original
- GET: http://127.0.0.1:8000/calcular, dónde devuelve el conjunto original sin los numeros extraidos



