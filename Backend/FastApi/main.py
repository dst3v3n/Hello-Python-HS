from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root ():
    return "¡Hello FastApi!"

@app.get("/url")
async def url ():
    return {"url_curso" : "https:haroldsabogal"}