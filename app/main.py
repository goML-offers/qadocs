
from fastapi import FastAPI,File, UploadFile
from db.model import Pdfqna
from fastapi.middleware.cors import CORSMiddleware
from api import api
import os
app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "OPTIONS", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Fast API in Python"}


@app.post("/qna")
def read_user(payload: Pdfqna):

    payload = payload.dict()

    return api.pdf_to_qna(payload)

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_directory=f"temp_files"
    file_location = f"{file_directory}/{file.filename}"

    if not os.path.exists(file_directory):
        os.makedirs(file_directory)

    with open(file_location, "wb") as f:
        f.write(file.file.read())
    return {"file_llocation":file_location}
