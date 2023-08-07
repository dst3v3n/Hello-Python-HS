from fastapi import FastAPI

app = FastAPI()

@app.get("/") 
async def root (): #Hacer procesos en segundo plano
    return "Hola FastApi"

@app.get("/url") 
async def url (): #Hacer procesos en segundo plano
    return {"url" : "https://mouredev.com/python"}
