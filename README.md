# Tríade Digital — MVP acadêmico

MVP web para gestão escolar: cadastro de estudantes, turmas, frequência e alertas de faltas consecutivas.

## Stack
- API: Python 3.12 + FastAPI + SQLAlchemy
- Banco local: SQLite (facilita demonstração acadêmica)
- Banco de referência para implantação: PostgreSQL (docker-compose)
- Interface: HTML/CSS/JavaScript responsivo servido pela API

## Executar localmente
```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Abra http://127.0.0.1:8000 e a documentação da API em http://127.0.0.1:8000/docs.

Por padrão, usa SQLite em `backend/triade.db`. Para PostgreSQL, configure `DATABASE_URL` (exemplo em `.env.example`).

## Escopo implementado
- CRUD de estudantes
- CRUD de turmas
- Registro de frequência por data
- Painel de alertas: 3 ou mais faltas consecutivas em dias letivos registrados
- Documentação OpenAPI automática

## Limitações deliberadas do MVP
- Dados demonstrativos; não inserir dados reais de crianças/adolescentes.
- Autenticação, autorização por perfil, mensageria, integração externa, trilha de auditoria completa e deploy público ainda precisam ser implementados e testados antes de qualquer uso real.
- A regra de alerta considera apenas datas com chamada registrada para a turma. Calendário letivo, justificativas, feriados e abono devem ser refinados com a instituição.

## Estrutura
- `backend/app/main.py`: API e inicialização do banco
- `backend/static/`: interface
- `docs/`: backlog, ADR, requisitos revisados, plano dos marcos e wireframes textuais
