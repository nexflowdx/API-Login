# 📖 Glossário — Projeto API Login

Referência rápida dos comandos e conceitos usados em cada fase do projeto.

---

## Fase 1 — Preparação do ambiente

### Navegação e arquivos

| Comando | O que faz |
|---|---|
| `cd <caminho>` | Muda para a pasta indicada |
| `mkdir <nome>` | Cria uma pasta nova |
| `New-Item <arquivo>` | Cria um arquivo vazio (pode criar vários de uma vez, separados por vírgula) |
| `dir "<caminho>"` | Lista o conteúdo de uma pasta, ou confirma se um arquivo existe |

### Python e ambiente virtual

| Comando | O que faz |
|---|---|
| `python --version` | Mostra a versão do Python que está sendo reconhecida |
| `python -m venv .venv` | Cria um ambiente virtual isolado na pasta `.venv` |
| `.\.venv\Scripts\Activate.ps1` | Ativa o ambiente virtual (o VS Code costuma fazer isso sozinho ao abrir o terminal) |
| `pip install <pacotes>` | Instala bibliotecas Python dentro do ambiente virtual ativo |

### Diagnóstico de PATH (Python)

| Comando | O que faz |
|---|---|
| `where.exe <programa>` | Mostra em quais pastas o Windows encontra um programa pelo nome |
| `Get-Command <programa> -All` | Lista **todos** os executáveis encontrados com esse nome, na ordem de prioridade |
| `$env:Path -split ';'` | Divide a variável PATH em uma lista, uma pasta por linha, para inspecionar |
| `[Environment]::GetEnvironmentVariable("Path","User")` | Lê o PATH salvo permanentemente no Windows para o usuário atual |
| `[Environment]::SetEnvironmentVariable("Path", $novo, "User")` | Grava um novo valor de PATH permanentemente |

### Git

| Comando | O que faz |
|---|---|
| `git --version` | Confirma se o Git está instalado e qual versão |
| `git config --global user.name "Nome"` | Define o nome usado nos commits (vale para todos os projetos) |
| `git config --global user.email "email"` | Define o email usado nos commits |
| `git init` | Transforma a pasta atual em um repositório Git |
| `git status` | Mostra o que mudou desde o último commit (e o que está sendo ignorado) |
| `git add .` | Adiciona todos os arquivos modificados/novos à área de staging |
| `git commit -m "mensagem"` | Grava um commit com as mudanças que estão em staging |
| `git remote add origin <url>` | Conecta o repositório local a um endereço remoto (GitHub) |
| `git push -u origin master` | Envia os commits locais para o GitHub (a primeira vez, fixando a conexão) |
| `git push` | Envia novos commits (depois do primeiro `push -u`) |

---

## Fase 2 — Estrutura profissional

### PowerShell — manipulação de texto (script de data)

| Comando/conceito | O que faz |
|---|---|
| `Get-Content <arquivo> -Encoding UTF8` | Lê o conteúdo de um arquivo de texto |
| `-replace 'padrão', 'substituto'` | Troca um trecho de texto por outro (aceita expressões regulares) |
| `Set-Content <arquivo> -Encoding UTF8` | Grava conteúdo de volta em um arquivo |
| `Get-Date -Format "dd/MM/yyyy HH:mm"` | Gera a data e hora atuais no formato especificado |
| `param([string]$Nome)` | Declara um parâmetro reutilizável dentro de um script `.ps1` |
| `.\scripts\set-data.ps1 -Arquivo <caminho>` | Roda o script reutilizável de data, passando o arquivo alvo como parâmetro |

---

## Fase 3 — Primeira API

### Bibliotecas Python

| Biblioteca | Papel no projeto |
|---|---|
| **FastAPI** | Framework principal — cria as rotas da API (`/login`, `/usuarios`, etc.) |
| **Uvicorn** | Servidor que roda a aplicação FastAPI e escuta requisições |

### Código FastAPI

| Conceito | O que é |
|---|---|
| `app = FastAPI()` | Cria a instância principal da aplicação |
| `@app.get("/rota")` | Decorador — registra a função abaixo como responsável por responder GET nessa rota |
| `uvicorn app.main:app --reload` | Roda o servidor local, reiniciando automaticamente a cada mudança salva |

---

## Fase 4 — Banco de dados

### PostgreSQL e SQL

