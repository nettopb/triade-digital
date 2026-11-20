# Requisitos do sistema — Tríade Digital

## 1. Objetivo e contexto

Desenvolver o portal web corporativo da plataforma Tríade Digital para centralizar a gestão acadêmica, o diário de classe e a comunicação entre escola, responsáveis e estudantes. O sistema deve apoiar a identificação precoce de risco de evasão, a rastreabilidade dos comunicados e a gestão de informações escolares.

A descrição-base do projeto apresenta cinco funcionalidades centrais: diário de classe web; mural de avisos segmentados com confirmação de leitura; chat web com horário configurável; painel de monitoramento da evasão; e fórum de orientação de estudos.

## 2. Perfis de usuário

O sistema terá cinco perfis, cujas regras de acesso estão detalhadas em [Matriz de permissões](matriz-permissoes.md):

1. Professor.
2. Coordenação pedagógica.
3. Direção.
4. Secretaria escolar.
5. Gestão da Secretaria de Educação.

O controle de acesso deverá ser aplicado no servidor, em cada operação e consulta. Não basta ocultar botões na interface.

## 3. Requisitos funcionais

### 3.1. Acesso e estrutura escolar

- **RF01 — Autenticação:** permitir que usuários autorizados entrem no sistema.
- **RF02 — Perfis e permissões:** controlar as operações e os dados acessíveis conforme o perfil e o escopo escolar/turma.
- **RF03 — Cadastro de alunos:** cadastrar, consultar e atualizar dados cadastrais dos alunos, respeitando as permissões.
- **RF04 — Cadastro de responsáveis:** registrar responsáveis e seus contatos oficiais, vinculando-os aos alunos.
- **RF05 — Cadastro de turmas:** cadastrar e consultar turmas e suas informações.
- **RF06 — Matrícula e vínculo com turma:** associar alunos às turmas e registrar transferências entre turmas.
- **RF07 — Histórico escolar de turma e frequência:** ao transferir um aluno, preservar o histórico do aluno e os registros de presença/falta já lançados nos dias anteriores do ano letivo. A transferência não deverá apagar nem deslocar registros históricos.

### 3.2. Diário de classe e frequência

- **RF08 — Lançamento de frequência:** permitir ao professor registrar a frequência das suas turmas. A chamada deverá apresentar todos os alunos como “Presente” por padrão; o professor desmarca os ausentes e salva. A interação deverá ser otimizada para lançamento rápido.
- **RF09 — Consulta de frequência:** permitir a consulta dos registros de frequência conforme a matriz de permissões.
- **RF10 — Correção de frequência:** permitir que professor e coordenação corrijam uma frequência já lançada. A operação deverá preservar informação suficiente para auditoria (registro anterior, novo valor, responsável e data/hora da alteração).
- **RF11 — Falta justificada:** permitir marcar uma falta como justificada por meio de uma flag e preencher um campo descritivo (por exemplo, “atestado por 5 dias”).
- **RF12 — Aplicação por período da justificativa:** quando a justificativa abranger vários dias, o sistema deverá repetir a operação de justificativa nos dias seguintes informados, gerando os registros correspondentes para o período indicado. A regra de calendário escolar e o tratamento de dias sem aula deverão ser definidos antes da implementação.
- **RF13 — Alerta de frequência:** identificar e apresentar alerta quando o aluno atingir **3 faltas consecutivas**. A coordenação deverá visualizar o aluno, o período/duração da ausência e o acesso à ação de busca ativa/notificação aos responsáveis.
- **RF14 — Notas, conteúdos e ocorrências:** disponibilizar no diário de classe o registro de notas, conteúdos ministrados e ocorrências, respeitando o acesso do professor às próprias turmas e as permissões institucionais aplicáveis.

### 3.3. Comunicados e comunicação

