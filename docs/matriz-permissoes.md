# Matriz de permissões — Tríade Digital

Esta matriz consolida as regras informadas para os cinco perfis do projeto. “Acesso” significa autorização no sistema, aplicada no servidor e também nas consultas aos dados.

## 1. Matriz resumida

| Operação / recurso | Professor | Coordenação | Direção | Secretaria | Gestão da Secretaria |
|---|---|---|---|---|---|
| Consultar alunos | Somente das próprias turmas | Todos os alunos da escola | A definir | Conforme necessidade cadastral; escopo exato a definir | Somente dados agregados/anonimizados |
| Consultar frequência | Somente das próprias turmas | Todos os alunos da escola | Consulta, sem alteração | Não definido; não presumir acesso acadêmico | Somente dados agregados/anonimizados |
| Lançar frequência | Próprias turmas | Não definido | Não | Não | Não |
| Corrigir frequência lançada | Próprias turmas | Todos os alunos da escola | Não | Não | Não |
| Registrar justificativa de falta | Próprias turmas | Todos os alunos da escola | Não | Não | Não |
| Alterar dados cadastrais | Não definido | Não definido | Não definido | Sim, somente dados cadastrais | Não |
| Gerenciar turmas/matrículas | Não definido | Não definido | Não definido | Não definido | Não |
| Publicar comunicados | Sim | Sim | Sim | Não | Não |
| Consultar confirmação de leitura | Comunicados publicados/escopo autorizado — detalhar | Escopo da escola — detalhar | Comunicados institucionais e indicadores de engajamento | Não definido | Somente indicadores agregados/anonimizados |
| Chat com responsáveis | Dentro do horário de atendimento | A definir | A definir | Não definido | Não |
| Painel de evasão/busca ativa | Não definido | Sim, escopo da escola | Não definido | Não | Somente indicadores agregados/anonimizados |
| Relatórios | Dados relevantes das próprias turmas | Dados relevantes da escola | Dados relevantes da escola | Dados cadastrais/operacionais autorizados | Dados agregados/anonimizados por região/rede |
| Exportar dados | Não definido | Não definido | Não definido | Não definido | Sim, somente agregados/anonimizados |
| Fórum de estudos | Participação/moderação a definir | A definir | A definir | Não definido | Não definido |
| Emitir boletim PDF | Não definido | Não definido | Não definido | Necessidade descrita na persona; confirmar autorização | Não |

## 2. Regras obrigatórias já definidas

1. **Professor:** seu escopo de dados é limitado às turmas vinculadas a ele.
2. **Coordenação:** seu escopo abrange todos os alunos da escola.
3. **Direção:** não pode alterar registros de frequência.
4. **Secretaria:** pode alterar somente dados cadastrais; não recebe permissão de alteração de frequência ou de outros registros acadêmicos.
5. **Gestão da Secretaria de Educação:** acessa exclusivamente dados agregados e anonimizados. A restrição vale para telas, filtros, relatórios, downloads e exportações.
6. **Correção de frequência:** permitida somente a professor e coordenação, respeitando o escopo de cada um.
7. **Publicação de comunicados:** permitida a professor, coordenação e direção.
8. **Confirmação de leitura:** obrigatória para os comunicados.

## 3. Interpretação e limites

- “Não definido” significa que a regra ainda precisa de decisão; não equivale a permissão concedida.
- A secretaria tem permissão de edição limitada a dados cadastrais. A descrição-base cita matrícula, responsáveis, telefones/e-mails oficiais e boletins PDF; a autorização para emissão de boletins precisa ser confirmada porque a decisão recebida limita a secretaria à alteração cadastral.
- A coordenação pode corrigir frequência e consultar todos os alunos da escola. A permissão de lançamento inicial de frequência pela coordenação não foi definida.
- A direção pode publicar comunicados e acompanhar engajamento, conforme a descrição-base, mas não altera frequência.
- A gestão da Secretaria de Educação não pode consultar linhas individuais ou identificadores pessoais, mesmo que tenha filtros ou exportação disponíveis.
- O acesso de cada professor às próprias turmas deve ser validado tanto nas telas quanto nas rotas/consultas diretas.

## 4. Controles técnicos recomendados

- Negar acesso por padrão e conceder somente operações explicitamente autorizadas.
- Validar perfil, escola e vínculo do professor com a turma em toda requisição no servidor.
- Registrar usuário, data/hora, valor anterior e valor novo nas correções de frequência.
- Separar consultas individuais de consultas agregadas; não basta ocultar colunas na interface para caracterizar anonimização.
- Testar tentativas de acesso cruzado entre turmas, escolas e perfis.
- Impedir que exportações contornem as mesmas restrições aplicadas aos painéis.

## 5. Decisões ainda necessárias

- Quem cadastra usuários, atribui perfis e vincula professores às turmas?
- A coordenação também pode lançar frequência inicial ou apenas corrigir?
- A secretaria pode consultar frequência ou somente dados cadastrais?
- A secretaria pode emitir boletins em PDF, conforme a persona, apesar da regra de edição limitada a dados cadastrais?
- Quais consultas e relatórios individuais a direção poderá acessar?
- Quais perfis podem participar, moderar e administrar o fórum?
- Quem configura os horários do chat e se os intervalos 09h–10h e 14h–15h são globais ou por professor?
