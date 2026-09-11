# Contratos da API - Hubis Vitrine

Este documento define os contratos da API para Spec Driven Development (SDD).

## Configuração Global
- **Base URL:** Normalizada para `/api` no frontend. No backend local: `http://localhost:5174/api`.
- **Content-Type:** `application/json` (exceto `/api/upload` que usa `multipart/form-data`).
- **Autenticação:** JWT via Header `Authorization: Bearer <token>`.

## Modelos de Dados (Objetos JSON)

### Category
```json
{
  "id": "string",
  "name": "string",
  "color": "string | null",
  "emoji": "string | null"
}
```

### Enterprise
```json
{
  "id": "string",
  "name": "string",
  "category": "string",
  "coverImage": "string (URL)",
  "description": "string (short)",
  "fullDescription": "string",
  "whatsapp": "string",
  "instagram": "string",
  "email": "string",
  "tags": ["string"],
  "products": ["Product"]
}
```

### Product
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "price": "number",
  "priceMode": "single | range | hidden",
  "priceMin": "number | null",
  "priceMax": "number | null",
  "image": "string (URL)",
  "images": ["string (URL)"]
}
```

### User
```json
{
  "id": "string",
  "email": "string",
  "name": "string",
  "role": "admin | owner",
  "enterpriseId": "string | null",
  "active": "boolean"
}
```

---

## Endpoints

### Health
- **GET `/health`**
  - **Response (200):** `{ "status": "ok" }`.

### Autenticação
- **POST `/login`**
  - **Body:** `{ "email": "string", "password": "string" }`
  - **Response (200):** Objeto User + `"token": "string"`.
  - **Response (400):** `{ "message": "email and password required" }` ou validação de formato.
  - **Response (401):** `{ "ok": false }`.
- **GET `/auth/verify` (Auth Required)**
  - **Response (200):** `{ "ok": true }`.

### Categorias
- **GET `/categories`**
  - **Query Params:** `format=objects` para retornar lista de objetos, caso contrário retorna lista de nomes (strings).
  - **Response (200):** `[Category]` ou `[string]`.
- **GET `/categories/<id>`**
  - **Response (200):** `Category`.
- **POST `/categories` (Admin Only)**
  - **Body:** `{ "name": "string", "color": "string", "emoji": "string" }`
  - **Response (201):** `Category`.
- **PUT `/categories/<id>` (Admin Only)**
  - **Body:** `{ "name": "string", "color": "string", "emoji": "string" }`
- **DELETE `/categories/<id>` (Admin Only)**
  - **Response (200):** `{ "ok": true }`.
  - **Response (409):** `{ "message": "category in use" }`.

### Empreendimentos
- **GET `/enterprises`**
  - **Response (200):** `[Enterprise]`.
- **GET `/enterprises/<id>`**
  - **Response (200):** `Enterprise`.
- **POST `/enterprises` (Auth Required)**
  - **Body:** `{ "name": "string", "category": "string", "coverImage": "base64", ... }`.
  - **Response (201):** `Enterprise`.
  - **Response (400):** validações de `email` e `whatsapp`.
- **PUT `/enterprises/<id>` (Admin or Owner)**
  - **Body:** Campos parciais de Enterprise. `coverImage` aceita Base64 para novo upload.
  - **Response (400):** validações de `email` e `whatsapp`.
- **DELETE `/enterprises/<id>` (Admin or Owner)**

### Produtos
- **POST `/enterprises/<ent_id>/products` (Admin or Owner)**
  - **Body:** Schema de Product (price info + images em base64 ou URLs).
  - **Response (201):** `Product`.
- **PUT `/enterprises/<ent_id>/products/<prod_id>` (Admin or Owner)**
- **DELETE `/enterprises/<ent_id>/products/<prod_id>` (Admin or Owner)**

### Usuários
- **GET `/users` (Admin Only)**
- **POST `/users` (Admin Only)**
  - **Body:** `{ "email": "string", "password": "string", "name": "string", "role": "admin | owner", "enterpriseId": "string | null", "active": "boolean" }`
  - **Response (400):** validações de `email` e senha (min. 10 caracteres).
- **PUT `/users/<id>` (Admin or Self)**
  - **Body:** campos parciais de User, incluindo `password`.
  - **Response (400):** validações de `email` e senha (min. 10 caracteres).
- **DELETE `/users/<id>` (Admin or Self)**

### Uploads
- **POST `/upload` (Auth Required)**
  - **Content-Type:** `multipart/form-data`
  - **Response (201):** `{ "url": "/uploads/<filename>", "filename": "..." }`.
  - **Restrições:** arquivos `png`, `jpg`, `jpeg`, `gif`, `webp`.
- **GET `/uploads/<filename>`**
  - Retorna o arquivo binário.

---

## Notas de validação e autenticação
- **Erros de autenticação/autorização:**
  - `401` para header ausente, token inválido ou expirado.
  - `403` para falta de permissão (ex: admin requerido).
- **Imagens Base64:** apenas `jpeg`, `png`, `webp`, tamanho máximo 5MB.
- **Senha:** mínimo de 10 caracteres.
- **Telefone BR:** 10 ou 11 dígitos; se 11, o nono dígito deve ser `9`.
