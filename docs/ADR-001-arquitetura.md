# ADR-001 — Arquitetura inicial

- **Status:** proposta adotada para o MVP acadêmico
- **Data:** 13/11/2026
- **Contexto:** entregar CRUD funcional, API documentada e evolução incremental até março/2027.
- **Decisão:** FastAPI + SQLAlchemy no backend; interface web responsiva em HTML/CSS/JS no primeiro incremento; SQLite para execução simples local e PostgreSQL como banco-alvo de integração/deploy.
- **Motivos:** baixo atrito de instalação, documentação OpenAPI automática, tipagem/validação, ORM e caminho de migração para PostgreSQL.
- **Consequências positivas:** API explorável em `/docs`; protótipo executável sem serviços externos; estrutura simples para equipe acadêmica.
- **Consequências/limitações:** interface sem framework SPA; autenticação e controle de acesso ainda não implementados; banco SQLite não é alvo de produção multiusuário.
- **Alternativas consideradas:** Next.js + FastAPI (mais robusto para front-end maior, mas aumenta configuração inicial); Django (admin e autenticação integrados, mas API exige configuração adicional).
- **Revisão:** reavaliar após o Marco 2, conforme feedback de usabilidade e tamanho da equipe.
