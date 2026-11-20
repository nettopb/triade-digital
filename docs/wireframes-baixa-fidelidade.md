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

**Comportamento:** registrar frequência por turma e data; impedir duplicidade para o mesmo aluno/turma/data, conforme regra a definir; registrar usuário responsável pelo lançamento e data/hora da operação.

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

**Pendente de validação:** quantidade de faltas consecutivas que gera alerta, tratamento de falta justificada, janela de cálculo, destinatários e procedimento de acompanhamento.

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

## 9. Princípios de usabilidade considerados

- Consistência de cabeçalho, menu lateral, botões e nomenclaturas.
- Reconhecimento em vez de memorização: rótulos explícitos e filtros visíveis.
- Prevenção de erros: confirmação em ações sensíveis e validação de formulários.
- Feedback: informar sucesso, falha e estado de processamento.
- Acessibilidade: contraste adequado, navegação por teclado, rótulos associados aos campos e mensagens que não dependam apenas de cor.
- Simplicidade: apresentar apenas ações pertinentes ao perfil do usuário.

## 10. Pontos para validação

1. Quais perfis podem cadastrar, editar e inativar alunos?
2. Quem pode lançar, corrigir e consultar frequência?
3. Qual regra institucional define alerta de faltas consecutivas?
4. Quem recebe e acompanha alertas?
5. Comunicados exigem aprovação? É necessário registrar leitura?
6. Quais indicadores são úteis para cada perfil?

