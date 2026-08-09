import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

load_dotenv()

# cria e configura uma instância (um objeto) do gerenciador de senhas do Passlib chamado pwd_context. Define as regras de segurança que o sistema usará para transformar senhas em códigos seguros e ler esses códigos.
# pwd_context =É o nome da variável que você está criando. A partir daqui, você usará pwd_context.hash() para criptografar uma nova senha.
# CryptContext(...) É a classe que você importou do Passlib. Serve para automatizar toda a criptografia do sistema, evitando que configure algoritmos na mão.
# schemes=["bcrypt"] Define os algoritmos de criptografia (hashing) permitidos no seu sistema, que é um dos algoritmos mais seguros do mundo para senhas.
# deprecated="auto"O que faz: Gerencia automaticamente a obsolescência de algoritmos antigos. : Se no futuro adicionar um algoritmo mais novo na lista schemes (como o argon2), o deprecated="auto" vai marcar o bcrypt como "antigo". Quando um usuário antigo fizer login com uma senha bcrypt, o Passlib vai verificar a senha e, automaticamente, atualizá-la para o novo formato mais seguro no seu banco de dados, sem que o usuário perceba nada.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
EXPIRACAO_MINUTOS = 30

def hash_senha(senha):
    return pwd_context.hash(senha)

def verificar_senha(senha, hash_salvo):
    return pwd_context.verify(senha, hash_salvo)

def criar_token(dados: dict):
    dados_copia = dados.copy()
    expira_em = datetime.utcnow() + timedelta(minutes=EXPIRACAO_MINUTOS)
    dados_copia.update({"exp": expira_em})
    token = jwt.encode(dados_copia, SECRET_KEY, algorithm=ALGORITHM)
    return token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_usuario_atual(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    excecao_credenciais = HTTPException(status_code=401, detail="Não foi possível validar as credenciais")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise excecao_credenciais
    except JWTError:
        raise excecao_credenciais

    usuario = db.query(models.Usuario).filter(models.Usuario.email == email).first()
    if usuario is None:
        raise excecao_credenciais

    return usuario