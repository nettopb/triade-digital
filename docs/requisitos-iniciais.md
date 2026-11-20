# Requisitos do sistema — Tríade Digital

## 1. Objetivo e contexto

Desenvolver o portal web corporativo da plataforma Tríade Digital para centralizar a gestão acadêmica, o diário de classe e a comunicação entre escola, responsáveis e estudantes. O sistema deve apoiar a identificação precoce de risco de evasão, a rastreabilidade dos comunicados e a gestão de informações escolares.

A solução contempla diário de classe web; mural de avisos segmentados com confirmação de leitura; chat web; painel de monitoramento da evasão; e fórum de orientação de estudos.

## 2. Perfis de usuário

O sistema terá cinco perfis, com regras detalhadas em [Matriz de permissões](matriz-permissoes.md):

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

- **RF08 — Lançamento de frequência:** permitir ao professor registrar a frequência das suas turmas. A chamada deverá apresentar todos os alunos como “Presente” por padrão; o professor desmarca os ausentes e salva.
- **RF09 — Consulta de frequência:** permitir consulta conforme a matriz de permissões. A secretaria escolar pode consultar frequência, sem autorização para alterá-la.
- **RF10 — Correção de frequência:** permitir que professor e coordenação corrijam uma frequência já lançada. A coordenação pode corrigir, mas não realizar o lançamento inicial de frequência. A operação deverá preservar informação para auditoria (registro anterior, novo valor, responsável e data/hora).
- **RF11 — Falta justificada:** permitir marcar uma falta como justificada por meio de uma flag e preencher um campo descritivo (por exemplo, “atestado por 5 dias”).
- **RF12 — Aplicação por período da justificativa:** o período de justificativa será contado em dias corridos, incluindo finais de semana, feriados e dias sem aula. Entretanto, o sistema só deverá gerar/associar registros de frequência nos dias em que houver atividade escolar e frequência prevista. Nos dias sem aula não haverá lançamento de frequência. O usuário informará a data inicial, a duração em dias corridos e a descrição da justificativa; o sistema aplicará a justificativa aos dias letivos abrangidos.
- **RF13 — Alerta de frequência:** identificar e apresentar alerta quando o aluno atingir **3 faltas consecutivas**. A coordenação deverá visualizar o aluno, a duração da ausência e a ação de busca ativa/notificação aos responsáveis.
- **RF14 — Notas, conteúdos e ocorrências:** disponibilizar no diário de classe o registro de notas, conteúdos ministrados e ocorrências, respeitando o acesso do professor às próprias turmas e as permissões institucionais.

### 3.3. Comunicados e comunicação

- **RF15 — Publicação de comunicados:** permitir que professor, coordenação e direção publiquem comunicados.
- **RF16 — Segmentação de comunicados:** permitir direcionar comunicados à escola, a uma turma ou a um aluno, conforme a finalidade e a permissão do autor.
- **RF17 — Confirmação de leitura obrigatória:** exigir confirmação de leitura dos comunicados pelos destinatários e disponibilizar estado/indicadores de leitura aos perfis autorizados.
- **RF18 — Chat com responsáveis:** disponibilizar chat web para atendimento aos responsáveis, respeitando os horários fixos definidos para toda a escola.
- **RF19 — Horários de atendimento:** as janelas de atendimento serão **09h às 10h** e **14h às 15h**, iguais para toda a escola. Não haverá configuração individual de horários por professor.

### 3.4. Monitoramento e relatórios

