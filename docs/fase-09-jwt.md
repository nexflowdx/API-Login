# Fase 9 — JWT

## Objetivo
Gerar um token JWT após login bem-sucedido, permitindo que a API identifique o usuário em requisições futuras sem exigir email/senha novamente.

## Motivação
Sem um token, a API "esquece" quem fez login logo após a resposta. O JWT funciona como um crachá assinado digitalmente, com prazo de validade, que o cliente reapresenta nas próximas requisições.

## Pré-requisitos
Rota de login funcionando (Fase 8); biblioteca `python-jose` já instalada (Fase 1).

## Passo a passo
1. Criação da função `criar_token(dados: dict)` em `app/auth.py`, usando `jwt.encode` do `python-jose`.
2. Definição de `SECRET_KEY` (movida para `.env`), `ALGORITHM = "HS256"` e expiração de 30 minutos, calculada com `datetime` + `timedelta`.
3. Atualização da rota `POST /login` para gerar o token com `criar_token({"sub": usuario.email})` e retorná-lo junto com `token_type: "bearer"`.

## Como validar a configuração
- `POST /login` com credenciais corretas retorna `access_token` (string longa, formato JWT) e `token_type: "bearer"`.

## Lições aprendidas
A `SECRET_KEY` segue o mesmo princípio de segurança da senha do banco (Fase 4): nunca fica exposta no código, sempre lida via `.env`. O campo `"sub"` dentro do payload do token é convenção JWT para identificar "de quem" é o token — nesse caso, o email do usuário.

---
*Documentado em: 09/08/2026 20:18*
