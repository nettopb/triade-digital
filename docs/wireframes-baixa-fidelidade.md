# Wireframes — Tríade Digital

**Versão:** 0.1 — baixa fidelidade  
**Marco:** 1  
**Status:** proposta para validação

Os desenhos abaixo representam estrutura e hierarquia das telas, não o layout visual definitivo. A navegação e os dados exibidos devem respeitar o perfil e as permissões do usuário autenticado.

## 1. Login

```text
+--------------------------------------------------+
|                  TRÍADE DIGITAL                  |
|          Plataforma de Acompanhamento Escolar    |
|                                                  |
|  E-mail:  [________________________________]     |
|  Senha:   [________________________________]     |
|                                                  |
|                 [ Entrar ]                       |
|                                                  |
|             Esqueci minha senha                  |
+--------------------------------------------------+
```

**Comportamento:** validar credenciais no servidor; apresentar mensagem genérica em caso de falha; não revelar se determinado e-mail está cadastrado.

## 2. Painel inicial

```text
+--------------------------------------------------------------+
| TRÍADE DIGITAL                     Usuário | Perfil | Sair   |
+----------------------+---------------------------------------+
| Início               | PAINEL                                |
| Alunos               |                                       |
| Turmas               | [Total de alunos] [Turmas ativas]     |
| Frequência           | [Faltas para verificar] [Comunicados] |
| Alertas              |                                       |
| Comunicados          | Alertas recentes                      |
| Relatórios            | - Situações que exigem acompanhamento  |
|                      |                                       |
|                      | Frequência recente                    |
|                      | [Resumo por turma/período]             |
+----------------------+---------------------------------------+
```

**Comportamento:** indicadores e atalhos variam conforme o perfil. Exibir somente informações autorizadas.

## 3. Alunos — listagem

```text
+--------------------------------------------------------------+
| ALUNOS                                  [ + Novo aluno ]     |
| Buscar: [nome ou matrícula____________] [Filtrar]            |
|--------------------------------------------------------------|
| Matrícula | Nome             | Turma       | Situação | Ações |
| 0001      | Aluno Exemplo    | 1º A        | Ativo    | Ver   |
| 0002      | Aluna Exemplo    | 2º B        | Ativo    | Ver   |
|--------------------------------------------------------------|
|                         [Anterior] [Próxima]                 |
+--------------------------------------------------------------+
```

**Comportamento:** permitir busca, filtros e paginação. Exclusão física não é prevista no fluxo comum; avaliar inativação para preservar histórico.

## 4. Cadastro/edição de aluno

```text
+--------------------------------------------------------------+
| CADASTRO DE ALUNO                                            |
| Matrícula: [________________]                                |
| Nome:      [________________________________________]       |
| Data nasc.:[____/____/________]                              |
| Turma:     [Selecione________________________________]       |
| Responsável: [______________________________________]       |
| Contato do responsável: [____________________________]       |
| Situação:  (•) Ativo  ( ) Inativo                            |
|                                                              |
|                       [Cancelar] [Salvar]                    |
+--------------------------------------------------------------+
```

**Observação:** os campos são preliminares. Definir com a instituição quais dados são realmente necessários; evitar coletar dados pessoais excessivos.

## 5. Turmas

```text
+--------------------------------------------------------------+
| TURMAS                                      [ + Nova turma ] |
| Ano letivo: [________]  Buscar: [____________________]       |
|--------------------------------------------------------------|
| Código | Nome da turma | Etapa/série | Turno | Situação     |
| T01    | 1º Ano A      | Fundamental | Manhã | Ativa        |
|--------------------------------------------------------------|
| [Abrir turma] [Editar]                                       |
+--------------------------------------------------------------+
```

## 6. Frequência

```text
+--------------------------------------------------------------+
| REGISTRO DE FREQUÊNCIA                                       |
| Turma: [Selecione________] Data: [____/____/____] [Carregar] |
|--------------------------------------------------------------|
| Matrícula | Aluno             | Presença | Falta | Justificada|
| 0001      | Aluno Exemplo     | (•)      | ( )   | [ ]        |
| 0002      | Aluna Exemplo     | ( )      | (•)   | [ ]        |
|--------------------------------------------------------------|
| Observação: [___________________________________________]    |
|                                      [Salvar frequência]     |
+--------------------------------------------------------------+
```

**Comportamento:** todos os alunos iniciam como presentes; o professor desmarca os ausentes e salva. A coordenação não faz lançamento inicial. Professor e coordenação podem corrigir frequência já lançada, dentro de seus escopos, com registro de auditoria (valor anterior, novo valor, usuário, data/hora e motivo). A secretaria apenas consulta; a direção não altera.

A tela deve oferecer acesso à justificativa: flag de falta justificada, descrição, data inicial e duração em dias corridos. O sistema considera o calendário completo para contar a duração, mas aplica a justificativa somente às datas com aula prevista.

## 7. Alertas de frequência

