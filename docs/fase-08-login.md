# Fase 8 — Login

## Objetivo
Criar a rota `POST /login`, autenticando um usuário existente por email e senha, usando a função de verificação de hash criada na Fase 7.

## Motivação
Login é o segundo pilar da autenticação: depois de cadastrar (Fase 6) e proteger a senha (Fase 7), o sistema precisa confirmar a identidade de quem já está cadastrado, sem nunca revelar qual campo especificamente está incorreto (por segurança).

## Pré-requisitos
Função `verificar_senha` disponível em `app/auth.py` (Fase 7); usuário cadastrado com senha em hash (Fase 6/7).

## Passo a passo
1. Criação do schema `UsuarioLogin` em `schemas.py`, com apenas `email` e `senha`.
2. Criação da rota `POST /login`, buscando o usuário no banco via `db.query(models.Usuario).filter(models.Usuario.email == login.email).first()`.
3. Verificação em duas etapas: usuário existe (`if usuario is None`) e senha bate (`if not verificar_senha(...)`) — ambas retornando o mesmo erro genérico `401 - "Email ou senha incorretos"`, por segurança.
4. Ajuste de imports no `main.py`: adição de `HTTPException` (fastapi) e `verificar_senha` (app.auth), que estavam faltando.

## Como validar a configuração
- `POST /login` com credenciais corretas retorna `200` e `{"mensagem": "Login realizado com sucesso"}`.
- Testado com o usuário `teste2@exemplo.com`, cadastrado já com hash correto (Fase 7).

## Lições aprendidas
Erros `500` sem detalhe na tela do Swagger exigem checar o terminal do `uvicorn` para ver o traceback completo — no caso desta fase, a causa era um import faltando (`verificar_senha`), não um problema de lógica. Também foi importante ajustar o método de estudo: reconstruir uma rota inteira do zero, peça por peça, sem ver o exemplo funcionando antes, gerou confusão — o formato que funcionou melhor foi ver o código completo primeiro, entender e testar, com a prática de reescrita de memória como exercício separado, não como bloqueio para avançar.

---
*Documentado em: 09/08/2026 14:51*
