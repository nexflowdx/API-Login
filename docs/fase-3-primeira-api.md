# Fase 3 — Primeira API

## Objetivo
Criar as primeiras rotas da API e validar que o servidor FastAPI + Uvicorn está funcionando corretamente.

## Motivação
Antes de conectar banco de dados ou lógica de autenticação, é importante confirmar que a estrutura básica da API responde corretamente — evita depurar múltiplos problemas ao mesmo tempo mais adiante.

## Pré-requisitos
Bibliotecas instaladas via pip (FastAPI, Uvicorn e demais dependências do projeto).

## Passo a passo
1. Criação da instância da aplicação FastAPI em `app/main.py`.
2. Criação da rota `GET /`, retornando uma mensagem de status simples.
3. Criação da rota `GET /status`, retornando `{"status": "ok"}`.
4. Execução do servidor local com `uvicorn app.main:app --reload`.

## Como validar a configuração
- `http://127.0.0.1:8000/` retorna `{"mensagem":"API Login está no ar"}`.
- `http://127.0.0.1:8000/status` retorna `{"status":"ok"}`.
- `http://127.0.0.1:8000/docs` exibe a documentação interativa (Swagger) gerada automaticamente pelo FastAPI.

## Lições aprendidas
O servidor Uvicorn só fica ativo enquanto o comando está rodando no terminal — ao fechar o terminal ou o VS Code, é necessário rodar `uvicorn app.main:app --reload` novamente para a API voltar a responder.

---
*Documentado em: 05/08/2026 21:26*
