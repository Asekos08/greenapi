from pydantic import BaseModel


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