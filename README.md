# Prueba_tecnica
Prueba Técnica



## Sección 1: Procesamiento y transferencia de datos

### Objetivo: Crear un proceso con las herramientas disponibles por el usuario

Los ejercicios de programación tienen que incluir los procedimientos de instalación y ejecución de las herramientas a utilizar y los scripts que realizaran los procedimientos. Se puede realizar a través de Dockers. Pueden incluir pruebas unitarias o de integración. Se puede compartir por Github o cualquier repositorio o en un zip.
### Implementación

Ejecuté el siguiente comando

### 1.3 Disperción de la Información

Las tablas se generaron en base al siguiente diagrama:

![image](https://github.com/alangamboa97/prueba_tecnica/assets/23564068/160d4471-71d4-4afc-8f0c-391be3330627)





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



