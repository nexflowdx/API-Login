from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "API Login está no ar"}

@app.get("/status")
def read_status():
    return {"status": "ok"}


