# 🔐 API Login

Documentação da construção de uma API de autenticação profissional com FastAPI, PostgreSQL e JWT, seguindo boas práticas de backend e segurança.

## 🎯 Objetivo

Este repositório documenta minha jornada de aprendizado na construção de uma API de autenticação do zero, desde o planejamento até a publicação em produção.

Além de servir como material de estudo, este projeto funciona como um portfólio técnico, registrando cada etapa, as decisões tomadas e as boas práticas aplicadas.

## 🏗️ Arquitetura do Projeto

Esta arquitetura foi construída com foco em segurança, organização e preparação para servir como base de autenticação de outros projetos (Nexflow DX, SCME, agentes de IA).

A API utiliza FastAPI como framework principal, PostgreSQL como banco de dados, SQLAlchemy como ORM, e JWT para autenticação de rotas protegidas.

## 🏗️ Pilha

* FastAPI
* Uvicorn
* PostgreSQL
* SQLAlchemy
* Passlib + Bcrypt
* Python-Jose (JWT)
* Docker (deploy)

## 📚 Documentação

O projeto foi dividido em 14 etapas:

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
12. Publicação (Docker, VPS, EasyPanel)
13. Integração com n8n

A documentação completa está disponível na pasta:
[/docs](https://github.com/nexflowdx/API-Login/blob/main/docs)

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
* [ ] Integração com n8n
* [x] Publicação (Docker + VPS)

## 📚 Documentação

Cada etapa deste projeto será documentada contendo:

* Objetivo
* Motivação
* Pré-requisitos
* Passo a passo
* Como validar a configuração
* Lições aprendidas

## 🧠 Considerações finais

Leia mais sobre o processo de construção:
[SOBRE-O-PROJETO.md](https://github.com/nexflowdx/API-Login/blob/main/SOBRE-O-PROJETO.md)

---
*Documentado em: 04/08/2026 07:52*
