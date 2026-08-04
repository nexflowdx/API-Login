# 📖 Glossário — Projeto API Login

Referência rápida dos comandos e conceitos usados até a Fase 2. Vou atualizando conforme avançamos.

---

## 🖥️ Comandos PowerShell

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

### Diagnóstico (usados para resolver o problema de PATH)

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

### PowerShell — manipulação de texto (script de data)

| Comando/conceito | O que faz |
|---|---|
| `Get-Content <arquivo> -Encoding UTF8` | Lê o conteúdo de um arquivo de texto |
| `-replace 'padrão', 'substituto'` | Troca um trecho de texto por outro (aceita expressões regulares) |
| `Set-Content <arquivo> -Encoding UTF8` | Grava conteúdo de volta em um arquivo |
| `Get-Date -Format "dd/MM/yyyy HH:mm"` | Gera a data e hora atuais no formato especificado |
| `param([string]$Nome)` | Declara um parâmetro reutilizável dentro de um script `.ps1` |

---

## 🐍 Bibliotecas Python do projeto

Ainda não escrevemos código Python de verdade (isso começa na Fase 3), mas já instalamos e entendemos o papel de cada biblioteca:

| Biblioteca | Papel no projeto |
|---|---|
| **FastAPI** | Framework principal — cria as rotas da API (`/login`, `/usuarios`, etc.) |
| **Uvicorn** | Servidor que roda a aplicação FastAPI e escuta requisições |
| **SQLAlchemy** | ORM — permite representar tabelas do PostgreSQL como classes Python |
| **Passlib** | Gerencia o hashing de senhas antes de salvar no banco |
| **Bcrypt** | Algoritmo de criptografia usado por baixo dos panos pelo Passlib |
| **python-jose** | Cria e valida tokens JWT (autenticação) |

---

*Última atualização: 04/08/2026 09:12*
