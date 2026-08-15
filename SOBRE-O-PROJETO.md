# Sobre o Projeto — API Login

## Contexto

Este foi o primeiro projeto de backend do meu portfólio, construído do zero — literalmente: no início, meu computador nem tinha Python ou Git configurados corretamente no PATH. A ideia era clara desde o planejamento (Fase 0): construir uma API de autenticação profissional, com JWT e boas práticas de segurança, que servisse tanto como prova técnica quanto como base de autenticação reutilizável para outros projetos da Nexflow DX (e futuramente SCME, CRM, agentes de IA).

## Decisões técnicas

- **FastAPI + PostgreSQL + SQLAlchemy + JWT**, com senha sempre tratada via hash (bcrypt), nunca armazenada em texto puro.
- **Documentação fase a fase**, no formato runbook (Objetivo, Motivação, Pré-requisitos, Passo a passo, Como validar, Lições aprendidas), seguindo o mesmo padrão do meu outro projeto de portfólio, [secure-vps-setup](https://github.com/nexflowdx/secure-vps-setup).
- **Inversão da ordem das Fases 12 e 13:** o roadmap original previa integrar com o n8n antes de publicar a API. Na prática isso não era possível — o n8n já roda na VPS, e a API só existia localmente no Windows, sem rede alguma entre os dois. A ordem foi invertida: primeiro o deploy (Fase 12), depois a integração (Fase 13).
- **Reaproveitamento de infraestrutura existente:** em vez de criar um Postgres isolado só para este projeto, o deploy reaproveitou o `nexflow-postgres` já existente na VPS (criado durante o setup de infraestrutura), criando apenas um banco lógico novo (`api_login`) dentro dele — evitando desperdício de recursos.

## Tropeços reais (e o que aprendi com eles)

Nenhum projeto sai perfeito de primeira, e documentar os erros é tão importante quanto documentar os acertos:

- **Bug de encoding no PowerShell:** mensagens da API com acentos apareciam corrompidas (`UsuÃ¡rio` em vez de `Usuário`). O problema não estava no código — era o terminal usando `IBM850` em vez de `UTF-8`.
- **`requirements.txt` em UTF-16:** o `pip freeze > requirements.txt` no PowerShell gera o arquivo em UTF-16 por padrão, o que quebraria a instalação de dependências dentro do container Linux se não fosse corrigido antes do deploy.
- **`Dockerfile` case-sensitive:** o arquivo foi salvo inicialmente como `dockerfile` (minúsculo). No Windows isso não faz diferença; no Linux (onde o EasyPanel builda a imagem), faz — e o build simplesmente não encontrava o arquivo.
- **Tabela ausente em produção:** o primeiro teste de cadastro contra a API publicada falhou com `relation "usuarios" does not exist`. A tabela nunca tinha sido criada automaticamente pelo código — só existia localmente porque, na Fase 5, o comando de criação foi rodado manualmente, uma única vez. Corrigido tanto pontualmente (rodando o comando no banco de produção) quanto estruturalmente, depois, ao automatizar a criação da tabela no próprio startup da aplicação (Fase 14).
- **Porta divergente:** o `Dockerfile` expõe a aplicação na porta `8000`, mas o roteamento padrão do EasyPanel esperava porta `80` — o container subia normal, mas ficava inacessível externamente até a correção.

## Aprendizados sobre o processo, não só sobre código

- Testar uma API localmente com sucesso não garante que a infraestrutura em volta dela (schema do banco, variáveis de ambiente, portas, rede) foi replicada corretamente em produção. Só testar de ponta a ponta contra a URL pública revela esse tipo de lacuna.
- Diferenças de comportamento entre Windows (ambiente de desenvolvimento) e Linux (ambiente de produção) — case-sensitivity de arquivos, encoding padrão de terminal — são fontes reais e recorrentes de bugs de deploy, não “erros de iniciante”.
- Passos manuais executados uma única vez (como criar uma tabela via comando avulso) são dívida técnica silenciosa: funcionam até o dia em que o ambiente precisa ser recriado do zero.
- Nem sempre a ordem "lógica" de um roadmap é a ordem tecnicamente possível — vale sempre checar dependências reais entre etapas antes de segui-las na ordem planejada.

---
*Documentado em: 04/08/2026 12:23*