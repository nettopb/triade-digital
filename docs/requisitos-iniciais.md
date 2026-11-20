# Requisitos iniciais — Tríade Digital

## Objetivo
Centralizar operações essenciais de acompanhamento escolar em uma aplicação web, oferecendo registros consistentes e consultas adequadas aos diferentes perfis autorizados.

## Perfis de usuário previstos
- Professor
- Coordenação
- Direção
- Secretaria escolar
- Gestão da Secretaria de Educação

As permissões específicas de cada perfil ainda serão detalhadas e validadas antes da implementação.

## Requisitos funcionais iniciais
- **RF01:** permitir autenticação de usuários.
- **RF02:** permitir gerenciamento de usuários e perfis por usuário autorizado.
- **RF03:** permitir cadastrar, consultar, editar e inativar estudantes.
- **RF04:** permitir cadastrar, consultar, editar e organizar turmas.
- **RF05:** permitir associar estudantes às turmas.
- **RF06:** permitir registrar frequência por estudante e data.
- **RF07:** identificar ocorrências de faltas consecutivas segundo regra a ser confirmada com a instituição.
- **RF08:** permitir registrar e consultar comunicados.
- **RF09:** apresentar indicadores e relatórios básicos conforme permissão.

## Requisitos não funcionais iniciais
- **RNF01:** utilizar PHP 8.2+ e MySQL.
- **RNF02:** utilizar PDO e consultas parametrizadas.
- **RNF03:** aplicar controle de acesso no servidor, por perfil e operação.
- **RNF04:** proteger formulários contra CSRF e validar dados no servidor.
- **RNF05:** armazenar senhas com algoritmo seguro de hash disponibilizado pelo PHP.
- **RNF06:** não expor erros técnicos ou credenciais ao usuário final.
- **RNF07:** manter dados fictícios no ambiente acadêmico de desenvolvimento.
- **RNF08:** considerar privacidade, minimização de dados, auditoria e segurança antes de qualquer uso de dados reais de menores.

## Fora do MVP
- Chat em tempo real.
- Notificações push.
- Integrações automáticas com sistemas externos.
- Fórum ou rede social escolar.

## Regras pendentes de validação
- Quantidade de faltas consecutivas que gera alerta e momento do disparo.
- Quem pode visualizar, registrar e corrigir frequência.
- Escopo de visualização dos dados por escola, turma e rede.
- Fluxo de publicação e destinatários dos comunicados.
- Política de retenção e correção de registros.

Este documento é uma linha de base inicial, sujeita à validação com a orientação acadêmica e representantes da realidade escolar.