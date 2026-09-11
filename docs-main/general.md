# Documentação Geral - Hubis Vitrine

Este documento fornece uma visão geral do projeto Hubis Vitrine, uma plataforma de vitrine virtual para empreendimentos e produtos.

## Visão Geral
O Hubis Vitrine permite que gestores (Admin) e proprietários de negócios (Owner) gerenciem seus catálogos de produtos e informações institucionais. O sistema é composto por um frontend em React e um backend em Python (Flask).

## Stack Tecnológica

### Backend
- **Linguagem:** Python 3.x
- **Framework:** Flask
- **ORM:** SQLAlchemy
- **Banco de Dados:** SQLite (persistido via Docker volume)
- **Autenticação:** JWT (PyJWT)
- **Processamento de Imagem:** Pillow

### Frontend
- **Linguagem:** TypeScript
- **Framework:** React 18 (Vite)
- **Componentes UI:** Tailwind CSS, Radix UI, MUI Icons
- **Roteamento:** React Router (v6/v7)
- **Cliente HTTP:** Axios

## Configuração do Ambiente

### Pré-requisitos
- Docker e Docker Compose
- Node.js (opcional para desenvolvimento local do front)
- Python (opcional para desenvolvimento local do back)

### Execução via Docker (Recomendado)
```bash
docker compose up --build
```
A API estará disponível na porta `5174` e o frontend na porta padrão do Vite (geralmente `5173`).

### Execução Local (Backend)
1. Navegue até o diretório do backend: `cd back`
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - Linux/macOS: `source venv/bin/activate`
4. Instale dependências: `pip install -r requirements.txt`
5. Inicialize o banco: `python init_db.py`
6. Execute: `python app.py 5174 True` (Os parâmetros são [PORTA] e [DEBUG])

### Execução Local (Frontend)
1. Em outro terminal, navegue até o diretório do frontend: `cd front`
2. Instale dependências: `npm install`
3. Execute o servidor de desenvolvimento: `npm run dev`

## Estrutura de Diretórios
- `back/`: Código fonte do servidor Flask, modelos de dados e scripts de banco.
- `front/`: Código fonte da aplicação React, componentes e estilos.
- `docs/`: Documentação do projeto (este diretório).
