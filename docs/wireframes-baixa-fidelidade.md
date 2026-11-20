# Wireframes — Tríade Digital

**Versão:** 0.2 — baixa fidelidade revisada  
**Marco:** 1  
**Status:** proposta para validação

Os desenhos representam estrutura e hierarquia das telas, não o layout visual definitivo. A interface deverá apresentar somente as informações e ações permitidas ao perfil autenticado. A autorização deverá ser validada no servidor, mesmo quando um botão não estiver visível.

## 1. Login

~~~text
+--------------------------------------------------+
|                  TRÍADE DIGITAL                  |
|          Plataforma de Acompanhamento Escolar    |
|                                                  |
|  E-mail:  [________________________________]     |
|  Senha:   [________________________________]     |
|                                                  |
|                 [ Entrar ]                       |
|                                                  |
|             [Esqueci minha senha]                |
+--------------------------------------------------+
~~~

**Comportamento:** validar credenciais no servidor; apresentar mensagem genérica em caso de falha; não revelar se determinado e-mail está cadastrado.

## 2. Painel inicial por perfil

~~~text
+--------------------------------------------------------------+
| TRÍADE DIGITAL                       Usuário | Perfil | Sair |
+----------------------+---------------------------------------+
| Menu conforme perfil | PAINEL                                |
|                      | Indicadores autorizados               |
|                      |                                       |
|                      | Atividades e alertas recentes         |
|                      |                                       |
|                      | Consultas e atalhos permitidos        |
+----------------------+---------------------------------------+
~~~

**Conteúdo por perfil:**

- **Professor:** resumo das próprias turmas, frequência, notas, conteúdos, ocorrências e comunicados do seu escopo.
- **Coordenação:** visão da escola, alertas de três faltas consecutivas, justificativas e acompanhamento/busca ativa.
- **Direção:** indicadores consolidados da escola, comunicados institucionais e engajamento; sem ações de alteração de frequência.
- **Secretaria:** consultas cadastrais, matrículas, frequência somente para consulta e emissão de boletins PDF.
- **Gestão da Secretaria de Educação:** somente indicadores agregados e anonimizados por escola/região/rede; sem nomes, matrículas ou registros individuais.

## 3. Alunos — consulta e cadastro

~~~text
+--------------------------------------------------------------+
| ALUNOS                                                       |
| Buscar: [nome ou matrícula________________] [Filtrar]        |
|--------------------------------------------------------------|
| Matrícula | Nome             | Turma       | Situação | Ação  |
| 0001      | Aluno Exemplo    | 1º A        | Ativo    | Ver   |
| 0002      | Aluna Exemplo    | 2º B        | Ativo    | Ver   |
|--------------------------------------------------------------|
|                         [Anterior] [Próxima]                 |
+--------------------------------------------------------------+
~~~

**Comportamento e permissões:**

- Professor: consulta somente alunos das próprias turmas.
- Coordenação: consulta todos os alunos da escola.
- Secretaria: consulta e altera somente dados cadastrais, conforme atribuição definida.
- Direção: consultas individuais além dos relatórios consolidados ainda dependem de definição; não presumir acesso irrestrito.
- Gestão da Secretaria de Educação: não acessa listagem individual; recebe apenas dados agregados e anonimizados.
- A matriz ainda não define todos os responsáveis por criação/inativação de alunos. Não exibir ações de cadastro/edição a outros perfis até essa definição.

## 4. Cadastro e edição cadastral do aluno

~~~text
+--------------------------------------------------------------+
| DADOS CADASTRAIS DO ALUNO                                    |
| Matrícula: [________________]                                |
| Nome:      [________________________________________]       |
| Data nasc.:[____/____/________]                              |
| Responsáveis vinculados: [Consultar / editar vínculos]      |
| Situação cadastral: [Ativo/Inativo]                          |
|                                      [Cancelar] [Salvar]     |
+--------------------------------------------------------------+
~~~

**Comportamento:** tela destinada à manutenção cadastral autorizada à Secretaria. A edição de vínculos, os campos obrigatórios e a administração de responsáveis dependem de detalhamento institucional. Não permitir alteração de frequência, notas ou outros registros acadêmicos nesta tela.

## 5. Turmas e vínculos

~~~text
+--------------------------------------------------------------+
| TURMAS                                                       |
| Ano letivo: [________]  Buscar: [____________________]       |
|--------------------------------------------------------------|
| Código | Nome da turma | Etapa/série | Turno | Situação     |
| T01    | 1º Ano A      | Fundamental | Manhã | Ativa        |
|--------------------------------------------------------------|
| [Consultar turma]                                             |
+--------------------------------------------------------------+
~~~

**Comportamento:** exibir turmas conforme escola e vínculos autorizados. O professor visualiza somente turmas vinculadas a ele. As permissões para criar, editar, inativar turmas e administrar matrículas ainda não foram definidas na matriz; por isso, esses comandos não são presumidos no wireframe.