| Comando | O que faz |
|---|---|
| `psql --version` | Confirma se o cliente de linha de comando do PostgreSQL está instalado e acessível |
| `psql -U postgres` | Entra no console do PostgreSQL como o usuário `postgres` (pede senha) |
| `CREATE DATABASE nome;` | Cria um banco de dados novo (comando SQL — sempre termina com `;`) |
| `\l` | Lista todos os bancos de dados existentes (atalho do console `psql`) |
| `\q` | Sai do console do `psql` |
| `psql -U postgres -d <banco> -c "\d <tabela>"` | Mostra a estrutura de uma tabela específica sem precisar entrar no console interativo |

### Python — variáveis de ambiente

| Código/conceito | O que faz |
|---|---|
| `pip install python-dotenv` | Instala a biblioteca que lê arquivos `.env` |
| `load_dotenv()` | Lê o arquivo `.env` da raiz do projeto e carrega suas variáveis na memória |
| `os.getenv("NOME_VARIAVEL")` | Busca o valor de uma variável de ambiente (ex: senha do banco) sem expor ela no código |
| `python -c "código aqui"` | Roda uma linha de código Python direto no terminal, sem criar um arquivo — útil para testes rápidos |

### SQLAlchemy — conexão

| Conceito | O que é |
|---|---|
| **SQLAlchemy** | ORM — permite representar tabelas do PostgreSQL como classes Python |
| **psycopg2-binary** | Driver que permite ao SQLAlchemy se conectar de fato ao PostgreSQL |
| `create_engine(url)` | Cria o motor de conexão com o banco, a partir da URL de conexão |
| `sessionmaker(...)` | Cria uma fábrica de sessões — cada sessão é uma conversa individual com o banco |
| `declarative_base()` | Cria a classe base (`Base`) que as tabelas em `models.py` herdam para virarem tabelas reais |

---

## Fase 5 — Modelagem

### SQLAlchemy — definição de tabelas

| Conceito | O que é |
|---|---|
| `class Usuario(Base):` | Define uma classe que representa uma tabela, herdando de `Base` |
| `__tablename__ = "usuarios"` | Define o nome real da tabela no PostgreSQL |
| `Column(Integer, primary_key=True, index=True)` | Define uma coluna numérica como chave primária e indexada |
| `Column(String, nullable=False)` | Define uma coluna de texto obrigatória |
| `Column(String, unique=True, index=True, nullable=False)` | Define uma coluna de texto obrigatória, única e indexada (ex: email) |
| `Base.metadata.create_all(bind=engine)` | Cria fisicamente no banco todas as tabelas registradas em `Base` |

---

## Fase 6 — Cadastro

### Pydantic (schemas)

| Conceito | O que é |
|---|---|
| `pip install pydantic[email]` | Instala suporte à validação de formato de email |
| `class UsuarioCreate(BaseModel):` | Define o formato de dados que a API espera receber |
| `EmailStr` | Tipo do Pydantic que valida se o valor tem formato de email válido |
| `class Config: from_attributes = True` | Permite converter um objeto SQLAlchemy diretamente em um schema de resposta |

### FastAPI — banco e dependências

| Conceito | O que é |
|---|---|
| `def get_db(): ... yield db ... finally: db.close()` | Função que abre e garante o fechamento de uma sessão do banco a cada requisição |
| `Depends(get_db)` | Injeta o resultado de `get_db()` como parâmetro da rota (Dependency Injection) |
| `@app.post("/rota", response_model=Schema)` | Registra uma rota POST, validando o formato da resposta contra o schema indicado |
| `db.add(obj)` / `db.commit()` / `db.refresh(obj)` | Adiciona, salva definitivamente, e recarrega um objeto com dados gerados pelo banco (como o ---

## Fase 7 — Segurança (hash de senha)

### Passlib e bcrypt

| Conceito | O que é |
|---|---|
| `from passlib.context import CryptContext` | Importa a classe principal de gerenciamento de hash |
| `CryptContext(schemes=["bcrypt"], deprecated="auto")` | Configura o contexto para usar bcrypt como algoritmo |
| `pwd_context.hash(senha)` | Gera o hash de uma senha |
| `pwd_context.verify(senha, hash_salvo)` | Compara uma senha com um hash, retorna `True`/`False` |
| `pip install "bcrypt==X.Y.Z"` | Fixa uma versão específica de uma biblioteca, útil para resolver incompatibilidades |`id`) |

---

## Fase 8 — Login

### FastAPI — erros HTTP

