import pandas as pd
from pymongo import MongoClient
import mysql.connector
import uuid
import numpy as np

#se definen las columnas según el esquema

"""
------
1.1	Carga de información

La información proporcionada se debe de cargar en alguna base de datos. Puede ser estructurada o no estructurada. Ejemplo: MySQL, Postgres, MongoDB, etc.
------
"""
df = pd.read_csv('data_prueba_tecnica.csv')

data = df.to_dict(orient='records')

def conectar_mongo(data):
    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['data_prueba']
        collection = db['collection_prueba']
        collection.insert_many(data)
        print('Datos insertados correctamente')
    except Exception as e:
        print('Error al insertar datos: ', e)

# Renombrar las columnas según el esquema
#conectar_mongo(data)

# Convertir los tipos de datos de las columnas según el esquema
def visualizar_informacion():
    client = MongoClient('mongodb://localhost:27017/')

    db = client['data_prueba']
    collection = db['collection_prueba']
    for document in collection.find():
        print(document)
#visualizar_informacion()
# Imprimir los primeros 5 registros del DataFrame resultante

def extraccion():
    client = MongoClient('mongodb://localhost:27017/')

    db = client['data_prueba']
    collection = db['collection_prueba']

    documents = collection.find()
    df = pd.DataFrame(list(documents))

    df.to_csv('data_prueba_tecnica_mongo.csv', index=False)

#extraccion()



def modificacion():
    

    df = pd.read_csv('data_prueba_tecnica_mongo.csv')

    df = df[['id', 'name', 'company_id', 'amount', 'status', 'created_at', 'paid_at']]
    df = df.rename(columns={'name': 'company_name', 'paid_at': 'updated_at'})
   

# Verificar si hay valores nulos en las columnas 'id', 'company_id', 'amount', 'status' y 'created_at'
    null_columns= df[['id','company_name','company_id', 'amount', 'status', 'created_at']].columns[df[['id', 'company_name' ,'company_id', 'amount', 'status', 'created_at']].isnull().any()]
    is_empty = df['amount'].isna().any()

    if is_empty:
        print("La columna 'amount' contiene valores vacíos.")
    else:
        print("La columna 'amount' no contiene valores vacíos.")
# Si hay valores nulos, imprimir un mensaje de error
    if len(null_columns) > 0:
        for column in null_columns:
            num_null = df[column].isnull().sum()
            print(f"El campo '{column}' tiene {num_null} registros con valores nulos")
            null_rows = df.loc[df[column].isnull()]
            print(null_rows)
    else:
        print("Todos los campos tienen valores no nulos")

    #asigna valores aleatorios a los campos nulos de id
    uuids = [str(uuid.uuid4()) if pd.isnull(x) else x for x in df['id']]
    df['id'] = uuids
    df.loc[df['company_name'] == 'MiPasajefy', 'company_id'] = 'cbf1c8b09cd5b549416d49d220a40cbd317f952e'
    df = df.dropna(subset=["company_name"])
    df["company_name"] = df["company_name"].replace(["MiPas0xFFFF", "MiP0xFFFF"], "MiPasajefy")
    df.to_csv('data_prueba_tecnica_mongo_modificado.csv', index=False)
    #segunda comprobacion
    if len(null_columns) > 0:
        for column in null_columns:
            num_null = df[column].isnull().sum()
            print(f"El campo '{column}' tiene {num_null} registros con valores nulos")
            null_rows = df.loc[df[column].isnull()]
            print(null_rows)
    else:
        print("Todos los campos tienen valores no nulos")


#modificacion()

def conexion_mysql():
    cnx = mysql.connector.connect(user='root', password='password',
                              host='localhost',
                              port= 3306,
                              auth_plugin='mysql_native_password')
    cursor = cnx.cursor()

    cursor.execute("CREATE DATABASE mydatabase")
    cursor.execute("USE mydatabase")

    cursor.execute("""
    CREATE TABLE companies (
        company_id VARCHAR(40) PRIMARY KEY,
        company_name VARCHAR(130) NULL
    )
        """)
    cursor.execute("""
    CREATE TABLE charges (
        id VARCHAR(24) PRIMARY KEY,
        company_id VARCHAR(24) NOT NULL,
        amount DECIMAL(16,2) NOT NULL,
        status VARCHAR(30) NOT NULL,
        created_at TIMESTAMP NOT NULL,
        updated_at TIMESTAMP NULL,
        FOREIGN KEY (company_id) REFERENCES companies(company_id)
    )
    """)

    df = pd.read_csv('data_prueba_tecnica_mongo_modificado.csv')
    companies_df = df[['company_id','company_name']].reset_index(drop=True)
    df['amount'] = df['amount'].fillna(0)
    print(companies_df)

    charges_df = df[['id', 'company_id', 'amount', 'status', 'created_at', 'updated_at']]

    # Cargar los datos en las tablas
    companies_insert_query = """
        INSERT INTO companies (company_id,company_name)
        VALUES (%s ,%s)
    """
    charges_df.loc[:, 'amount'] = charges_df['amount'].replace(np.nan, 0)


    charges_insert_query = """
        INSERT INTO charges (id, company_id, amount, status, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    companies_data_list = [(d['company_id'], d['company_name']) for _, d in companies_df.iterrows()]
    charges_data_list = [(d['id'], d['company_id'], d['amount'], d['status'], d['created_at'], d['updated_at']) for _, d in charges_df.iterrows()]

    cursor.executemany(companies_insert_query, companies_data_list)
    #cursor.executemany(charges_insert_query, charges_data_list)

# Confirmar los cambios
    cnx.commit()

# Cerrar la conexión
    cursor.close()
    cnx.close()

#conexion_mysql()

def subir_datos_mongo():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase2"]
    charges_col = db["charges"]
    companies_col = db["companies"] 

    df = pd.read_csv('data_prueba_tecnica_mongo_modificado.csv')

    distinct_company_ids = df["company_id"].unique()

# Obtener los valores distintos en la columna "company_name"
    distinct_company_names = df["company_name"].unique()
    
  
  
    print(distinct_company_ids)
    print(distinct_company_names)

    
    for i in range(len(distinct_company_ids)):
        company = {
            "company_id": distinct_company_ids[i],
            "company_name": distinct_company_names[i]
        }
        companies_col.insert_one(company)
    
    for _, row in df.iterrows():
        charge = {
            "id": row["id"],
            "company_id": row["company_id"],
            "amount": row["amount"],
            "status": row["status"],
            "created_at": row["created_at"],
            "updated_at": row["updated_at"],

        }
        charges_col.insert_one(charge)
    
#subir_datos_mongo()


from pymongo import MongoClient


def crear_vista():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase2"]
    
    pipeline = [
        {
            "$lookup": {
                "from": "companies",
                "localField": "company_id",
                "foreignField": "company_id",
                "as": "company"
            }
        },
        {
            "$unwind": "$company"
        },
        {
            "$group": {
                "_id": {
                    "company_id": "$company_id",
                    "company_name": "$company.name",
                    "date": "$date"
                },
                "total_amount": { "$sum": "$amount" }
            }
        },
        {
            "$project": {
                "_id": 0,
                "company_id": "$_id.company_id",
                "company_name": "$_id.company_name",
                "date": "$_id.date",
                "total_amount": 1
            }
        }
    ]
    
    db.create_view("transactions_by_company_and_date", "charges", pipeline)

crear_vista()

crear_vista()
