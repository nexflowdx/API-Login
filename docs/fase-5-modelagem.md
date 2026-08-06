# Fase 5 — Modelagem

## Objetivo
Criar a primeira tabela do banco de dados (usuários), representada como uma classe Python usando o ORM do SQLAlchemy.

## Motivação
Modelar a tabela via código (em vez de SQL puro) permite que o SQLAlchemy gerencie a estrutura do banco de forma consistente com o restante da aplicação, e facilita futuras alterações.

## Pré-requisitos
Conexão com o PostgreSQL configurada e funcionando (Fase 4).

## Passo a passo
1. Criação da classe `Usuario` em `app/models.py`, herdando de `Base`.
2. Definição das colunas: `id` (chave primária), `nome`, `email` (único, indexado) e `senha`.
3. Execução do comando `Base.metadata.create_all(bind=engine)` para criar a tabela fisicamente no PostgreSQL.

## Como validar a configuração
- Comando de criação retorna "Tabela criada com sucesso!" sem erros.
- `psql -U postgres -d api_login -c "\d usuarios"` exibe a estrutura da tabela com as 4 colunas esperadas.

## Lições aprendidas
O SQLAlchemy separa claramente a definição da tabela (código Python) da criação física dela no banco (`create_all`) — o modelo só vira tabela real quando esse comando é executado.

---
*Documentado em: 05/08/2026 22:40*