| Conceito | O que é |
|---|---|
| `from fastapi import HTTPException` | Importa a classe usada para retornar erros HTTP customizados |
| `raise HTTPException(status_code=401, detail="mensagem")` | Interrompe a execução e devolve um erro HTTP com código e mensagem específicos |
| `raise` | Dispara um erro de propósito, parando a execução imediatamente naquele ponto |
| `401 Unauthorized` | Código HTTP que significa "credenciais não confirmadas" (diferente de 404, endereço não encontrado, ou 400, requisição malformada) |

### SQLAlchemy — consulta (query)

| Conceito | O que é |
|---|---|
| `db.query(Tabela).filter(condição).first()` | Busca no banco a primeira linha que bate com a condição, ou `None` se não achar |
| `Tabela.campo == valor` | Sintaxe de comparação usada dentro do `.filter()` |

---

## Fase 9 — JWT

### Datas e JWT

| Conceito | O que é |
|---|---|
| `from datetime import datetime, timedelta` | `datetime` representa um momento no tempo; `timedelta` representa uma duração (ex: 30 minutos) |
| `datetime.utcnow()` | Retorna a data/hora atual em UTC |
| `datetime.utcnow() + timedelta(minutes=30)` | Calcula "daqui a 30 minutos" a partir de agora |
| `from jose import jwt` | Importa o módulo de criação/validação de tokens JWT (pacote `python-jose`) |
| `jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)` | Monta e assina um token JWT a partir de um dicionário de dados |
| `"sub"` | Campo padrão do JWT para identificar o "dono" do token (ex: email do usuário) |
| `"exp"` | Campo padrão do JWT para a data de expiração |

---

## Fase 10 — Rotas protegidas

### FastAPI — autenticação

| Conceito | O que é |
|---|---|
| `from fastapi.security import OAuth2PasswordBearer` | Ferramenta que extrai o token do cabeçalho `Authorization` automaticamente |
| `OAuth2PasswordBearer(tokenUrl="login")` | Configura o esquema de autenticação, informando ao Swagger onde fica a rota de login |
| `jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])` | Decodifica e valida um token JWT, retornando o payload original |
| `JWTError` | Exceção lançada pelo `jose` quando o token é inválido, adulterado ou expirado |

### Terminal — testando rotas autenticadas

| Comando | O que faz |
|---|---|
| `curl.exe -X GET "<url>" -H "Authorization: Bearer <token>"` | Faz uma requisição GET incluindo o token JWT no cabeçalho, do jeito que uma aplicação real faria |

## Fase 11 — CRUD completo e testes de autenticação

### FastAPI — exclusão e edição

| Conceito | O que é |
|---|---|
| `@app.put("/usuarios/{usuario_id}")` | Rota para editar um usuário existente, usando *path parameter* para identificar qual registro alterar |
| `@app.delete("/usuarios/{usuario_id}")` | Rota para excluir um usuário existente, também via *path parameter* |
| `usuario_id: int` | *Path parameter* — parte da própria URL (`/usuarios/2`) que o FastAPI converte automaticamente em variável na função |
| `db.delete(usuario)` | Marca o registro para exclusão na sessão do SQLAlchemy |
| `db.commit()` | Confirma a exclusão (ou qualquer alteração) no banco de dados — sem isso, a mudança não é salva de verdade |
| `raise HTTPException(status_code=404, detail="...")` | Retorna erro 404 quando o `usuario_id` informado não existe no banco |

### HTTP — códigos de status usados nos testes

| Código | Significado | Quando aparece |
|---|---|---|
| `401 Unauthorized` | Não autenticado ou credenciais inválidas | Requisição sem token, ou com token inválido/expirado |
| `404 Not Found` | Recurso não encontrado | `usuario_id` que não existe no banco |
| `200 OK` | Sucesso | Requisição autenticada e válida |

### Terminal — PowerShell

| Comando | O que faz |
|---|---|
| `Invoke-RestMethod -Uri "<url>" -Method Get -Headers $headers` | Faz uma requisição HTTP (GET/POST/PUT/DELETE) incluindo headers, como o token JWT |
| `$headers = @{ Authorization = "Bearer <token>" }` | Cria um objeto de headers no PowerShell para reutilizar em várias requisições |
| `[Console]::OutputEncoding` | Mostra qual codificação de caracteres o terminal está usando para exibir texto |
| `[Console]::OutputEncoding = [System.Text.Encoding]::UTF8` | Corrige o terminal para exibir corretamente caracteres acentuados (UTF-8), evitando texto corrompido tipo `UsuÃ¡rio` |

*Documentado em: 11/08/2026 22:05*

