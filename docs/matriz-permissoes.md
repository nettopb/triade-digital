# Matriz de permissões — Tríade Digital

Esta matriz consolida as regras informadas para os cinco perfis. O controle deverá ser aplicado no servidor e nas consultas aos dados.

## 1. Matriz resumida

| Operação / recurso | Professor | Coordenação | Direção | Secretaria | Gestão da Secretaria |
|---|---|---|---|---|---|
| Consultar alunos | Somente das próprias turmas | Todos os alunos da escola | Conforme relatórios e atribuições da direção; detalhar consultas individuais | Conforme necessidade escolar | Somente dados agregados/anonimizados |
| Consultar frequência | Próprias turmas | Todos os alunos da escola | Consulta conforme relatórios; sem alteração | Sim, consulta | Somente dados agregados/anonimizados |
| Lançar frequência inicial | Próprias turmas | Não | Não | Não | Não |
| Corrigir frequência lançada | Próprias turmas | Sim, todos os alunos da escola | Não | Não | Não |
| Registrar falta justificada | Próprias turmas, dentro do lançamento/correção permitido | Sim, por correção | Não | Não | Não |
| Alterar dados cadastrais | Não definido | Não definido | Não definido | Sim, somente dados cadastrais | Não |
| Gerenciar turmas/matrículas | Não definido | Não definido | Não definido | Não definido | Não |
| Publicar comunicados | Sim | Sim | Sim | Não | Não |
| Consultar confirmação de leitura | Comunicados publicados/escopo autorizado | Escopo da escola | Comunicados institucionais e indicadores de engajamento | Não definido | Somente indicadores agregados/anonimizados |
| Chat com responsáveis | Dentro dos horários fixos da escola | Conforme necessidade e autorização a detalhar | Conforme necessidade e autorização a detalhar | Não definido | Não |
| Painel de evasão/busca ativa | Não definido | Sim, escopo da escola | Indicadores consolidados, conforme relatório | Não | Somente indicadores agregados/anonimizados |
| Relatórios | Frequência, notas, conteúdos e ocorrências das próprias turmas | Frequência, faltas, alertas, justificativas e busca ativa da escola | Indicadores consolidados da escola e engajamento | Dados cadastrais, matrícula, frequência consultável e boletins | Indicadores agregados/anonimizados por escola/região/rede |
| Exportar dados | Não definido | Não definido | Não definido | Não definido | Sim, somente agregados/anonimizados |
| Fórum de estudos | Participa se convidado; modera se for quem criou/convidou | Participa se convidada; modera se for quem criou/convidou | Participa se convidada; modera se for quem criou/convidou | Participa se convidada; modera se for quem criou/convidou | Participa se convidada; modera se for quem criou/convidou |
| Emitir boletim PDF | Não definido | Não definido | Não definido | Sim | Não |

## 2. Regras obrigatórias já definidas

1. **Professor:** acessa somente suas próprias turmas e pode lançar/corrigir a frequência dessas turmas.
2. **Coordenação:** acessa todos os alunos da escola e pode corrigir frequência já lançada, mas não realiza o lançamento inicial.
3. **Direção:** não pode alterar registros de frequência; pode publicar comunicados.
4. **Secretaria:** pode consultar frequência e emitir boletins em PDF. Sua permissão de alteração é limitada aos dados cadastrais; não pode alterar frequência, notas ou outros registros acadêmicos.
5. **Gestão da Secretaria de Educação:** acessa exclusivamente dados agregados e anonimizados. A restrição vale para telas, filtros, relatórios, downloads e exportações.
6. **Correção de frequência:** permitida somente a professor e coordenação, respeitando o escopo de cada um.
7. **Publicação de comunicados:** permitida a professor, coordenação e direção.
8. **Confirmação de leitura:** obrigatória para os comunicados.
9. **Chat:** horários fixos para toda a escola, das 09h às 10h e das 14h às 15h.
10. **Fórum:** participa quem for convidado/chamado; quem criou a discussão e convidou os participantes é o moderador.

## 3. Limites e interpretações

- “Não definido” significa que a regra ainda precisa de decisão; não equivale a permissão concedida.
- Consultar frequência não concede permissão para alterar frequência.
- Emitir boletim PDF não concede à secretaria permissão para alterar notas ou outros registros acadêmicos.
- A coordenação tem permissão de correção, não de lançamento inicial de frequência.
- A direção pode publicar comunicados e acompanhar indicadores de engajamento, mas não altera frequência.
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
- Quais consultas individuais de alunos a direção poderá acessar além dos indicadores consolidados?
- Quem pode configurar/gerenciar comunicados institucionais e consultar confirmações de leitura em cada nível?
- Qual o comportamento do chat fora dos horários fixos (bloqueio, fila ou aviso)?
- Como será realizado o convite ao fórum e quais controles o moderador terá?
- Quais perfis podem administrar turmas e matrículas?
- Quem pode emitir relatórios/exportações não anonimizados nos perfis escolares, respeitando as permissões já definidas?
