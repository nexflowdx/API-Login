# Fase 4 — Banco de dados

## Objetivo
Instalar o PostgreSQL, criar o banco de dados do projeto, e conectar a API a ele usando SQLAlchemy — mantendo credenciais fora do código-fonte.

## Motivação
A partir dessa fase a API passa a persistir dados reais, em vez de retornar respostas fixas. Manter a senha do banco fora do código versionado é uma prática essencial de segurança.

## Pré-requisitos
PostgreSQL instalado e adicionado ao PATH do sistema; bibliotecas `sqlalchemy`, `psycopg2-binary` e `python-dotenv` instaladas no ambiente virtual.

## Passo a passo
1. Instalação do PostgreSQL 18 no Windows (com ajuste de PATH para reconhecer o comando `psql`).
2. Criação do banco de dados `api_login` via console `psql`.
3. Instalação do driver `psycopg2-binary`, necessário para o SQLAlchemy se conectar ao PostgreSQL.
4. Criação do `app/database.py`, configurando `engine`, `SessionLocal` e `Base` do SQLAlchemy.
5. Criação do arquivo `.env` (ignorado pelo Git) para armazenar a senha do banco fora do código.
6. Instalação do `python-dotenv` e atualização do `database.py` para ler a senha via `os.getenv("DB_PASSWORD")`.
7. Teste de conexão validado com sucesso.

## Como validar a configuração
- `psql --version` reconhece o comando corretamente.
- `\l` no console do PostgreSQL lista o banco `api_login`.
- Comando de teste de conexão retorna "Conectou com sucesso!" usando a senha lida do `.env`.

## Lições aprendidas
Instaladores no Windows nem sempre adicionam seus binários ao PATH automaticamente — o mesmo padrão de diagnóstico usado com Python (`Get-Command`, localizar a pasta de instalação, adicionar ao PATH) se aplicou aqui ao PostgreSQL. Além disso, ficou reforçada a prática de nunca commitar senhas: elas devem viver em `.env`, protegido pelo `.gitignore`, e ser lidas via variável de ambiente no código.

---
*Documentado em: 05/08/2026 22:18*
