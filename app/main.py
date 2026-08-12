from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import hash_senha, verificar_senha, criar_token, get_db, get_usuario_atual

app = FastAPI()

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

@app.post("/login")
def login(login: schemas.UsuarioLogin, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.email == login.email).first()

    if usuario is None:
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    if not verificar_senha(login.senha, usuario.senha):
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    token = criar_token({"sub": usuario.email})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/me", response_model=schemas.UsuarioResponse)
def ler_usuario_atual(usuario_atual: models.Usuario = Depends(get_usuario_atual)):
    return usuario_atual

@app.get("/usuarios", response_model=list[schemas.UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db), usuario_atual: models.Usuario = Depends(get_usuario_atual)):
    usuarios = db.query(models.Usuario).all()
    return usuarios

@app.put("/usuarios/{usuario_id}", response_model=schemas.UsuarioResponse)
def editar_usuario(usuario_id: int, dados: schemas.UsuarioCreate, db: Session = Depends(get_db), usuario_atual: models.Usuario = Depends(get_usuario_atual)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    usuario.nome = dados.nome
    usuario.email = dados.email
    usuario.senha = hash_senha(dados.senha)

    db.commit()
    db.refresh(usuario)
    return usuario

@app.delete("/usuarios/{usuario_id}")
def excluir_usuario(usuario_id: int, db: Session = Depends(get_db), usuario_atual: models.Usuario = Depends(get_usuario_atual)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db.delete(usuario)
    db.commit()
    return {"mensagem": "Usuário excluído com sucesso"}