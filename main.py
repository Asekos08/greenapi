from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static", html=True), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

class InstanceData(BaseModel):
    idInstance: str
    apiTokenInstance: str

class MessageData(BaseModel):
    idInstance: str
    apiTokenInstance: str
    chatId: str
    message: str

class FileData(BaseModel):
    idInstance: str
    apiTokenInstance: str
    chatId: str
    urlFile: str
    fileName: str
    caption: str

@app.post("/getSettings")
async def get_settings(data: InstanceData):
    url = f"https://api.green-api.com/waInstance{data.idInstance}/getSettings/{data.apiTokenInstance}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@app.post("/getStateInstance")
async def get_state_instance(data: InstanceData):
    url = f"https://api.green-api.com/waInstance{data.idInstance}/getStateInstance/{data.apiTokenInstance}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@app.post("/sendMessage")
async def send_message(data: MessageData):
    url = f"https://api.green-api.com/waInstance{data.idInstance}/sendMessage/{data.apiTokenInstance}"
    payload = {
        "chatId": data.chatId,
        "message": data.message
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@app.post("/sendFileByUrl")
async def send_file_by_url(data: FileData):
    url = f"https://api.green-api.com/waInstance{data.idInstance}/sendFileByUrl/{data.apiTokenInstance}"
    payload = {
        "chatId": data.chatId,
        "urlFile": data.urlFile,
        "fileName": data.fileName,
        "caption": data.caption
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()
