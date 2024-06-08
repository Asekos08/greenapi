from .models import InstanceData, MessageData, FileData
from fastapi import APIRouter, HTTPException
import requests


router = APIRouter()

@router.post("/getSettings")
async def get_settings(data: InstanceData):
    url = f"https://api.green-api.com/waInstance{data.idInstance}/getSettings/{data.apiTokenInstance}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.post("/getStateInstance")
async def get_state_instance(data: InstanceData):
    url = f"https://api.green-api.com/waInstance{data.idInstance}/getStateInstance/{data.apiTokenInstance}"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.post("/sendMessage")
async def send_message(data: MessageData):
    url = f"https://api.green-api.com/waInstance{data.idInstance}/sendMessage/{data.apiTokenInstance}"
    payload = {
        "chatId": f"{data.chatId}@c.us",
        "message": data.message
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()

@router.post("/sendFileByUrl")
async def send_file_by_url(data: FileData):
    url = f"https://api.green-api.com/waInstance{data.idInstance}/sendFileByUrl/{data.apiTokenInstance}"
    payload = {
        "chatId": f"{data.chatId}@c.us",
        "urlFile": data.urlFile,
        "fileName": data.fileName,
        "caption": data.caption
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    return response.json()