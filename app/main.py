from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.auth import hash_senha

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"mensagem": "API Login está no ar"}

@app.get("/status")
def read_status():
    return {"status": "ok"}

@app.post("/usuarios", response_model=schemas.UsuarioResponse)
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    senha = hash_senha(usuario.senha)     
    novo_usuario = models.Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=senha                        
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario