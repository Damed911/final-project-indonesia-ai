from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TransactionRequest(BaseModel):
    text: str

@app.post("/transaction")
async def transaction(payload: TransactionRequest):
    lowercase = payload.text.lower()

    if "beli" in lowercase:
        return {
            "success": True,
            "message": "Berikut adalah transaksi yang kamu masukkan."
        }

    return {
        "success": False,
        "message": "Masukkan data yang lebih mudah dipahami"
    }

@app.get("/start")
async def root():
    return {"success": True, "message": "Hello world"}