- **RF20 — Painel de evasão:** apresentar alertas de alunos com 3 faltas consecutivas, com destaque visual, duração da ausência e ação para iniciar busca ativa.
- **RF21 — Histórico de comunicados:** disponibilizar histórico de comunicados enviados às famílias, conforme permissão.
- **RF22 — Busca ativa:** apoiar o registro/acompanhamento das ações de busca ativa realizadas pela coordenação.
- **RF23 — Relatórios por perfil:** apresentar indicadores e campos usuais e relevantes para cada perfil, respeitando o escopo de acesso. A primeira versão deverá adotar o catálogo de referência da seção 6, sujeito a ajustes durante a validação.
- **RF24 — Relatórios de engajamento:** permitir acompanhar indicadores de participação e confirmação de leitura dos comunicados/reuniões, conforme acesso da direção e demais perfis autorizados.
- **RF25 — Dados agregados e anonimizados:** disponibilizar à Gestão da Secretaria de Educação somente dados agregados e anonimizados, inclusive em relatórios e exportações.
- **RF26 — Exportação de dados:** permitir exportação de dados educacionais agregados e anonimizados para análise e acompanhamento de políticas públicas, sem exposição de dados pessoais identificáveis.

### 3.5. Orientação de estudos

- **RF27 — Fórum de orientação de estudos:** disponibilizar fórum em que participa quem for chamado/convidado para a discussão. A pessoa que criar/chamar os participantes será responsável pela moderação daquele espaço/discussão.

### 3.6. Documentos escolares

- **RF28 — Boletim em PDF:** permitir emissão/compilação de boletins escolares em PDF. A secretaria escolar pode emitir boletins, sem que isso lhe conceda permissão para alterar notas ou outros registros acadêmicos.

## 4. Regras de negócio definidas

- **RN01:** o alerta de frequência é gerado ao atingir 3 faltas consecutivas.
- **RN02:** o professor acessa somente suas próprias turmas.
- **RN03:** a coordenação acessa todos os alunos da sua escola.
- **RN04:** a direção não pode alterar registros de frequência.
- **RN05:** a secretaria escolar pode alterar somente dados cadastrais; pode consultar frequência e emitir boletins em PDF, mas não pode alterar frequência, notas ou outros registros acadêmicos.
- **RN06:** a Gestão da Secretaria de Educação acessa dados agregados e anonimizados, sem acesso a registros pessoais identificáveis.
- **RN07:** somente professor e coordenação podem corrigir frequência já lançada; a coordenação não realiza lançamento inicial.
- **RN08:** falta justificada exige uma flag e uma descrição.
- **RN09:** a duração da justificativa é contada em dias corridos. A justificativa alcança os dias letivos dentro do intervalo, mas não cria registros de frequência em dias sem aula.
- **RN10:** transferência entre turmas deve preservar o histórico do aluno e os registros de presença/falta anteriores do ano letivo.
- **RN11:** professor, coordenação e direção podem publicar comunicados.
- **RN12:** confirmação de leitura de comunicado é obrigatória.
- **RN13:** as janelas do chat são fixas para toda a escola: 09h–10h e 14h–15h.
- **RN14:** no fórum, participam somente as pessoas convidadas/chamadas; quem criou a discussão e convidou os participantes é seu moderador.

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

## 6. Catálogo inicial de relatórios por perfil

O responsável pelo projeto definiu que os relatórios deverão priorizar indicadores mais importantes e usuais. Para orientar a primeira versão, fica estabelecido o seguinte catálogo inicial:

| Perfil | Indicadores/campos de referência |
|---|---|
| Professor | Frequência por turma e período; lista de alunos presentes/ausentes; faltas justificadas; notas e desempenho por avaliação; conteúdos ministrados; ocorrências. Restrito às próprias turmas. |
| Coordenação | Frequência por aluno/turma/período; faltas consecutivas e injustificadas; alunos com alerta de risco; justificativas; histórico de comunicados; ações de busca ativa e seu status. Restrito à escola. |
| Direção | Indicadores consolidados da escola: frequência, ausências, evolução de desempenho, comunicados publicados, percentual de confirmação de leitura e participação/engajamento em reuniões. Sem alteração de frequência. |
| Secretaria escolar | Dados cadastrais e de matrícula; situação de matrícula/turma; frequência consultável; emissão de boletins em PDF. Alterações limitadas aos dados cadastrais. |
| Gestão da Secretaria de Educação | Indicadores agregados e anonimizados por escola/região/rede: frequência, abandono/evasão, evolução temporal, desempenho agregado e engajamento das famílias. Exportações somente agregadas e anonimizadas. |

