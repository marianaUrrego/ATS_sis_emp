from fastapi import FastAPI
from routers import apiOfertas, apiUsuarios

#python -m pip install routers
# para instalar fastapi :          pip install fastapi 
# o si de esta manera no funciona: python -m pip install fastapi

# para instalar uvicorn : python -m pip install uvicorn    
# python -m pip install psycopg2 : esto también se necesita, aunque no se muy bien paque

app = FastAPI()

app.include_router(apiUsuarios.router)
app.include_router(apiOfertas.router)

@app.get("/")
def root():
    return "esta es la API"

#para iniciar el servidor se usa python -m uvicorn api:app --reload     