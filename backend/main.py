from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from dotenv import load_dotenv
from model import predict_aesthetic

load_dotenv()

app = FastAPI()

cors_origins = os.getenv("CORS_ORIGINS", "")
origins = [origin.strip() for origin in cors_origins.split(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Image Aesthetic Scorer API"}

@app.post("/predict/")
async def predict_image(file: UploadFile = File(...)):
    filename = "temp_" + file.filename
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    score = predict_aesthetic(f"temp_{file.filename}")

    try:
        os.remove(filename)
    except Exception as e:
        print(f"Warning: could not delete temp file {filename}: {e}")

        
    return {"score": score}
