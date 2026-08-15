# Fase 12 — Deploy Mínimo na VPS

## 🎯 Objetivo

Publicar a API Login na VPS (via EasyPanel), tornando-a acessível publicamente com HTTPS, e validar com testes reais — cadastro, login e rota protegida — que ela funciona em produção da mesma forma que funciona localmente.

## 💡 Motivação

O roadmap original previa a Fase 12 como "integração com n8n" e a Fase 13 como "publicação". Na prática, essa ordem não funcionava: o n8n já roda na VPS, e a API só rodava localmente no Windows — a VPS não tem como alcançar `127.0.0.1` da máquina local. Por isso as fases foram invertidas: primeiro publicar a API (nova Fase 12), depois integrá-la ao n8n (nova Fase 13), já que ambos precisam estar na mesma rede para conversar.

## 📋 Pré-requisitos

- Fases 0 a 11 concluídas (API funcional localmente, com CRUD completo e autenticação testada)
- VPS com EasyPanel já configurado (projeto "nexflow" já existente, com `nexflow-postgres` rodando)
- Repositório `nexflowdx/API-Login` público no GitHub

## 🔨 Passo a passo

### 1. Preparação do código para deploy

Três ajustes foram necessários antes de tentar o deploy:

- **`app/database.py`** — a `DATABASE_URL` estava com `localhost` fixo no código. Corrigido para montar a URL a partir de variáveis de ambiente (`DB_USER`, `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_PASSWORD`), com valores padrão que mantêm o ambiente local funcionando sem mudanças.
- **`requirements.txt`** — estava salvo em UTF-16 (efeito colateral do `pip freeze > requirements.txt` no PowerShell), o que quebraria a instalação de dependências dentro do container Linux. Regravado em UTF-8 com `pip freeze | Out-File -Encoding utf8 requirements.txt`.
- **`Dockerfile`** — criado na raiz do projeto, usando `python:3.13-slim`, copiando `requirements.txt` primeiro (para aproveitar cache de build), depois a pasta `app/`, expondo a porta `8000` e rodando `uvicorn app.main:app --host 0.0.0.0 --port 8000`. Também foi necessário corrigir o nome do arquivo, que tinha sido salvo como `dockerfile` (minúsculo) — no Windows isso não faz diferença, mas em Linux nomes de arquivo são *case-sensitive*, e o EasyPanel não reconheceria o arquivo sem a correção.

### 2. Banco de dados

Em vez de criar um serviço de Postgres novo e isolado, foi reaproveitado o `nexflow-postgres` já existente na VPS — criando apenas um banco lógico novo dentro dele:

```sql
CREATE DATABASE api_login;
```

Executado via console do próprio serviço `nexflow-postgres` no EasyPanel.

### 3. Criação do serviço no EasyPanel

Dentro do projeto "nexflow" já existente, foi criado um novo serviço do tipo **Aplicativo**, chamado `api-login`, conectado ao repositório GitHub (`nexflowdx/API-Login`, branch `master`, build via `Dockerfile`).

Variáveis de ambiente configuradas no serviço:

```
DB_USER=postgres
DB_HOST=nexflow_nexflow-postgres
DB_PORT=5432
DB_NAME=api_login
DB_PASSWORD=<senha do postgres>
SECRET_KEY=<mesma chave usada localmente>
```

### 4. Primeiro deploy e correção de porta

O primeiro deploy buildou e subiu o container com sucesso (log confirmando `Application startup complete`), mas o domínio público retornava "Service is not reachable". O EasyPanel estava roteando para a porta `80` por padrão, enquanto a API roda na porta `8000` (definida no `Dockerfile`). Corrigido editando a porta do domínio diretamente no painel, sem necessidade de novo build.

### 5. Erro de tabela ausente e correção

Ao testar o cadastro (`POST /usuarios`) contra a URL pública, a API retornou `500 Internal Server Error`. O log do serviço mostrou a causa exata:

```text
sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "usuarios" does not exist
```

A tabela `usuarios` nunca existiu no banco de produção porque, localmente (Fase 5), ela foi criada de forma manual e pontual — rodando `Base.metadata.create_all(bind=engine)` uma única vez, sem que esse comando fizesse parte do código da aplicação. Corrigido executando o mesmo comando manualmente, através do console do serviço `api-login` no EasyPanel:

```bash
python3 -c "from app.database import Base, engine; from app import models; Base.metadata.create_all(bind=engine)"
```

> **⚠️ Observação / dívida técnica:** essa criação de tabela continua sendo manual e artesanal — o mesmo problema vai se repetir se o container for recriado do zero, ou se outra pessoa clonar o projeto e tentar rodá-lo pela primeira vez. O ideal, como melhoria futura, é automatizar a criação/atualização da estrutura do banco na inicialização da aplicação (por exemplo, chamando `create_all` no startup do FastAPI) ou adotar uma ferramenta de migração como o Alembic, em vez de depender de um comando rodado manualmente uma vez.

## ✅ Como validar

| Teste | Resultado |
|---|---|
| `GET /` (raiz) | ✅ `{"mensagem": "API Login está no ar"}` |
| `GET /status` | ✅ `{"status": "ok"}` |
| `POST /usuarios` (cadastro) | ✅ Usuário criado e persistido no banco de produção |
| `POST /login` | ✅ Token JWT retornado corretamente |
| `GET /usuarios` (protegida, com token) | ✅ Lista retornada corretamente |

## 📚 Lições aprendidas

- A ordem "lógica" de um roadmap nem sempre é a ordem tecnicamente possível — integrar com o n8n antes de publicar a API seria impossível, já que um está na VPS e o outro só existia localmente. Vale sempre checar dependências de rede antes de seguir a numeração de fases às cegas.
- Diferenças de comportamento entre Windows e Linux (case-sensitivity de nomes de arquivo, encoding padrão de redirecionamento do PowerShell) são fontes reais de bugs de deploy — não são "coisa de iniciante", travam qualquer desenvolvedor que treina localmente no Windows e publica em Linux.
- Rodar uma aplicação localmente com sucesso não garante que toda a infraestrutura around dela (schema do banco, variáveis de ambiente, portas) foi replicada em produção. Testar de ponta a ponta contra a URL pública — não só verificar se o container "está de pé" — foi o que revelou o problema real da tabela ausente.
- Passos manuais executados uma única vez (como criar uma tabela via comando avulso) são uma fonte silenciosa de dívida técnica: funcionam até o dia em que o ambiente precisa ser recriado do zero.

---
*Documentado em: 15/08/2026 11:24*
