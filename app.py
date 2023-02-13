from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from bson import ObjectId
import motor.motor_asyncio
import pydantic

# origins = [
#     "https://ecse3038-lab3-tester.netlify.app/"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(["mongodb+srv://week4:<password>@cluster0.ulfwdah.mongodb.net/?retryWrites=true&w=majority"])
db = client.college

pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str

# @app.get()
# async def 
#   return

@app.post("")
async def create_new_todo(request: Request):
  todo_object = await request.json()

  new_todo = await request.json()
  created_todo = await db["todos"].find_one({"_id": new_todo.inserted_id}) 
  
  return created_todo

# @app.delete()
# async def 
#       return
#   return 
# @app.patch()
# async def 
#       return 
#   return 