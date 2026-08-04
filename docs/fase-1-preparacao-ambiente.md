# Fase 1 — Preparação do ambiente

## Objetivo
Preparar o ambiente de desenvolvimento local: estrutura de pastas, ambiente virtual Python, e versionamento com Git/GitHub.

## Motivação
Uma base de ambiente bem configurada evita retrabalho e problemas de dependências nas fases seguintes, além de já deixar o projeto rastreável desde o primeiro commit.

## Pré-requisitos
Python instalado e acessível no PATH do sistema; Git instalado e configurado.

## Passo a passo
1. Criação da pasta raiz do projeto (`API-Login/`) e abertura no VS Code.
2. Criação do ambiente virtual: `python -m venv .venv`.
3. Correção de um problema de PATH do Windows, onde o comando `python` apontava para o stub da Microsoft Store em vez da instalação real — resolvido reordenando o PATH e reiniciando o Explorer do Windows.
4. Instalação e configuração do Git (nunca usado localmente antes, só pela interface web do GitHub): `git config --global user.name` e `user.email`.
5. Inicialização do repositório: `git init`.
6. Criação do `.gitignore`, excluindo `.venv/`, `__pycache__/`, `*.pyc` e `.env`.
7. Documentação inicial no `README.md`.
8. Primeiro commit e push para `https://github.com/nexflowdx/API-Login`.

## Como validar a configuração
- `python --version` retorna a versão correta sem erro.
- `git status` não lista a pasta `.venv` como alterável (confirma que o `.gitignore` está funcionando).
- Repositório visível e atualizado em `https://github.com/nexflowdx/API-Login`.

## Lições aprendidas
Problemas de PATH no Windows não são erros de programação, mas de configuração do sistema — o comando `Get-Command -All` foi essencial para identificar qual `python.exe` estava sendo priorizado incorretamente. Também ficou claro que mudanças de variável de ambiente exigem reiniciar processos (Explorer ou terminal) para serem aplicadas.

---
*Documentado em: 04/08/2026 08:01*
