# ADR-001 — Arquitetura da aplicação

- **Status:** proposta inicial
- **Data:** 20/11/2026
- **Contexto:** o Projeto 10 requer uma plataforma web de acompanhamento escolar, desenvolvida individualmente e com escopo compatível com os marcos acadêmicos.
- **Decisão:** utilizar PHP 8.2+, MySQL, PDO e arquitetura MVC, com interface HTML, CSS, JavaScript e Bootstrap.
- **Organização:** separar responsabilidades em Models (dados e regras), Views (apresentação), Controllers (fluxo da aplicação) e camada de configuração/infraestrutura.
- **Ambiente local:** XAMPP.
- **Justificativa:** a stack permite desenvolvimento incremental, uso de tecnologias acessíveis no contexto acadêmico e implantação em hospedagens compatíveis com PHP/MySQL.
- **Consequências:** será necessário implementar roteamento, validação, tratamento de erros, autenticação, autorização e proteção contra CSRF. Segredos e credenciais não serão versionados.
- **Revisão:** esta decisão poderá ser atualizada caso os requisitos ou o ambiente de implantação exijam mudanças.