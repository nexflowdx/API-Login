# Fase 13 — Integração com n8n

## 🎯 Objetivo

Construir, dentro do n8n já existente na VPS, um workflow que reproduza o ciclo completo de autenticação da API Login (login → obter token → chamar rota protegida), validando que a API publicada na Fase 12 pode ser consumida por automações reais.

## 💡 Motivação

Publicar a API não é suficiente por si só — o objetivo final dela é servir de base de autenticação para automações do Nexflow DX, começando pelo próprio n8n. Testar essa integração de ponta a ponta prova que a API está pronta para ser usada por outros workflows no futuro, não só acessível via navegador ou PowerShell.

## 📋 Pré-requisitos

- Fase 12 concluída (API publicada e acessível via `https://nexflow-api-login.tlwieg.easypanel.host`)
- Instância `nexflow-n8n` rodando na VPS
- Um usuário de teste já cadastrado na API (`producao@exemplo.com`)

## 🔨 Passo a passo

### 1. Criação do workflow

Criado um novo workflow no `nexflow-n8n` chamado `teste-autenticacao-api-login`.

### 2. Nó de início

Adicionado um nó **Manual Trigger** ("When clicking 'Execute workflow'"), permitindo rodar o workflow sob demanda durante os testes.

### 3. Nó "Login"

Nó **HTTP Request** configurado como:

- Method: `POST`
- URL: `https://nexflow-api-login.tlwieg.easypanel.host/login`
- Send Body: ativado, tipo `JSON`
- Body:
```json
{
  "email": "producao@exemplo.com",
  "senha": "senha123"
}
```

Executado isoladamente ("Execute step") e validado: retornou `access_token` e `token_type: bearer` corretamente.

### 4. Nó "Listar Usuarios"

Segundo nó **HTTP Request**, conectado à saída do nó "Login":

- Method: `GET`
- URL: `https://nexflow-api-login.tlwieg.easypanel.host/usuarios`
- Send Headers: ativado
- Header `Authorization`, valor: `Bearer {{ $json.access_token }}`

A expressão `{{ $json.access_token }}` referencia automaticamente o token retornado pelo nó anterior — nenhum valor foi copiado manualmente.

## ✅ Como validar

| Nó | Resultado |
|---|---|
| Login | ✅ `access_token` e `token_type` retornados |
| Listar Usuarios | ✅ Lista de usuários retornada corretamente, usando o token do nó anterior |

## 📚 Lições aprendidas

- O encadeamento automático de dados entre nós do n8n (`{{ $json.campo }}`) elimina a necessidade de gerenciar variáveis manualmente entre passos, ao contrário do PowerShell, onde era preciso guardar `$resposta.access_token` explicitamente numa variável.
- Testar cada nó isoladamente ("Execute step") antes de rodar o workflow inteiro ajuda a isolar problemas rapidamente — a mesma lógica dos testes negativos/positivos feitos na Fase 11.
- Validar a integração real com uma ferramenta de automação (não só o acesso direto via terminal) é o que efetivamente comprova que a API está pronta para ser consumida por outros sistemas, que é o propósito real dela dentro do Nexflow DX.

---
*Documentado em: 15/08/2026 11:41*