- **RF15 — Publicação de comunicados:** permitir que professor, coordenação e direção publiquem comunicados.
- **RF16 — Segmentação de comunicados:** permitir direcionar comunicados à escola, a uma turma ou a um aluno, conforme a finalidade e a permissão do autor.
- **RF17 — Confirmação de leitura obrigatória:** exigir confirmação de leitura dos comunicados pelos destinatários e disponibilizar o estado/indicadores de leitura aos perfis autorizados.
- **RF18 — Chat com responsáveis:** disponibilizar chat web para atendimento aos responsáveis, respeitando os horários definidos para atendimento.
- **RF19 — Horários de atendimento:** configurar as janelas de atendimento de **09h às 10h** e **14h às 15h**. A descrição-base prevê horário configurável; a possibilidade de horários diferentes por professor ou por escola deverá ser detalhada na configuração técnica.

### 3.4. Monitoramento e relatórios

- **RF20 — Painel de evasão:** apresentar alertas de alunos com 3 faltas consecutivas, com destaque visual, duração da ausência e ação para iniciar busca ativa.
- **RF21 — Histórico de comunicados:** disponibilizar histórico de comunicados enviados às famílias, conforme permissão.
- **RF22 — Busca ativa:** apoiar o registro/acompanhamento das ações de busca ativa realizadas pela coordenação.
- **RF23 — Relatórios por perfil:** apresentar relatórios com os dados mais relevantes para cada perfil, respeitando a matriz de permissões. A seleção exata de indicadores e campos ainda será especificada.
- **RF24 — Relatórios de engajamento:** permitir acompanhar indicadores de participação e confirmação de leitura dos comunicados/reuniões, conforme acesso da direção e demais perfis autorizados.
- **RF25 — Dados agregados e anonimizados:** disponibilizar à Gestão da Secretaria de Educação somente dados agregados e anonimizados, inclusive em relatórios e exportações.
- **RF26 — Exportação de dados:** permitir exportação de dados educacionais agregados e anonimizados para análise e acompanhamento de políticas públicas, sem exposição de dados pessoais identificáveis.

### 3.5. Orientação de estudos

- **RF27 — Fórum de orientação de estudos:** disponibilizar espaço web de orientação de estudos para apoio aos alunos. Regras de participação, moderação e perfis autorizados ainda deverão ser detalhadas.

### 3.6. Documentos escolares

- **RF28 — Boletim em PDF:** permitir emissão/compilação de boletins escolares em PDF, respeitando as permissões de acesso.

## 4. Regras de negócio definidas

- **RN01:** o alerta de frequência é gerado ao atingir 3 faltas consecutivas.
- **RN02:** o professor acessa somente suas próprias turmas.
- **RN03:** a coordenação acessa todos os alunos da sua escola.
- **RN04:** a direção não pode alterar registros de frequência.
- **RN05:** a secretaria escolar pode alterar somente dados cadastrais.
- **RN06:** a Gestão da Secretaria de Educação acessa dados agregados e anonimizados, sem acesso a registros pessoais identificáveis.
- **RN07:** somente professor e coordenação podem corrigir frequência já lançada.
- **RN08:** falta justificada exige uma marcação específica (flag) e uma descrição.
- **RN09:** justificativa com duração em dias deve ser aplicada aos dias seguintes abrangidos pelo período informado.
- **RN10:** transferência entre turmas deve preservar o histórico do aluno e os registros de presença/falta anteriores do ano letivo.
- **RN11:** professor, coordenação e direção podem publicar comunicados.
- **RN12:** confirmação de leitura de comunicado é obrigatória.
- **RN13:** as janelas de atendimento do chat são 09h–10h e 14h–15h.

## 5. Requisitos não funcionais e conformidade

- **RNF01:** utilizar PHP 8.2 ou superior e MySQL.
- **RNF02:** utilizar PDO e consultas parametrizadas.
- **RNF03:** aplicar autenticação e autorização no servidor, negando por padrão operações não autorizadas.
- **RNF04:** proteger formulários contra CSRF e validar dados no servidor.
- **RNF05:** armazenar senhas com mecanismo seguro de hash disponibilizado pelo PHP.
- **RNF06:** não expor erros técnicos, credenciais ou informações sensíveis ao usuário final.
- **RNF07:** manter dados fictícios no ambiente acadêmico de desenvolvimento.
- **RNF08:** registrar trilha de auditoria para alterações de dados acadêmicos sensíveis, especialmente frequência, justificativas, matrículas e permissões.
- **RNF09:** aplicar princípios de finalidade, necessidade, segurança, prevenção e controle de acesso no tratamento de dados pessoais.
- **RNF10:** projetar o sistema considerando a Lei Geral de Proteção de Dados Pessoais (LGPD — Lei nº 13.709/2018) e a Política Nacional de Educação Digital (PNED — Lei nº 14.533/2023).