## 6. Frequência — lançamento inicial

~~~text
+--------------------------------------------------------------+
| LANÇAR FREQUÊNCIA                                            |
| Turma: [Selecione turma vinculada] Data: [__/__/____]        |
|--------------------------------------------------------------|
| Matrícula | Aluno             | Presente | Ausente            |
| 0001      | Aluno Exemplo     |   (•)    |   ( )              |
| 0002      | Aluna Exemplo     |   (•)    |   ( )              |
|--------------------------------------------------------------|
|                                      [Salvar lançamento]     |
+--------------------------------------------------------------+
~~~

**Permissões e comportamento:**

- Professor: realiza o lançamento inicial somente nas próprias turmas. Todos os alunos aparecem como presentes por padrão; o professor marca os ausentes e salva.
- Coordenação: não realiza lançamento inicial.
- Direção: não lança nem altera frequência.
- Secretaria: consulta, sem alterar.
- Gestão da Secretaria de Educação: somente indicadores agregados e anonimizados; não acessa a chamada individual.

## 7. Frequência — consulta e correção

~~~text
+--------------------------------------------------------------+
| CONSULTAR / CORRIGIR FREQUÊNCIA                              |
| Turma: [________] Aluno: [________] Período: [________]      |
|--------------------------------------------------------------|
| Data       | Aluno          | Situação atual | Ação          |
| __/__/____ | Aluno Exemplo  | Ausente         | [Corrigir]    |
|--------------------------------------------------------------|
| Valor anterior: [Ausente]   Novo valor: [________]           |
| Motivo da correção: [________________________________]      |
|                                      [Salvar correção]       |
| Histórico: usuário, data/hora e valores                      |
+--------------------------------------------------------------+
~~~

**Permissões e comportamento:**

- Professor: consulta e corrige registros das próprias turmas.
- Coordenação: consulta todos os alunos da escola e corrige registros já lançados; não pode criar lançamento inicial.
- Secretaria: somente consulta.
- Direção: somente consulta nos limites dos relatórios e atribuições definidos; não altera.
- Gestão da Secretaria de Educação: somente dados agregados e anonimizados.
- Toda correção registra valor anterior, valor novo, usuário, data/hora e motivo em trilha de auditoria.

## 8. Justificativa de falta

~~~text
+--------------------------------------------------------------+
| REGISTRAR JUSTIFICATIVA                                      |
| Aluno: [________________________]                            |
| Data inicial: [__/__/____]                                   |
| Duração (dias corridos): [___]                               |
| Descrição: [___________________________________________]     |
| Período calculado: [__/__/____] até [__/__/____]             |
|--------------------------------------------------------------|
| Datas letivas abrangidas: [lista de datas]                   |
| Datas sem aula no intervalo: [lista informativa]             |
|                                      [Salvar justificativa]  |
+--------------------------------------------------------------+
~~~

**Comportamento:** a justificativa exige marcação de falta justificada e descrição. A duração inclui sábados, domingos, feriados e dias sem aula; a aplicação alcança somente datas letivas com frequência prevista. Não criar registros de frequência em dias sem aula.

**Permissões:** professor pode registrar/associar justificativa no lançamento ou correção permitido em suas turmas; coordenação pode fazê-lo no contexto de correção. Direção não altera frequência e Secretaria apenas consulta.

## 9. Alertas de frequência e busca ativa

~~~text
+--------------------------------------------------------------+
| ALERTAS DE FREQUÊNCIA                                        |
| Período: [________] Turma: [Todas____] Situação: [Abertos__] |
|--------------------------------------------------------------|
| Aluno          | Turma | Faltas consecutivas | Situação      |
| Aluno Exemplo  | 1º A  | 3                   | Em aberto     |
|--------------------------------------------------------------|
| [Consultar histórico] [Registrar busca ativa]               |
+--------------------------------------------------------------+
~~~

**Comportamento:** o alerta aparece ao atingir três faltas consecutivas. A coordenação visualiza os alunos da escola e registra/acompanhada as ações de busca ativa. Os demais perfis recebem somente indicadores previstos na matriz.

## 10. Comunicados e confirmação de leitura

~~~text
+--------------------------------------------------------------+
| COMUNICADOS                              [ + Novo comunicado]|
|--------------------------------------------------------------|
| Título             | Público-alvo    | Publicação | Situação |
| Reunião de pais    | Turmas selecion.| ...        | Publicado|
|--------------------------------------------------------------|
| [Visualizar] [Consultar confirmações, se autorizado]        |
+--------------------------------------------------------------+
~~~

**Publicação:** professor, coordenação e direção podem publicar comunicados. O autor seleciona escola, turma ou aluno, respeitando seu escopo e sua permissão. Secretaria e Gestão da Secretaria de Educação não recebem permissão de publicação na matriz atual.

