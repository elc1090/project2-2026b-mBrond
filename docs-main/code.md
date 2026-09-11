# Documentação de Código - Hubis Vitrine

Este documento descreve a arquitetura, padrões e fluxos de dados do sistema.

## Arquitetura do Backend

O backend segue uma estrutura simples baseada em Flask, organizada em torno de:
- `app.py`: Centraliza as rotas da API, lógica de autenticação e middlewares.
- `models.py`: Define o esquema do banco de dados usando SQLAlchemy.
- `validators.py`: Funções auxiliares para validação de dados (email, telefone, base64 images).
- `init_db.py` / `seed_data.py`: Gerenciamento do estado inicial do banco de dados.

### Padrão de Autenticação
- Utiliza JWT para sessões.
- O token é gerado no login e enviado no header `Authorization: Bearer <token>`.
- Middlewares internos `_require_authenticated()` e `_require_admin()` controlam o acesso.

### Persistência de Imagens
- Imagens são recebidas via Base64.
- Processadas para redimensionamento (máx 1080px) e compressão usando a biblioteca Pillow.
- Armazenadas no diretório `./uploads` e servidas estaticamente.

## Arquitetura do Frontend

O frontend utiliza React com Vite e TypeScript, seguindo uma estrutura modular em `front/src/app/`.

### Estrutura de Pastas
- `api/`: Centraliza chamadas ao backend usando Axios. Inclui interceptores para anexar o token JWT e tratar erros 401.
- `components/`: Componentes reutilizáveis.
    - `ui/`: Componentes base (shadcn/Radix).
- `contexts/`: Provedores de estado global (ex: AuthContext).
- `pages/`: Componentes de página que mapeiam para rotas.
- `utils/`: Lógicas auxiliares (formatação, cálculos de preço, exportação PDF).

### Fluxo de Dados
1. O usuário interage com a UI.
2. Componentes de página chamam funções em `api/index.ts`.
3. O interceptor de Axios anexa o token do `localStorage`.
4. Os dados retornados são tipados via `types.ts`.

### Estilização
- **Tailwind CSS:** Para layout e estilos atômicos.
- **Theme.css:** Variáveis globais de cores e fontes.

## Convenções de Código
- **Tipagem:** TypeScript rigoroso no frontend.
- **Snake Case:** No backend (padrão Python).
- **Camel Case:** No frontend (padrão JS/TS). No entanto, note que as respostas da API podem seguir o padrão do banco (muitas vezes snake_case), então o frontend mapeia ou utiliza conforme disponível em `types.ts`.
