# Kanban — Marco 1

**Projeto:** Tríade Digital  
**Responsável:** Paulo Bezerra Netto.  
**Segundo integrante indicado:** Fabrício Melo.
**Prazo do marco:** 02/12/2026, às 19h  
**Branch de trabalho:** `dev`

## Fluxo

`A fazer` → `Em andamento` → `Em revisão/teste` → `Concluído`

A equipe deverá limitar o trabalho em andamento para manter o fluxo previsível, evitando excesso de tarefas simultâneas.

## Quadro inicial

| ID | Tarefa | Prioridade | Estimativa | Estado inicial |
|---|---|---:|---:|---|
| M1-01 | Revisar escopo e delimitar MVP | Alta | 1 h | A fazer |
| M1-02 | Detalhar requisitos funcionais e não funcionais | Alta | 2 h | A fazer |
| M1-03 | Validar regras de negócio pendentes | Alta | 2 h | A fazer |
| M1-04 | Revisar ADR-001 e justificativa tecnológica | Alta | 1 h | A fazer |
| M1-05 | Elaborar wireframes de baixa fidelidade | Alta | 3 h | A fazer |
| M1-06 | Elaborar modelo entidade-relacionamento | Alta | 2 h | A fazer |
| M1-07 | Organizar backlog priorizado e critérios de aceite | Alta | 1 h | A fazer |
| M1-08 | Organizar repositório, branches e documentação | Média | 1 h | Em revisão/teste |
| M1-09 | Revisar pacote de entrega e preparar apresentação | Alta | 2 h | A fazer |

**Estimativa inicial total:** 15 horas. Estimativas são referência de planejamento, não compromisso de duração exata.

## Critérios de conclusão do Marco 1

- [ ] Escopo do MVP documentado e funcionalidades fora do MVP identificadas.
- [ ] Requisitos funcionais e não funcionais identificados e rastreáveis.
- [ ] Regras ainda não confirmadas registradas como pendências, sem decisões inventadas.
- [ ] ADR-001 documenta arquitetura proposta, alternativas e consequências.
- [ ] Wireframes cobrem os principais fluxos do MVP.
- [ ] Modelo ER inicial documenta entidades, relacionamentos e restrições propostas.
- [ ] Backlog priorizado com tarefas pequenas e critérios de aceite.
- [ ] Repositório possui documentação versionada e branches `main` e `dev`.
- [ ] Apresentação do marco preparada.

## Política de trabalho com Git

- `main`: versão estável; não desenvolver diretamente nela.
- `dev`: integração do desenvolvimento.
- Para funcionalidades futuras, criar branches curtas a partir de `dev`, por exemplo `feature/cadastro-alunos`.
- Commits pequenos, com mensagens objetivas.
- Revisar/testar antes de integrar em `dev`; promover para `main` somente versões estáveis.

## Métricas simples

Ao final de cada ciclo, registrar:
- Itens concluídos.
- Itens iniciados e não concluídos.
- Estimativa versus esforço realizado.
- Impedimentos e decisões pendentes.

Registrar métricas do fluxo da equipe com cautela; um único ciclo ainda não permite estabelecer uma velocidade estável.
