from fastapi import FastAPI, status, responses, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel
from uuid import UUID


app = FastAPI()



# Allow frontend origin
origins = [
    "http://127.0.0.1:5500",  # your local frontend
    "http://localhost:5500",  # sometimes browser uses localhost
    "https://your-frontend-domain.com"  # (later when deployed)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # allow specific origins
    allow_credentials=True,
    allow_methods=["*"],       # allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],       # allow all headers
)



@app.get('/', deprecated=False)
def root():
    return{"message":"Hello"}


class Name(BaseModel):
    id:int
    name:str
    



@app.post('/sendname',status_code=status.HTTP_201_CREATED)
def sendname(name: Name):
    if not name.name or not name.name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be empty.")
    return {"message": f"{name.name}"}



@app.get('/Name{name}',status_code=status.HTTP_200_OK)
def get_name(name: str):
    return {"message": f"Hello {name}"}
