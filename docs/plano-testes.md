# Plano de testes inicial

| ID | Cenário | Resultado esperado |
|---|---|---|
| CT-01 | Criar estudante com matrícula inédita | HTTP 201 e registro listado |
| CT-02 | Repetir matrícula | HTTP 409 |
| CT-03 | Cadastrar estudante com turma inexistente | HTTP 404 |
| CT-04 | Criar turma com nome repetido | HTTP 409 |
| CT-05 | Registrar frequência | HTTP 201 |
| CT-06 | Registrar novamente mesma data/estudante | Atualiza registro, sem duplicar |
| CT-07 | Três faltas consecutivas | Estudante aparece no alerta |
| CT-08 | Presença entre faltas | Interrompe sequência |
| CT-09 | Inativar estudante | Não aparece na listagem ativa |
| CT-10 | Abrir `/docs` | Swagger UI disponível |

## Evidências pendentes
Executar os testes no ambiente-alvo e anexar resultados reais. Este documento é um plano, não um relatório de testes executados.
