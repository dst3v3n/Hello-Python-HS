from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI ()

# Entidad User

class User(BaseModel):
    id : int
    name:str
    surname:str
    url:str
    age:int

users_list = [User(id = 1 , name = "Harold" , surname = "Sabogal" , url = "https://harold.com" , age = 18),
              User(id = 2 , name = "Steven" , surname = "Perez" , url = "https://steven.com" , age = 18) ,
              User(id = 3 , name = "Haakon" , surname = "Daglberg" , url =  "https://haakon.com" , age = 34)] 

@app.get ("/usersjson") 
async def usersjson ():
    return [{"name" : "Harold", "surname" : "Sabogal" , "url" : "https://moure.dev", "age" : 18},
            {"name" : "Steven", "surname" : "Perez" , "url" : "https://moure.com", "age": 18},
            {"name" : "Haakon", "surname" : "Daglberg" , "url" : "https://haakon.com" , "age" : 34}]

@app.get ("/users")
async def users ():
    return users_list

#path

@app.get ("/user/{id}")
async def users (id : int):
    return search_user(id)

#Query

@app.get ("/userquery/")
async def users (id : int):
    return search_user(id)


def search_user(id: int):
    users = filter (lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
      return {"eror": "No se ha encontrado el usuario"}