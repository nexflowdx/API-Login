# Fase 2 — Estrutura profissional

## Objetivo
Organizar o projeto em pastas com responsabilidades separadas, e estabelecer o padrão de documentação (README, /docs, glossário) que seguiria o resto do projeto.

## Motivação
Uma estrutura clara desde o início evita que o código vire um único arquivo gigante, e facilita saber onde procurar cada parte da lógica conforme o projeto cresce.

## Pré-requisitos
Repositório Git inicializado (Fase 1).

## Passo a passo
1. Criação da pasta `app/`, com os arquivos vazios `main.py`, `database.py`, `models.py`, `schemas.py` e `auth.py`, cada um com uma responsabilidade única.
2. Reescrita do `README.md`, seguindo o mesmo estilo e estrutura do projeto [[nexflow-dx-vps-setup]] (secure-vps-setup), incluindo seções de Objetivo, Arquitetura, Pilha, Roteiro e Documentação.
3. Criação da pasta `docs/`, destinada a documentação detalhada por fase.
4. Criação do `SOBRE-O-PROJETO.md`, para reunir contexto e decisões do projeto.
5. Criação do `docs/glossario.md`, para reunir comandos e conceitos usados ao longo do projeto, organizados por fase.

## Como validar a configuração
- Os 5 arquivos aparecem corretamente dentro de `app/` no VS Code.
- `README.md`, `SOBRE-O-PROJETO.md` e `docs/glossario.md` publicados corretamente no GitHub.

## Lições aprendidas
Definir a estrutura de pastas e o padrão de documentação antes de escrever qualquer rota evitou retrabalho nas fases seguintes — cada arquivo novo já tinha um lugar óbvio para ir.

---
*Documentado em: 09/08/2026 21:01*
