# Fase 10 — Rotas protegidas

## Objetivo
Criar a rota `GET /me`, acessível apenas com um token JWT válido, retornando os dados do usuário autenticado.

## Motivação
É o que torna o JWT gerado na Fase 9 útil de fato: sem validação em alguma rota, o token não tinha propósito prático ainda.

## Pré-requisitos
Login gerando token JWT funcionando (Fase 9).

## Passo a passo
1. Criação de `oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")` em `auth.py`, responsável por extrair o token do cabeçalho `Authorization`.
2. Criação da função `get_usuario_atual`, que decodifica o token (`jwt.decode`), extrai o email (`payload.get("sub")`), busca o usuário no banco, e retorna erro 401 em qualquer etapa que falhar (token inválido, expirado, ou usuário não encontrado).
3. Movimentação de `get_db` do `main.py` para o `auth.py`, já que `get_usuario_atual` também depende dela.
4. Criação da rota `GET /me`, protegida via `Depends(get_usuario_atual)`.

## Como validar a configuração
- `GET /me` sem token retorna `401`.
- `GET /me` com token válido (enviado via header `Authorization: Bearer <token>`) retorna os dados do usuário (`id`, `nome`, `email`).
- Testado via `curl.exe -H "Authorization: Bearer <token>"`, já que o botão "Authorize" do Swagger espera formato form-data (`username`/`password`), incompatível com o `/login` em JSON deste projeto.

## Lições aprendidas
O `OAuth2PasswordBearer` do FastAPI assume, por padrão, um fluxo de login via formulário — quando a rota de login usa JSON com nomes de campo diferentes (como `email`/`senha` em vez de `username`/`password`), o botão "Authorize" do Swagger não funciona out-of-the-box, exigindo testar via `curl` ou outra ferramenta (Postman, Insomnia) passando o header manualmente.

---
*Documentado em: 09/08/2026 20:47*
