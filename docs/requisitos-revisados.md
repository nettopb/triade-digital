# Requisitos revisados — Tríade Digital

## Escopo acadêmico do MVP
1. CRUD de turmas.
2. CRUD de estudantes (cadastro, listagem, edição via API e inativação).
3. Registro/atualização de frequência por estudante e data.
4. Alerta demonstrativo para 3 ou mais faltas consecutivas em registros lançados.
5. API REST documentada automaticamente via OpenAPI.

## Regras que precisam de validação com docente/cliente
- Regra original apresenta “3 faltas consecutivas” no processo e “mais de 3” na história US02. Para o MVP foi adotado provisoriamente **3 ou mais**, pois permite acionar busca ativa no terceiro dia; confirmar formalmente.
- Definir se consecutividade significa dias letivos, aulas, períodos ou registros de chamada. O MVP considera os últimos registros de frequência ordenados por data.
- Definir tratamento de falta justificada, feriados, finais de semana, transferência e matrícula tardia.
- Definir se frequência pode ser alterada e por quem, prazo de retificação e justificativa obrigatória.
- Definir papéis e permissões: Secretaria, Direção, Coordenação, Professor, Responsável e estudante.
- Definir se “confirmação de leitura” exige apenas abertura ou ação explícita de confirmação.
- Definir canais de comunicação e consentimentos/configurações de notificação.

## Requisitos não funcionais
- Interface responsiva e acessível por teclado.
- Validação de dados no servidor.
- Proteção de dados pessoais, controle de acesso e trilha de auditoria antes de qualquer piloto real.
- Backups, monitoramento, logs e procedimento de restauração para deploy.
- Não utilizar dados reais de crianças/adolescentes nesta versão acadêmica.

## Critérios de aceite iniciais
- Não permitir matrícula duplicada.
- Não permitir turma inexistente ao cadastrar estudante.
- Permitir registrar e atualizar frequência para a mesma data.
- Gerar alerta ao atingir 3 faltas consecutivas segundo a regra provisória.
- Expor operações e modelos na documentação `/docs`.
- Interface utilizável em largura móvel e desktop.
