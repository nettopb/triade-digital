# Modelo de Dados — Tríade Digital

**Versão:** 0.1 — conceitual/lógico inicial  
**Marco:** 1  
**Status:** proposta; revisar após validação dos requisitos.

## 1. Premissas

- Banco relacional MySQL.
- Identificadores internos numéricos.
- Datas e horários registrados no banco.
- Usuários vinculados a perfis; autorização aplicada no servidor.
- Aluno pode possuir histórico de vínculo com turma, em vez de sobrescrever a turma anterior.
- Frequência registrada por aluno e data, associada à turma.
- Alertas devem preservar o motivo, o período analisado e o estado de acompanhamento.
- Dados fictícios durante desenvolvimento acadêmico.

## 2. Diagrama entidade-relacionamento

```mermaid
erDiagram
    PERFIL ||--o{ USUARIO : classifica
    USUARIO ||--o{ FREQUENCIA : registra
    USUARIO ||--o{ ALERTA : acompanha
    USUARIO ||--o{ COMUNICADO : publica
    ALUNO ||--o{ MATRICULA_TURMA : possui
    TURMA ||--o{ MATRICULA_TURMA : recebe
    ALUNO ||--o{ FREQUENCIA : possui
    TURMA ||--o{ FREQUENCIA : organiza
    ALUNO ||--o{ ALERTA : origina
    TURMA ||--o{ ALERTA : contextualiza
    COMUNICADO ||--o{ COMUNICADO_TURMA : direciona
    TURMA ||--o{ COMUNICADO_TURMA : recebe

    PERFIL {
      int id PK
      varchar nome
      varchar descricao
    }
    USUARIO {
      int id PK
      int perfil_id FK
      varchar nome
      varchar email UK
      varchar senha_hash
      boolean ativo
      datetime criado_em
    }
    ALUNO {
      int id PK
      varchar matricula UK
      varchar nome
      date data_nascimento
      varchar nome_responsavel
      varchar contato_responsavel
      boolean ativo
      datetime criado_em
    }
    TURMA {
      int id PK
      varchar codigo UK
      varchar nome
      varchar etapa
      varchar turno
      int ano_letivo
      boolean ativa
    }
    MATRICULA_TURMA {
      int id PK
      int aluno_id FK
      int turma_id FK
      date data_inicio
      date data_fim
      varchar situacao
    }
    FREQUENCIA {
      int id PK
      int aluno_id FK
      int turma_id FK
      int usuario_id FK
      date data_aula
      varchar situacao
      varchar observacao
      datetime registrado_em
    }
    ALERTA {
      int id PK
      int aluno_id FK
      int turma_id FK
      int usuario_responsavel_id FK
      varchar tipo
      text descricao
      date periodo_inicio
      date periodo_fim
      varchar status
      datetime criado_em
      datetime atualizado_em
    }
    COMUNICADO {
      int id PK
      int usuario_id FK
      varchar titulo
      text conteudo
      datetime publicado_em
      varchar status
    }
    COMUNICADO_TURMA {
      int id PK
      int comunicado_id FK
      int turma_id FK
    }
```

## 3. Regras e restrições preliminares

- `USUARIO.email` deve ser único.
- `ALUNO.matricula` deve ser única, se a instituição confirmar que a matrícula é identificador único e permanente.
- `FREQUENCIA` deve possuir restrição única para aluno + turma + data da aula, caso seja confirmado que existe apenas um registro diário por aluno/turma.
- `MATRICULA_TURMA` deve impedir vínculos simultâneos conflitantes para o mesmo aluno, conforme regra de transferência e rematrícula.
- Senhas armazenadas exclusivamente como hash seguro gerado pela aplicação.
- Operações de leitura e escrita devem respeitar perfil, escopo institucional e vínculo com turma.
- Inativação de aluno/usuário não deve apagar registros históricos.

## 4. Decisões ainda pendentes

1. A matrícula é globalmente única ou única por ano letivo/instituição?
2. Um aluno pode estar em mais de uma turma no mesmo período?
3. Frequência é diária ou por aula/horário?
4. Quais situações são permitidas: presente, falta, falta justificada, atraso, atividade remota?
5. Como registrar correção de frequência e manter trilha de auditoria?
6. Alertas serão gerados automaticamente ou inicialmente por consulta/regra executada pelo sistema?
7. Quais campos de responsável são necessários e autorizados?
8. Comunicados serão gerais, por turma ou por perfil?

## 5. Entidades complementares propostas para as regras já definidas

As entidades abaixo complementam o modelo conceitual para suportar calendário escolar, justificativas, auditoria e funcionalidades de comunicação. Os campos são propostas iniciais e deverão ser refinados antes do SQL definitivo.

| Entidade | Campos principais propostos | Finalidade |
|---|---|---|
| CALENDARIO_ESCOLAR | id, escola_id, ano_letivo, descricao | Identificar o calendário aplicável à escola e ao ano letivo. |
| DIA_CALENDARIO | id, calendario_id, data, tipo_dia, possui_aula | Registrar dias letivos, feriados, recessos e dias sem aula. |
| JUSTIFICATIVA | id, aluno_id, data_inicio, duracao_dias_corridos, descricao, usuario_id, criado_em | Guardar a justificativa e seu intervalo em dias corridos. |
| AUDITORIA_FREQUENCIA | id, frequencia_id, usuario_id, valor_anterior, valor_novo, motivo, alterado_em | Manter histórico de cada correção de frequência. |
| COMUNICADO_LEITURA | id, comunicado_id, responsavel_id, confirmado_em | Registrar a confirmação individual de leitura do comunicado. |
| DISCUSSAO_FORUM | id, criador_usuario_id, titulo, conteudo, criado_em, status | Representar a discussão criada e moderada por quem convidou. |
| CONVITE_FORUM | id, discussao_id, usuario_convidado_id, convidado_por_id, status, enviado_em, respondido_em | Controlar quem foi convidado e se aceitou participar. |
| PARTICIPACAO_FORUM | id, discussao_id, usuario_id, entrou_em, status | Registrar participantes autorizados na discussão. |

### Regras de relacionamento e processamento

- A data inicial e a duração da justificativa definem um intervalo de calendário; o sistema calcula a data final considerando dias corridos.
- A aplicação da justificativa à frequência consulta DIA_CALENDARIO e alcança somente dias com possui_aula = true. Não criar frequência em fins de semana, feriados ou dias sem aula.
- Cada correção gera um registro em AUDITORIA_FREQUENCIA, sem sobrescrever o histórico de alterações.
- A transferência encerra o vínculo anterior em MATRICULA_TURMA e inicia outro vínculo, preservando FREQUENCIA associada à turma original e à data em que ocorreu.
- A confirmação de leitura deve ser registrada por destinatário/responsável, permitindo identificar pendências quando houver mais de um responsável vinculado ao aluno.
- Somente usuários convidados podem integrar a discussão. O criador da discussão, responsável pelos convites, recebe a permissão de moderação.

## 6. Próxima etapa

Após validar as regras, converter este modelo em modelo lógico definitivo e script SQL de criação. Não utilizar dados reais de menores no ambiente acadêmico sem autorização institucional e controles adequados de privacidade e segurança.