**Leitura:** o destinatário deve confirmar a leitura. A tela de confirmação/indicadores será exibida conforme a matriz: professor no escopo autorizado, coordenação no escopo da escola, direção para comunicados institucionais e indicadores de engajamento; Gestão da Secretaria de Educação somente indicadores agregados e anonimizados. A consulta individual pela Secretaria não está definida.

## 11. Chat com responsáveis

~~~text
+--------------------------------------------------------------+
| CHAT COM RESPONSÁVEIS                                        |
| Atendimento: 09h–10h e 14h–15h                               |
|--------------------------------------------------------------|
| Conversa                                                     |
| [Histórico de mensagens]                                     |
|                                                              |
| [Digite sua mensagem___________________________] [Enviar]    |
+--------------------------------------------------------------+
~~~

**Comportamento:** as janelas são fixas para toda a escola, não configuradas por professor. Durante os horários, o atendimento funciona normalmente. Fora deles, o sistema retorna automaticamente:

“Nosso horário de atendimento é das 09h às 10h e das 14h às 15h. Por favor, entre em contato durante esse período.”

Não foi definida fila de mensagens nem promessa de resposta posterior. A Secretaria só utilizará o chat conforme autorização institucional a detalhar; a Gestão da Secretaria de Educação não possui acesso ao chat na matriz.

## 12. Fórum de orientação de estudos

~~~text
+--------------------------------------------------------------+
| FÓRUM DE ESTUDOS                         [ + Nova discussão ] |
| Minhas discussões / Convites recebidos                       |
|--------------------------------------------------------------|
| Discussão: Orientação para avaliação                         |
| Criada por: Usuário responsável                              |
| Participantes convidados: [lista]                            |
|--------------------------------------------------------------|
| Mensagens e respostas                                        |
| [Escreva sua contribuição________________________] [Enviar]  |
|--------------------------------------------------------------|
| Moderação (somente criador): [Gerenciar discussão]           |
+--------------------------------------------------------------+
~~~

**Comportamento e permissões:**

- Participa somente quem foi convidado/chamado para a discussão.
- O criador da discussão, responsável por convidar os participantes, é o moderador.
- O moderador pode convidar participantes, revogar convites pendentes, remover participantes, ocultar/reativar mensagens inadequadas e encerrar/reabrir a discussão.
- Participantes comuns podem publicar mensagens e respostas, mas não administrar convites nem moderar.
- Todas as ações de moderação são auditadas com moderador, ação, data/hora e motivo quando aplicável.
- A matriz permite a participação dos cinco perfis quando convidados; os controles de moderação cabem ao criador da discussão.

## 13. Relatórios

~~~text
+--------------------------------------------------------------+
| RELATÓRIOS                                                   |
| Tipo: [Selecione relatório] Período: [________] [Consultar]  |
|--------------------------------------------------------------|
| Indicadores e resultados permitidos para o perfil            |
|                                                              |
| [Exportar, quando autorizado]                                |
+--------------------------------------------------------------+
~~~

**Conteúdo por perfil:**

- Professor: frequência, faltas justificadas, notas, conteúdos e ocorrências das próprias turmas.
- Coordenação: frequência, faltas consecutivas/injustificadas, alertas, justificativas e ações de busca ativa da escola.
- Direção: indicadores consolidados da escola e engajamento; sem alteração de frequência.
- Secretaria: dados cadastrais/matrícula, frequência consultável e boletins PDF.
- Gestão da Secretaria de Educação: indicadores agregados e anonimizados por escola/região/rede; exportações somente agregadas e anonimizadas.

## 14. Princípios de usabilidade e segurança

- Consistência de cabeçalho, menu, botões e nomenclaturas.
- Reconhecimento em vez de memorização: rótulos explícitos e filtros visíveis.
- Prevenção de erros: confirmação em ações sensíveis e validação de formulários.
- Feedback: informar sucesso, falha e estado de processamento.
- Acessibilidade: contraste adequado, navegação por teclado, rótulos associados aos campos e mensagens que não dependam apenas de cor.
- Simplicidade: apresentar somente ações pertinentes ao perfil autenticado.
- Autorização no servidor em cada rota, consulta e operação; ocultar um botão não substitui controle de acesso.
- Gestão da Secretaria de Educação nunca recebe linhas individuais nem identificadores pessoais nas telas, relatórios ou exportações.

## 15. Pontos para validação

1. Quem administra usuários, perfis e vínculos de professores às turmas?
2. Quais consultas individuais de alunos a direção poderá realizar além dos indicadores consolidados?
3. Quais perfis podem administrar turmas e matrículas?
4. Como será tratada a data efetiva de transferência e a chamada ainda não lançada?
5. A confirmação de leitura será individual por responsável quando houver mais de um responsável vinculado ao aluno?
6. Quais perfis poderão consultar confirmações individuais de leitura?
7. Quais etapas e estados serão utilizados no acompanhamento da busca ativa?
8. Quais técnicas e limiares mínimos serão adotados para anonimização e prevenção de reidentificação?
9. A frequência será diária ou por aula/horário e quais situações serão aceitas?
