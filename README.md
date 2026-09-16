# Hubis - Vitrine Virtual

Projeto composto por:
- **Backend:** Python + Flask + SQLAlchemy + JWT + Gunicorn (`/backend`)
- **Frontend:** React + Vite + TailwindCSS (`/frontend`)

---

## Como Rodar Localmente

### 1. Backend
```bash
cd backend
python -m venv venv

# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
python init_db.py
python app.py
```
A API estará rodando em `http://localhost:5000`.

### 2. Frontend
Em outro terminal:
```bash
cd frontend
npm install
npm run dev
```
O Frontend estará rodando em `http://localhost:5173`.

---

## Como Fazer Deploy no Render

### Opção A: Deploy Automático via Blueprint (Mais Fácil)
1. Suba este repositório no seu GitHub.
2. Acesse o [Dashboard do Render](https://dashboard.render.com).
3. Clique em **New +** e selecione **Blueprint**.
4. Conecte o repositório do GitHub. O Render lerá o arquivo `render.yaml` e criará automaticamente:
   - O serviço **hubis-backend** (Web Service).
   - O serviço **hubis-frontend** (Static Site com redirect de SPA configurado).
5. Após a criação:
   - Copie a URL do seu backend gerada pelo Render (ex: `https://hubis-backend.onrender.com`).
   - No serviço do frontend no Render, vá em **Environment** e adicione a variável:
     - `VITE_API_URL` = `https://hubis-backend.onrender.com` (sem barra no final).
   - Clique em **Manual Deploy -> Deploy latest commit** no frontend.

---

### Opção B: Deploy Manual no Render

#### 1. Criar o Backend (Web Service)
- No Render: **New +** -> **Web Service**.
- Conecte seu repositório.
- Preencha:
  - **Name:** `hubis-backend`
  - **Root Directory:** `backend`
  - **Runtime:** `Python 3`
  - **Build Command:** `pip install -r requirements.txt && python init_db.py`
  - **Start Command:** `gunicorn app:app`
- Em **Environment Variables**:
  - `JWT_SECRET`: Insira uma chave secreta qualquer (ex: `chave_super_secreta_123`).
- Clique em **Create Web Service**.
- Aguarde o deploy finalizar e copie a URL do backend gerada pelo Render.

#### 2. Criar o Frontend (Static Site)
- No Render: **New +** -> **Static Site**.
- Conecte o mesmo repositório.
- Preencha:
  - **Name:** `hubis-frontend`
  - **Root Directory:** `frontend`
  - **Build Command:** `npm install && npm run build`
  - **Publish Directory:** `dist`
- Em **Environment Variables**:
  - `VITE_API_URL`: cole a URL do seu backend (ex: `https://hubis-backend.onrender.com`).
- Em **Redirects/Rewrites**:
  - Clique em **Add Rule**:
    - **Source:** `/*`
    - **Destination:** `/index.html`
    - **Action:** `Rewrite`
  *(Isso garante que rotas como `/login` funcionem sem erro 404 ao atualizar a página).*
- Clique em **Create Static Site**.
