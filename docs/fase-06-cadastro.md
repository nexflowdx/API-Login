# Fase 6 — Cadastro

## Objetivo
Criar a rota `POST /usuarios`, permitindo cadastrar novos usuários no banco de dados através da API.

## Motivação
É o primeiro endpoint que efetivamente escreve dados no banco, validando entrada (via Pydantic) e controlando o que é exposto na resposta (nunca devolvendo a senha).

## Pré-requisitos
Tabela `usuarios` criada no PostgreSQL (Fase 5).

## Passo a passo
1. Criação dos schemas `UsuarioCreate` (dados recebidos) e `UsuarioResponse` (dados retornados, sem senha) em `app/schemas.py`, usando Pydantic.
2. Instalação da validação de email (`pydantic[email]`).
3. Criação da função `get_db()` em `main.py`, usando `Depends` para abrir e fechar a sessão do banco automaticamente a cada requisição.
4. Criação da rota `POST /usuarios`, que recebe um `UsuarioCreate`, salva no banco via SQLAlchemy, e retorna um `UsuarioResponse`.

## Como validar a configuração
- `/docs` exibe a nova rota `POST /usuarios`.
- Testando via Swagger, o cadastro retorna status 200 com `id`, `nome` e `email` — sem o campo `senha` na resposta.
- O usuário aparece salvo na tabela `usuarios` do PostgreSQL.

## Lições aprendidas
Separar `models.py` (estrutura do banco) de `schemas.py` (formato de entrada/saída da API) evita expor dados sensíveis, como a senha, nas respostas. Nesta fase a senha ainda é salva em texto puro, propositalmente — a Fase 7 resolve isso com hash.

---
*Documentado em: 05/08/2026 22:58*
