# Fase 7 — Segurança (hash de senha)

## Objetivo
Parar de salvar senhas em texto puro no banco, usando hash criptográfico via bcrypt.

## Motivação
Um hash é irreversível — não existe forma de "desembaralhar" de volta pra senha original. Isso protege os usuários mesmo se o banco for comprometido.

## Pré-requisitos
Bibliotecas `passlib` e `bcrypt` já instaladas (Fase 1).

## Passo a passo
1. Criação de `app/auth.py` com `CryptContext` do passlib, configurado para usar bcrypt.
2. Duas funções: `hash_senha(senha)` (gera o hash) e `verificar_senha(senha, hash_salvo)` (compara senha digitada com hash salvo).
3. Atualização da rota `POST /usuarios` para calcular `senha = hash_senha(usuario.senha)` antes de salvar no banco.
4. Correção de incompatibilidade entre `bcrypt 5.0.0` e `passlib 1.7.4`, fixando a versão: `pip install "bcrypt==4.0.1"`.

## Como validar a configuração
- Cadastro via `/docs` retorna 200 normalmente.
- `SELECT email, senha FROM usuarios;` no `psql` mostra a senha como hash (formato `$2b$12$...`), não mais como texto puro.

## Lições aprendidas
Nem todo erro é sobre lógica do próprio código — incompatibilidade de versões entre bibliotecas é comum e não dá pra prever só raciocinando; é resolvido pesquisando a mensagem de erro específica. A lógica de hash/verificação, por outro lado, foi construída via raciocínio próprio, sem olhar código pronto antes.

---
*Documentado em: 09/08/2026 12:12*
