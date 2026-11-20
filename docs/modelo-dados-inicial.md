# Modelo de Dados — Tríade Digital

**Versão:** 0.2 — modelo conceitual/lógico inicial revisado  
**Marco:** 1  
**Status:** proposta para validação; ainda não é o script SQL definitivo.

## 1. Premissas

- Banco relacional MySQL, identificadores numéricos e datas/horários armazenados no banco.
- A autorização será aplicada no servidor em toda consulta e operação, considerando perfil, escola e vínculo do professor com a turma.
- A escola é a unidade de segregação dos dados escolares. A Gestão da Secretaria de Educação consulta somente resultados agregados e anonimizados.
- O vínculo do aluno com a turma mantém histórico; transferências não alteram nem apagam frequências anteriores.
- O registro de frequência identifica aluno, turma, data da atividade e usuário que realizou o lançamento inicial. Correções ficam em trilha de auditoria.
- A justificativa é contada em dias corridos, mas aplicada somente às datas letivas com frequência prevista.
- Dados fictícios serão utilizados no desenvolvimento acadêmico.

## 2. Diagrama entidade-relacionamento proposto

O diagrama contempla os módulos previstos nos requisitos. Cardinalidades e atributos ainda dependentes de decisões institucionais permanecem sujeitos à validação.

