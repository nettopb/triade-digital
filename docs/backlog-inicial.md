# Backlog inicial — Projeto 10

A composição definida a priori na reunião de 18/11/2026 é de uma dupla. As atividades de análise, desenvolvimento, testes, documentação e apresentação serão organizadas entre os integrantes, com responsabilidades a detalhar no planejamento da equipe.

A visão do produto deve contemplar as funcionalidades da descrição-base. A priorização abaixo organiza as entregas acadêmicas, mas não elimina funcionalidades do escopo pretendido.

## Marco 1 — 02/12/2026 às 19h

- [ ] Consolidar problema, público-alvo e visão do produto.
- [ ] Revisar requisitos funcionais e não funcionais.
- [ ] Validar matriz de permissões e regras de negócio.
- [ ] Registrar e revisar ADR de arquitetura.
- [ ] Elaborar e revisar wireframes de baixa fidelidade para os módulos previstos.
- [ ] Organizar backlog e quadro Kanban.
- [ ] Definir entidades, relacionamentos e modelo conceitual do banco.
- [ ] Revisar documentação e preparar apresentação.

### Artefatos do Marco 1

- [Requisitos do sistema](requisitos-iniciais.md)
- [Matriz de permissões](matriz-permissoes.md)
- [ADR-001 — Arquitetura](ADR-001-arquitetura.md)
- [Wireframes de baixa fidelidade](wireframes-baixa-fidelidade.md)
- [Modelo inicial de dados](modelo-dados-inicial.md)
- [Kanban do Marco 1](kanban-marco-1.md)

## Marco 2 — 13/01/2027 às 19h

- [ ] Criar estrutura MVC em PHP.
- [ ] Configurar conexão MySQL via PDO.
- [ ] Implementar primeiro CRUD funcional, priorizando autenticação, autorização e cadastros necessários.
- [ ] Implementar primeira versão do diário de classe e frequência.
- [ ] Documentar endpoints/contratos da API, se aplicável.
- [ ] Registrar evidências e métricas da sprint.

## Marco 3 — 17/02/2027 às 19h

- [ ] Integrar módulos priorizados: diário de classe (frequência, notas, conteúdos e ocorrências), comunicados com confirmação de leitura e painel de evasão.
- [ ] Implementar regras de justificativa, correção e transferência de turma.
- [ ] Implementar autorização por perfil e escopo de escola/turma.
- [ ] Implementar relatórios e controles de dados agregados/anonimizados.
- [ ] Avançar nos módulos de chat, fórum e boletim PDF conforme priorização e capacidade.
- [ ] Configurar pipeline de publicação.
- [ ] Executar e documentar testes de aceitação, incluindo testes de acesso indevido.

## Marco 4 — 17/03/2027 às 19h

- [ ] Publicar aplicação em ambiente de nuvem.
- [ ] Preparar demonstração de 3 a 5 minutos.
- [ ] Elaborar manual de instalação e manual do usuário.
- [ ] Consolidar documentação técnica.
- [ ] Elaborar relatório de extensão conforme as orientações acadêmicas aplicáveis à equipe.

## Fluxo Kanban

A fazer → Em andamento → Em revisão/teste → Concluído.

## Critérios gerais de conclusão

Uma tarefa só será considerada concluída quando estiver implementada ou produzida, revisada/testada no escopo previsto e documentada quando necessário. Decisões ainda não confirmadas devem permanecer registradas como pendências, sem serem tratadas como requisitos definitivos.

## Organização do Git

- `main`: versão estável.
- `dev`: integração do desenvolvimento.
- Branches curtas `feature/nome-da-funcionalidade` para funcionalidades futuras.
