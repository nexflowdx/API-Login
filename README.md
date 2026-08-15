Readme · MD
🔐 API Login

Documentação da construção de uma API de autenticação profissional com FastAPI, PostgreSQL e JWT, seguindo boas práticas de backend e segurança.

🎯 Objetivo

Este repositório documenta minha jornada de aprendizado na construção de uma API de autenticação do zero, desde o planejamento até a publicação em produção.

Além de servir como material de estudo, este projeto funciona como um portfólio técnico, registrando cada etapa, as decisões tomadas e as boas práticas aplicadas.

🏗️ Arquitetura do Projeto

Esta arquitetura foi construída com foco em segurança, organização e preparação para servir como base de autenticação de outros projetos (Nexflow DX, SCME, agentes de IA).

A API utiliza FastAPI como framework principal, PostgreSQL como banco de dados, SQLAlchemy como ORM, e JWT para autenticação de rotas protegidas. Publicada em VPS própria via Docker e EasyPanel, com domínio e HTTPS próprios.

API em produção: https://api-login.nexflowdx.cloud

## 🏗️ Pilha

* FastAPI
* Uvicorn
* PostgreSQL
* SQLAlchemy
* Passlib + Bcrypt
* Python-Jose (JWT)
* Docker
* EasyPanel + Cloudflare

## 📚 Documentação

O projeto foi dividido em 15 etapas:

00. Planejamento
01. Preparação do ambiente
02. Estrutura profissional
03. Primeira API
04. Banco de dados
05. Modelagem
06. Cadastro de usuários
07. Segurança (hash de senha)
08. Login
09. JWT
10. Rotas protegidas
11. CRUD completo
12. Deploy mínimo na VPS
13. Integração com n8n
14. Hardening final

A ordem das fases 12 e 13 foi invertida em relação ao planejamento original: o deploy precisou vir antes da integração com n8n, já que o n8n roda na VPS e não conseguiria alcançar a API enquanto ela só existia localmente.

Cada etapa está documentada com Objetivo, Motivação, Pré-requisitos, Passo a passo, Como validar e Lições aprendidas — disponível na pasta /docs.

## 📋 Roteiro

* [x] Planejamento do fluxo completo
* [x] Ambiente virtual (venv)
* [x] Git e GitHub configurados
* [x] Estrutura de pastas do app
* [x] Primeira rota (GET /status)
* [x] Conexão com PostgreSQL
* [x] Modelagem da tabela de usuários
* [x] Cadastro de usuários (POST /usuarios)
* [x] Hash de senha (bcrypt)
* [x] Login (POST /login)
* [x] Geração e validação de JWT
* [x] Rotas protegidas (GET /me)
* [x] CRUD completo de usuários
* [x] Deploy mínimo na VPS (Docker + EasyPanel)
* [x] Integração com n8n
* [x] Hardening final (correção de dívida técnica + domínio próprio)


## 📚 Documentação

Cada etapa deste projeto será documentada contendo:

* Objetivo
* Motivação
* Pré-requisitos
* Passo a passo
* Como validar a configuração
* Lições aprendidas

🧠 Considerações finais

Leia mais sobre o processo de construção, os tropeços e os aprendizados: SOBRE-O-PROJETO.md

---
*Documentado em: 04/08/2026 07:52*