~~~mermaid
erDiagram
    ESCOLA ||--o{ USUARIO : possui
    ESCOLA ||--o{ TURMA : organiza
    ESCOLA ||--o{ ALUNO : matricula
    PERFIL ||--o{ USUARIO : classifica
    USUARIO ||--o{ USUARIO_TURMA : vincula
    TURMA ||--o{ USUARIO_TURMA : possui_professor
    ALUNO ||--o{ ALUNO_RESPONSAVEL : possui
    RESPONSAVEL ||--o{ ALUNO_RESPONSAVEL : acompanha
    ALUNO ||--o{ MATRICULA_TURMA : possui
    TURMA ||--o{ MATRICULA_TURMA : recebe
    ESCOLA ||--o{ CALENDARIO_ESCOLAR : define
    CALENDARIO_ESCOLAR ||--o{ DIA_CALENDARIO : contem
    ALUNO ||--o{ FREQUENCIA : possui
    TURMA ||--o{ FREQUENCIA : organiza
    USUARIO ||--o{ FREQUENCIA : lanca
    JUSTIFICATIVA o|--o{ FREQUENCIA : fundamenta
    FREQUENCIA ||--o{ AUDITORIA_FREQUENCIA : possui
    ALUNO ||--o{ ALERTA : origina
    TURMA ||--o{ ALERTA : contextualiza
    ALERTA ||--o{ ACAO_BUSCA_ATIVA : acompanha
    USUARIO ||--o{ ACAO_BUSCA_ATIVA : registra
    USUARIO ||--o{ COMUNICADO : publica
    COMUNICADO ||--o{ COMUNICADO_DESTINATARIO : direciona
    COMUNICADO ||--o{ COMUNICADO_LEITURA : recebe_confirmacao
    RESPONSAVEL ||--o{ COMUNICADO_LEITURA : confirma
    RESPONSAVEL ||--o{ CHAT_CONVERSA : participa
    USUARIO ||--o{ CHAT_CONVERSA : atende
    CHAT_CONVERSA ||--o{ CHAT_MENSAGEM : contem
    USUARIO ||--o{ DISCUSSAO_FORUM : cria
    DISCUSSAO_FORUM ||--o{ CONVITE_FORUM : possui
    USUARIO ||--o{ CONVITE_FORUM : recebe
    DISCUSSAO_FORUM ||--o{ PARTICIPACAO_FORUM : autoriza
    USUARIO ||--o{ PARTICIPACAO_FORUM : participa
    DISCUSSAO_FORUM ||--o{ MENSAGEM_FORUM : contem
    USUARIO ||--o{ MENSAGEM_FORUM : escreve
    DISCUSSAO_FORUM ||--o{ MODERACAO_FORUM : registra
    USUARIO ||--o{ MODERACAO_FORUM : modera

    ESCOLA {
      int id PK
      varchar nome
      varchar codigo UK
      boolean ativa
    }
    PERFIL {
      int id PK
      varchar nome UK
      varchar descricao
    }
    USUARIO {
      int id PK
      int escola_id FK
      int perfil_id FK
      varchar nome
      varchar email UK
      varchar senha_hash
      boolean ativo
      datetime criado_em
    }
    USUARIO_TURMA {
      int id PK
      int usuario_id FK
      int turma_id FK
      date data_inicio
      date data_fim
    }
    ALUNO {
      int id PK
      int escola_id FK
      varchar matricula
      varchar nome
      date data_nascimento
      boolean ativo
      datetime criado_em
    }
    RESPONSAVEL {
      int id PK
      varchar nome
      varchar email
      varchar telefone
      boolean ativo
    }
    ALUNO_RESPONSAVEL {
      int id PK
      int aluno_id FK
      int responsavel_id FK
      varchar parentesco
      boolean principal
    }
    TURMA {
      int id PK
      int escola_id FK
      varchar codigo
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
    CALENDARIO_ESCOLAR {
      int id PK
      int escola_id FK
      int ano_letivo
      varchar descricao
    }
    DIA_CALENDARIO {
      int id PK
      int calendario_id FK
      date data
      varchar tipo_dia
      boolean possui_aula
    }
    FREQUENCIA {
      int id PK
      int aluno_id FK
      int turma_id FK
      int usuario_lancamento_id FK
      int justificativa_id FK
      date data_aula
      varchar situacao
      text observacao
      datetime registrado_em
    }
    JUSTIFICATIVA {
      int id PK
      int aluno_id FK
      int usuario_id FK
      date data_inicio
      int duracao_dias_corridos
      date data_fim_calculada
      text descricao
      datetime criado_em
    }
    AUDITORIA_FREQUENCIA {
      int id PK
      int frequencia_id FK
      int usuario_id FK
      varchar valor_anterior
      varchar valor_novo
      text motivo
      datetime alterado_em
    }
    ALERTA {
      int id PK
      int aluno_id FK
      int turma_id FK
      varchar tipo
      date periodo_inicio
      date periodo_fim
      varchar status
      datetime criado_em
      datetime atualizado_em
    }
    ACAO_BUSCA_ATIVA {
      int id PK
      int alerta_id FK
      int usuario_id FK
      varchar tipo_acao
      text descricao
      varchar status
      datetime registrada_em
      datetime atualizada_em
    }
    COMUNICADO {
      int id PK
      int usuario_id FK
      varchar titulo
      text conteudo
      datetime publicado_em
      varchar status
    }
    COMUNICADO_DESTINATARIO {
      int id PK
      int comunicado_id FK
      varchar tipo_destino
      int destino_id
    }
    COMUNICADO_LEITURA {
      int id PK
      int comunicado_id FK
      int responsavel_id FK
      datetime confirmado_em
    }
    CHAT_CONVERSA {
      int id PK
      int responsavel_id FK
      int usuario_atendente_id FK
      varchar status
      datetime criada_em
    }
    CHAT_MENSAGEM {
      int id PK
      int conversa_id FK
      varchar remetente_tipo
      int remetente_id
      text conteudo
      boolean resposta_automatica
      datetime enviada_em
    }
    DISCUSSAO_FORUM {
      int id PK
      int criador_usuario_id FK
      varchar titulo
      text descricao
      varchar status
      datetime criada_em
      datetime atualizada_em
    }
    CONVITE_FORUM {
      int id PK
      int discussao_id FK
      int usuario_convidado_id FK
      int convidado_por_id FK
      varchar status
      datetime enviado_em
      datetime respondido_em
    }
    PARTICIPACAO_FORUM {
      int id PK
      int discussao_id FK
      int usuario_id FK
      varchar status
      datetime entrou_em
      datetime removido_em
    }
    MENSAGEM_FORUM {
      int id PK
      int discussao_id FK
      int usuario_id FK
      text conteudo
      varchar status
      datetime criada_em
      datetime atualizada_em
    }
    MODERACAO_FORUM {
      int id PK
      int discussao_id FK
      int usuario_moderador_id FK
      varchar tipo_acao
      int mensagem_id FK
      int participante_id FK
      text motivo
      datetime criado_em
    }
~~~

## 3. Regras de integridade e autorização

### 3.1. Usuários, escola e turmas

- Cada usuário escolar pertence a uma escola e possui um perfil.
- USUARIO_TURMA delimita as turmas às quais o professor tem acesso. A aplicação valida esse vínculo em cada requisição.
- A Gestão da Secretaria de Educação não recebe registros individualizados. Consultas e exportações desse perfil serão construídas sobre dados agregados e anonimizados; não se concede acesso direto às tabelas pessoais.
- Os campos e operações de cadastro de usuários, perfis e vínculos ainda dependem de definição institucional.

### 3.2. Alunos, responsáveis e matrícula

- RESPONSAVEL e ALUNO são entidades separadas. ALUNO_RESPONSAVEL permite mais de um responsável por aluno e um responsável vinculado a mais de um aluno.
- MATRICULA_TURMA registra o histórico. Uma transferência encerra o vínculo anterior e inicia outro, sem mover ou apagar FREQUENCIA já registrada.
- A Secretaria altera somente dados cadastrais; não altera frequência, notas ou outros registros acadêmicos.
- A unicidade da matrícula e as regras para vínculos simultâneos permanecem pendentes.

### 3.3. Frequência, justificativas e auditoria

- O lançamento inicial é realizado pelo professor, restrito às próprias turmas. A coordenação não lança frequência inicial.
- Professor e coordenação podem corrigir frequência já lançada, respeitando o escopo previsto. Secretaria apenas consulta; direção não altera.
- Cada correção gera AUDITORIA_FREQUENCIA com valor anterior, valor novo, usuário, data/hora e motivo, sem apagar o histórico.
- JUSTIFICATIVA registra data inicial, duração em dias corridos, data final calculada e descrição. A aplicação consulta DIA_CALENDARIO e associa a justificativa somente às datas letivas com frequência prevista.
- Não se criam registros de frequência em fins de semana, feriados ou dias sem aula.
- A frequência mantém a turma original associada ao registro histórico.

### 3.4. Alertas e busca ativa

- ALERTA representa a ocorrência de três faltas consecutivas.
- ACAO_BUSCA_ATIVA registra ações realizadas pela coordenação e seu estado de acompanhamento.
- A coordenação consulta os alertas da escola e registra o acompanhamento. Os demais perfis recebem somente indicadores previstos na matriz.

### 3.5. Comunicados e confirmação de leitura

- COMUNICADO registra autor, título, conteúdo e estado de publicação.
- COMUNICADO_DESTINATARIO permite direcionar o comunicado à escola, turma ou aluno, conforme autorização do perfil que publica.
- COMUNICADO_LEITURA registra a confirmação por responsável. A regra exige confirmação de leitura; o tratamento de múltiplos responsáveis permanece pendente.
- Professor, coordenação e direção podem publicar comunicados. A consulta de indicadores e confirmações respeita a matriz de permissões.

### 3.6. Chat com responsáveis

- CHAT_CONVERSA e CHAT_MENSAGEM representam conversas e mensagens entre responsáveis e usuários atendentes autorizados.
- As janelas são fixas para toda a escola: 09h–10h e 14h–15h.
- Fora dessas janelas, o sistema retorna a mensagem automática definida nos requisitos. CHAT_MENSAGEM identifica respostas automáticas.
- Não há requisito de fila ou promessa de resposta posterior fora do horário.

### 3.7. Fórum de orientação de estudos

- Somente usuários convidados podem participar da discussão.
- O criador da discussão, responsável por chamar/convidar os participantes, é o moderador.
- CONVITE_FORUM controla convites e respostas; PARTICIPACAO_FORUM registra a participação autorizada.
- MENSAGEM_FORUM armazena mensagens e respostas. MODERACAO_FORUM audita convites revogados, remoções, ocultação/reativação de mensagens e encerramento/reabertura da discussão.
- Participantes comuns podem publicar mensagens e respostas, mas não administrar convites nem executar ações de moderação.

## 4. Restrições preliminares

- USUARIO.email deve ser único.
- A unicidade de ALUNO.matricula depende da confirmação institucional.
- A restrição única de FREQUENCIA depende da decisão sobre frequência diária ou por aula/horário.
- Datas de MATRICULA_TURMA não devem permitir vínculos simultâneos conflitantes, conforme regra de transferência/rematrícula a validar.
- Exclusões físicas não devem apagar histórico acadêmico ou trilhas de auditoria.
- A aplicação deve negar por padrão operações não autorizadas e validar o escopo no servidor.

## 5. Decisões ainda pendentes

1. A matrícula do aluno é única por escola, por ano letivo ou em toda a rede?
2. Um aluno pode estar em mais de uma turma no mesmo período?
3. A frequência será diária ou por aula/horário?
4. Quais situações de frequência serão aceitas além de presente, falta e falta justificada?
5. Qual é a data efetiva da transferência e como tratar chamadas ainda não lançadas?
6. Quais campos cadastrais de responsáveis são realmente necessários?
7. A confirmação de leitura será exigida de cada responsável individualmente quando houver mais de um vinculado ao aluno?
8. Quais perfis poderão consultar confirmações individuais de leitura, além dos indicadores descritos na matriz?
9. Quais são as etapas, os estados e os tipos de ação da busca ativa?
10. Qual técnica e limiar mínimo serão utilizados para agregação/anonimização, evitando reidentificação?
11. Quem administra usuários, perfis, escolas e vínculos de professores às turmas?
12. Quais consultas individuais de alunos a direção poderá acessar, além dos indicadores consolidados?
13. Quais perfis escolares poderão realizar exportações não anonimizadas, se houver essa necessidade?

## 6. Próxima etapa

Após a validação das regras e das decisões pendentes, detalhar tipos, chaves, índices e restrições, produzir o modelo lógico definitivo e elaborar o script SQL. Não utilizar dados reais de menores no ambiente acadêmico sem autorização institucional e controles adequados de privacidade e segurança.
