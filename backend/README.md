# Backend API

## Overview
Este é o backend do projeto, desenvolvido em Python utilizando o framework Flask. A aplicação fornece uma API RESTful para gerenciar usuários, categorias, empresas e produtos, além de suportar manipulação de imagens e autenticação segura com JWT. O banco de dados utilizado é o SQLite, manipulado através de SQLAlchemy.

## Instruções de execução

1. **Crie e ative um ambiente virtual (recomendado):**
   ```bash
   python -m venv venv
   
   # No Windows (PowerShell/CMD):
   venv\Scripts\activate
   
   # No Linux/macOS:
   source venv/bin/activate
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Inicialize o banco de dados:**
   Para criar as tabelas necessárias:
   ```bash
   python init_db.py
   ```

4. **Execute a aplicação:**
   ```bash
   python app.py [PORTA] [DEGUG]
   ```
   A flag [DEBUG] deve ser `True` ou `False`, e determina o debug da API. Deve ser usado True apenas em casos de teste.
   A API estará rodando em `http://0.0.0.0:[PORTA]`.

## Estrutura das pastas

### Principais:

- `app.py`: Ponto de entrada da aplicação Flask e definição das rotas da API.
- `init_db.py`: Script para criar e inicializar as tabelas no banco de dados.

### Auxiliares:

- `models.py`: Modelos de banco de dados do SQLAlchemy (`User`, `Enterprise`, `Product`, `Category`).
- `requirements.txt`: Lista de dependências do projeto.
- `seed_data.py`: Script para popular o banco de dados com usuários, empresas e produtos fictícios.
- `validators.py`: Funções auxiliares para validação de formato (e-mail, telefone, imagens em base64, etc.).