```text
+--------------------------------------------------------------+
| ALERTAS DE FREQUÊNCIA                                        |
| Período: [________] Turma: [Todas____] Situação: [Abertos__] |
|--------------------------------------------------------------|
| Aluno          | Turma | Ocorrência         | Data | Ação     |
| Aluno Exemplo  | 1º A  | Sequência de faltas| ...  | Analisar |
|--------------------------------------------------------------|
| [Abrir histórico] [Registrar acompanhamento]                 |
+--------------------------------------------------------------+
```

**Regra definida:** exibir alerta ao atingir 3 faltas consecutivas. A coordenação consulta o histórico e registra o acompanhamento/busca ativa.

## 8. Comunicados

```text
+--------------------------------------------------------------+
| COMUNICADOS                                [ + Novo comunicado]
|--------------------------------------------------------------|
| Título              | Público-alvo     | Publicação | Status |
| Reunião de pais     | Turmas selecion. | ...        | Ativo  |
|--------------------------------------------------------------|
| [Visualizar] [Editar] [Arquivar]                             |
+--------------------------------------------------------------+
```

**Comportamento:** criar comunicado, definir público-alvo autorizado, publicar e arquivar. Regras de aprovação e confirmação de leitura ainda precisam ser validadas.

## 9. Fórum de orientação de estudos

```text
+--------------------------------------------------------------+
| FÓRUM DE ESTUDOS                         [ + Nova discussão ] |
| Minhas discussões / Convites recebidos                       |
|--------------------------------------------------------------|
| Discussão: Orientação para avaliação                         |
| Criada por: Usuário responsável                              |
| Participantes convidados: [lista de participantes]          |
|--------------------------------------------------------------|
| Mensagens e respostas                                        |
| [Escreva sua contribuição________________________] [Enviar]  |
|--------------------------------------------------------------|
| Moderação (somente criador): [Gerenciar participantes]       |
+--------------------------------------------------------------+
```

**Comportamento e controles de moderação:** somente pessoas convidadas participam. O criador da discussão, responsável pelos convites, é o moderador. Ele poderá:

- convidar participantes;
- revogar convites ainda não aceitos;
- remover participantes da discussão;
- ocultar uma mensagem inadequada, informando o motivo, e reativá-la quando cabível;
- encerrar e reabrir a discussão.

As ações de moderação devem ser registradas em histórico de auditoria, com moderador, ação, data/hora e motivo quando aplicável. Participantes comuns podem publicar mensagens e respostas, mas não administrar convites nem moderar conteúdos.

## 10. Calendário escolar e justificativas

```text
+--------------------------------------------------------------+
| CALENDÁRIO / JUSTIFICATIVA                                   |
| Aluno: [________________________]                            |
| Início: [__/__/____] Duração (dias corridos): [___]          |
| Descrição: [___________________________________________]     |
| Intervalo calculado: [__/__/____] até [__/__/____]           |
|--------------------------------------------------------------|
| Dias letivos abrangidos: [lista de datas]                    |
| Dias sem aula no intervalo: [lista informativa]              |
|                                      [Salvar justificativa]  |
+--------------------------------------------------------------+
```

**Comportamento:** a duração inclui sábados, domingos, feriados e dias sem aula. A justificativa só gera/associa registros de frequência nas datas letivas com frequência prevista; não deve criar registros em dias sem aula.

## 11. Chat com responsáveis

```text
+--------------------------------------------------------------+
| CHAT COM RESPONSÁVEIS                                        |
| Horário de atendimento: 09h–10h e 14h–15h                    |
|--------------------------------------------------------------|
| Conversa                                                     |
| [Histórico de mensagens]                                     |
|                                                              |
| [Digite sua mensagem___________________________] [Enviar]    |
+--------------------------------------------------------------+
```

**Comportamento:** durante as janelas de atendimento, o chat funciona normalmente. Fora delas, ao receber tentativa de envio, o sistema retorna automaticamente: “Nosso horário de atendimento é das 09h às 10h e das 14h às 15h. Por favor, entre em contato durante esse período.” Não foi definida fila de mensagens nem promessa de resposta posterior.

## 12. Princípios de usabilidade considerados

- Consistência de cabeçalho, menu lateral, botões e nomenclaturas.
- Reconhecimento em vez de memorização: rótulos explícitos e filtros visíveis.
- Prevenção de erros: confirmação em ações sensíveis e validação de formulários.
- Feedback: informar sucesso, falha e estado de processamento.
- Acessibilidade: contraste adequado, navegação por teclado, rótulos associados aos campos e mensagens que não dependam apenas de cor.
- Simplicidade: apresentar apenas ações pertinentes ao perfil do usuário.

## 13. Pontos para validação

1. Quais perfis podem cadastrar, editar e inativar alunos?
2. Quem pode lançar, corrigir e consultar frequência?
3. Qual regra institucional define alerta de faltas consecutivas?
4. Quem recebe e acompanha alertas?
5. Comunicados exigem aprovação? É necessário registrar leitura?
6. Quais indicadores são úteis para cada perfil?
7. Confirmar se os controles de moderação propostos atendem à dinâmica do fórum.

