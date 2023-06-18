# Utiliza la imagen oficial de Python con Ubuntu 20.04 como base

FROM python:3.9-buster
USER root
# Instala MySQL Server
RUN apt-get update && \
    apt-get install -y mysql-server

# Instala MongoDB
RUN apt-get install -y wget gnupg && \
    wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add - && \
    echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.4 main" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list && \
    apt-get update && \
    apt-get install -y mongodb-org

# Copia el archivo requirements.txt
COPY requirements.txt .

# Instala las librerías de Python
RUN pip3 install -r requirements.txt

# Abre los puertos necesarios para MongoDB y MySQL
EXPOSE 27017
EXPOSE 3306