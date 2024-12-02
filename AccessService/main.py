import grpc
import user_pb2
import user_pb2_grpc
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

def validate_credentials(email, password):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = user_pb2_grpc.UserServiceStub(channel)
        request = user_pb2.ValidateRequest(email=email, password=password)
        response = stub.ValidateCredentials(request)
        return response.is_valid

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:5173",  # Dirección del frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir estos orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

class LoginData(BaseModel):
    email: str
    password: str

@app.post("/login")
def login(data: LoginData):
    is_valid = validate_credentials(data.email, data.password)
    if is_valid:
        return {"message": "Inicio de sesión exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
