from pydantic import BaseModel


class Pdfqna(BaseModel):
    file_location:str
    model_name: str
    embedding_name: str
    question:str
    rag: bool