Este catálogo é uma proposta inicial de indicadores usuais para atender à orientação recebida; poderá ser refinado sem ampliar as permissões de cada perfil.

## 7. Critérios de aceite de referência

- **CA01 — Chamada rápida:** ao abrir a chamada, todos os alunos da turma aparecem como presentes; o professor desmarca apenas os ausentes e salva.
- **CA02 — Alerta:** ao completar 3 faltas consecutivas, o aluno aparece no painel da coordenação com destaque, duração da ausência e ação de busca ativa.
- **CA03 — Escopo do professor:** um professor não consegue consultar alunos ou frequências de turmas que não estejam vinculadas a ele.
- **CA04 — Correção:** somente professor e coordenação conseguem corrigir frequência já lançada; a coordenação não consegue realizar lançamento inicial; a alteração fica auditável.
- **CA05 — Direção:** o perfil direção não consegue criar, editar ou excluir registros de frequência.
- **CA06 — Secretaria:** o perfil secretaria consulta frequência e emite boletins PDF, mas só altera dados cadastrais.
- **CA07 — Gestão da Secretaria:** telas, relatórios e exportações desse perfil não expõem dados pessoais identificáveis.
- **CA08 — Justificativa:** ao informar atestado de cinco dias corridos, o sistema considera todo o intervalo de calendário, mas registra a justificativa de frequência somente nos dias letivos abrangidos.
- **CA09 — Transferência:** após transferir o aluno, os registros anteriores permanecem vinculados ao histórico do aluno e à turma/período em que foram lançados.
- **CA10 — Comunicados:** professor, coordenação e direção conseguem publicar; o destinatário precisa confirmar leitura.
- **CA11 — Chat:** o atendimento respeita as janelas fixas 09h–10h e 14h–15h para toda a escola.
- **CA12 — Fórum:** somente convidados participam da discussão; o autor/criador da discussão é seu moderador.

## 8. Pendências de detalhamento

1. **Transferência:** definir a data efetiva da mudança, turma de origem/destino e tratamento de chamadas ainda não lançadas.
2. **Chat:** definir o comportamento de mensagens enviadas fora das janelas (bloqueio, fila ou aviso de indisponibilidade).
3. **Fórum:** definir como são enviados convites, se o convidado pode compartilhar a discussão e se o moderador pode remover participantes/conteúdos.
4. **Comunicados:** definir se a confirmação de leitura será exigida de cada responsável individualmente e como tratar responsáveis múltiplos.
5. **Busca ativa:** detalhar etapas, responsáveis, status e eventual integração com Conselho Tutelar/assistência social.
6. **Dados anonimizados:** definir técnica de anonimização, limiar mínimo de agregação e prevenção de reidentificação em grupos pequenos.
7. **Administração de usuários:** definir quem cria, bloqueia e atribui perfis e vínculos institucionais.

## 9. Priorização e escopo

A descrição do projeto apresenta as funcionalidades listadas neste documento como parte da solução pretendida. A divisão entre MVP, entregas posteriores e itens demonstrativos deverá ser feita no backlog, considerando os marcos acadêmicos e a capacidade de desenvolvimento individual. Não se deve excluir uma funcionalidade da visão do produto apenas por ela não entrar na primeira entrega.

## 10. Referências legais

- [Lei nº 14.533/2023 — Política Nacional de Educação Digital (PNED)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14533.htm).
- [Lei nº 13.709/2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm).

Este documento consolida decisões de negócio informadas pelo responsável pelo projeto e requisitos identificados na descrição-base. Os itens indicados como pendentes permanecem abertos e não devem ser tratados como decisões já tomadas.