## 6. Critérios de aceite de referência

- **CA01 — Chamada rápida:** ao abrir a chamada, todos os alunos da turma aparecem como presentes; o professor desmarca apenas os ausentes e salva.
- **CA02 — Alerta:** ao completar 3 faltas consecutivas, o aluno aparece no painel da coordenação com destaque, duração da ausência e ação de busca ativa.
- **CA03 — Escopo do professor:** um professor não consegue consultar alunos ou frequências de turmas que não estejam vinculadas a ele.
- **CA04 — Correção:** somente professor e coordenação conseguem alterar uma frequência já lançada; a alteração fica auditável.
- **CA05 — Direção:** o perfil direção não consegue criar, editar ou excluir registros de frequência.
- **CA06 — Secretaria:** o perfil secretaria consegue alterar dados cadastrais, mas não registros acadêmicos de frequência.
- **CA07 — Gestão da Secretaria:** telas, relatórios e exportações desse perfil não expõem dados pessoais identificáveis.
- **CA08 — Justificativa:** ao informar justificativa com período de cinco dias, o sistema aplica a justificativa aos dias letivos abrangidos, conforme calendário escolar.
- **CA09 — Transferência:** após transferir o aluno, os registros anteriores permanecem vinculados ao histórico do aluno e à turma/período em que foram lançados.
- **CA10 — Comunicados:** professor, coordenação e direção conseguem publicar; o destinatário precisa confirmar leitura.
- **CA11 — Chat:** o atendimento respeita as janelas 09h–10h e 14h–15h.

## 7. Pendências de detalhamento

As decisões abaixo não impedem o registro dos requisitos, mas precisam ser especificadas antes da implementação das respectivas funcionalidades:

1. **Calendário escolar e justificativas:** definir como tratar finais de semana, feriados, recessos, dias sem aula, justificativas retroativas e sobreposição com frequência já lançada.
2. **Transferência:** definir a data efetiva da mudança, a turma de origem/destino e como tratar chamadas ainda não lançadas.
3. **Chat:** confirmar se as janelas são globais para a escola ou se cada professor poderá configurar disponibilidade dentro delas; definir mensagens fora do horário.
4. **Relatórios:** selecionar indicadores e campos por perfil; “os mais relevantes” é a orientação inicial, ainda sem catálogo fechado.
5. **Fórum:** definir participantes, moderação, publicação e denúncia de conteúdo.
6. **Comunicados:** definir se a confirmação de leitura será exigida de cada responsável individualmente e como tratar responsáveis múltiplos.
7. **Busca ativa:** detalhar etapas, responsáveis, status e eventual integração com Conselho Tutelar/assistência social.
8. **Dados anonimizados:** definir técnica de anonimização, limiar mínimo de agregação e prevenção de reidentificação em grupos pequenos.
9. **Administração de usuários:** definir quem cria, bloqueia e atribui perfis e vínculos institucionais.

## 8. Priorização e escopo

A descrição do projeto apresenta as funcionalidades listadas neste documento como parte da solução pretendida. A divisão entre MVP, entregas posteriores e itens demonstrativos deverá ser feita no backlog, considerando os marcos acadêmicos e a capacidade de desenvolvimento individual. Não se deve excluir uma funcionalidade da visão do produto apenas por ela não entrar na primeira entrega.

## 9. Referências legais

- [Lei nº 14.533/2023 — Política Nacional de Educação Digital (PNED)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14533.htm).
- [Lei nº 13.709/2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm).

Este documento consolida decisões de negócio informadas pelo responsável pelo projeto e requisitos identificados na descrição-base. Os itens indicados como pendentes permanecem abertos e não devem ser tratados como decisões já tomadas.
