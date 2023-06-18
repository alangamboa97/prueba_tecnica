from fastapi import FastAPI
from faltante import Conjunto

app = FastAPI()
conjunto = Conjunto()

#uvicorn main:app --reload

@app.delete("/extraer/{numero}")
async def extraer_numero(numero: int):
    conjunto.extraer(numero)
    return {"conjunto": list(conjunto.conjunto)}


@app.get("/calcular")
async def calcular_faltante():
    elementos_faltantes = conjunto.calcular_faltante()
    if elementos_faltantes:
        return {"elementos_faltantes": elementos_faltantes}
    else:
        return {"mensaje": "El conjunto está vacío."}
