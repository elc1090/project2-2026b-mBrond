# Hubis Vitrine - Documentação

Bem-vindo à documentação do Hubis Vitrine! Este diretório contém todas as referências técnicas do projeto.

## Índice

- [Visão Geral (general.md)](./general.md): Visão geral do projeto, stack tecnológica e instruções para rodar o ambiente.
- [Código e Arquitetura (code.md)](./code.md): Explicações sobre a arquitetura do Backend e Frontend, fluxos de dados e convenções.
- [Contratos da API (contracts.md)](./contracts.md): Documentação detalhada dos endpoints, estruturas JSON de requisição/resposta e regras de autenticação (Spec Driven Development).
- [Estrutura do Banco de Dados (database.json)](./database.json): Arquivo JSON contendo a estrutura detalhada de tabelas e colunas, útil para análises automatizadas e IA.
- [Especificação OpenAPI (openapi.json)](./openapi.json): Especificação padrão da API (OpenAPI 3.1). Pode ser regerada executando `python generate_openapi.py`.
- [Script Gerador (generate_openapi.py)](./generate_openapi.py): Script FastAPI que gera o schema `openapi.json` a partir dos modelos da API.

---

*Esta documentação deve ser mantida atualizada conforme novas features ou mudanças na arquitetura forem introduzidas.*
