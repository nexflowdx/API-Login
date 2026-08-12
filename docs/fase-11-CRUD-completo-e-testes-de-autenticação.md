# Fase 11 — CRUD Completo e Testes de Autenticação

## 🎯 Objetivo

Concluir o CRUD completo da API (criar, listar, editar e excluir usuários) e validar, com testes reais, que a autenticação via JWT está de fato protegendo as rotas — não apenas assumir que está.

## 💡 Motivação

Até a Fase 10, a API já tinha cadastro, login, geração de JWT e uma primeira rota protegida (`GET /me`). Faltava fechar o CRUD (editar e excluir usuários) e, principalmente, provar com testes que alguém sem token — ou com token inválido — realmente não consegue acessar dados protegidos. Sem esses testes, a proteção é uma suposição, não um fato verificado.

## 📋 Pré-requisitos

- Fases 0 a 10 concluídas (ambiente, banco, modelagem, cadastro, hash de senha, login, JWT, rota protegida `/me`)
- Servidor da API rodando localmente via `uvicorn app.main:app --reload`
- PowerShell com ambiente virtual (`.venv`) ativado

## 🔨 Passo a passo

### 1. Rota de edição — `PUT /usuarios/{usuario_id}`

Rota criada usando *path parameter* (`{usuario_id}` na URL), protegida por token JWT via `Depends(get_usuario_atual)`. Permite atualizar nome, email e senha — a senha continua sendo processada por `hash_senha()`, nunca armazenada em texto puro.

### 2. Rota de exclusão — `DELETE /usuarios/{usuario_id}`

```python
@app.delete("/usuarios/{usuario_id}")
def excluir_usuario(
    usuario_id: int,
    db: Session = Depends(get_db),
    usuario_atual: models.Usuario = Depends(get_usuario_atual)
):
    usuario = db.query(models.Usuario).filter(
        models.Usuario.id == usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    db.delete(usuario)
    db.commit()

    return {"mensagem": "Usuário excluído com sucesso"}
```

Testada via PowerShell:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/usuarios/2" -Method Delete -Headers $headers
```

Resultado: usuário removido com sucesso do banco (confirmado depois, na Fase de testes, por ele não aparecer mais em `GET /usuarios`).

### 3. Bug de encoding no PowerShell

A mensagem de sucesso do DELETE veio corrompida: `UsuÃ¡rio excluÃ­do com sucesso`. O código da API estava correto — o problema era o terminal, configurado em `IBM850` (CodePage 850) em vez de `UTF-8`. Diagnóstico:

```powershell
[Console]::OutputEncoding
```

Correção:

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
```

Depois disso a saída passou a exibir acentos corretamente.

### 4. Testes de autenticação e autorização

Com o CRUD fechado, restava provar que a proteção das rotas funciona nos três cenários possíveis:

**Sem token:**
```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/usuarios" -Method Get
```
→ `401 Unauthorized`, `{"detail":"Not authenticated"}`

**Token inválido:**
```powershell
$headersTeste = @{ Authorization = "Bearer token-falso" }
Invoke-RestMethod -Uri "http://127.0.0.1:8000/usuarios" -Method Get -Headers $headersTeste
```
→ `401 Unauthorized`, `{"detail":"Não foi possível validar as credenciais"}`

**Token válido:**
Criado usuário de teste (`testejwt@exemplo.com`), login realizado, token obtido e usado no header:
```powershell
$headers = @{ Authorization = "Bearer $($resposta.access_token)" }
Invoke-RestMethod -Uri "http://127.0.0.1:8000/usuarios" -Method Get -Headers $headers
```
→ Lista de usuários retornada corretamente, confirmando também que o usuário excluído na etapa 2 não aparece mais.

## ✅ Como validar

| Método | Endpoint | Autenticação | Status |
|---|---|---|---|
| POST | `/usuarios` | Não | ✅ |
| POST | `/login` | Não | ✅ |
| GET | `/me` | Sim | ✅ |
| GET | `/usuarios` | Sim | ✅ |
| PUT | `/usuarios/{id}` | Sim | ✅ |
| DELETE | `/usuarios/{id}` | Sim | ✅ |
| Acesso sem token | — | — | ✅ bloqueado (401) |
| Acesso com token inválido | — | — | ✅ bloqueado (401) |
| Acesso com token válido | — | — | ✅ liberado |

## 📚 Lições aprendidas

- Testar que uma rota **bloqueia** o acesso indevido é tão importante quanto testar que ela funciona com credenciais corretas — sem os três cenários (sem token / token inválido / token válido), a proteção é presumida, não comprovada.
- Erros de encoding entre terminal e API são fáceis de confundir com bug de código. Antes de mexer na aplicação, vale checar a codificação do próprio terminal.
- `Invoke-RestMethod` do PowerShell trata qualquer resposta HTTP de erro (4xx/5xx) como exceção do próprio comando — o corpo da resposta da API (`{"detail": "..."}`) aparece dentro da mensagem de erro do PowerShell, não como um retorno normal.

---
*Documentado em: 11/08/2026 22:02*
