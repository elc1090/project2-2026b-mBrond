import json
from fastapi import FastAPI, UploadFile, File, Form, Query
from pydantic import BaseModel
from typing import List, Optional, Any, Union
app = FastAPI(title="Hubis API", version="1.0.0", description="API documentation for Hubis backend.")
# --- Models ---
class HealthResponse(BaseModel):
    status: str
class CategoryResponse(BaseModel):
    id: str
    name: str
    color: Optional[str] = None
    emoji: Optional[str] = None
class CategoryCreate(BaseModel):
    name: str
    color: Optional[str] = None
    emoji: Optional[str] = None
class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None
    emoji: Optional[str] = None
class ProductResponse(BaseModel):
    id: str
    name: str
    description: str
    image: str
    images: List[str]
    price: float
    priceMode: str
    priceMin: Optional[float] = None
    priceMax: Optional[float] = None
class ProductCreate(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    price: Optional[float] = None
    priceMode: Optional[str] = None
    priceMin: Optional[float] = None
    priceMax: Optional[float] = None
    image: Optional[str] = None
    images: Optional[List[str]] = None
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    priceMode: Optional[str] = None
    priceMin: Optional[float] = None
    priceMax: Optional[float] = None
    image: Optional[str] = None
    images: Optional[List[str]] = None
class EnterpriseResponse(BaseModel):
    id: str
    name: str
    category: str
    coverImage: Optional[str] = None
    description: str
    fullDescription: str
    whatsapp: str
    instagram: str
    email: str
    tags: List[str]
    products: List[ProductResponse]
class EnterpriseCreate(BaseModel):
    id: Optional[str] = None
    name: str
    category: Optional[str] = "Artesanato"
    coverImage: Optional[str] = None
    description: Optional[str] = None
    fullDescription: Optional[str] = None
    whatsapp: Optional[str] = None
    instagram: Optional[str] = None
    email: Optional[str] = None
    tags: Optional[List[str]] = []
class EnterpriseUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    coverImage: Optional[str] = None
    description: Optional[str] = None
    fullDescription: Optional[str] = None
    whatsapp: Optional[str] = None
    instagram: Optional[str] = None
    email: Optional[str] = None
    tags: Optional[List[str]] = None
class UserResponse(BaseModel):
    id: str
    email: str
    name: Optional[str] = None
    role: str
    enterpriseId: Optional[str] = None
    active: bool
class UserCreate(BaseModel):
    id: Optional[str] = None
    email: str
    password: str
    name: Optional[str] = None
    role: Optional[str] = "owner"
    enterpriseId: Optional[str] = None
    active: Optional[bool] = True
class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None
    role: Optional[str] = None
    enterpriseId: Optional[str] = None
    active: Optional[bool] = None
class LoginRequest(BaseModel):
    email: str
    password: str
class LoginResponse(UserResponse):
    token: str
class UploadResponse(BaseModel):
    url: str
    filename: str
class MessageResponse(BaseModel):
    ok: bool
# --- Routes ---
@app.get("/api/health", response_model=HealthResponse, tags=["Health"])
def health():
    pass
@app.get("/api/categories", response_model=Union[List[CategoryResponse], List[str]], tags=["Categories"])
def list_categories(format: Optional[str] = Query(None, description="Set to 'objects' to return a list of objects instead of strings")):
    pass
@app.post("/api/categories", response_model=CategoryResponse, status_code=201, tags=["Categories"])
def create_category(payload: CategoryCreate):
    pass
@app.get("/api/categories/{cat_id}", response_model=CategoryResponse, tags=["Categories"])
def category_detail(cat_id: str):
    pass
@app.put("/api/categories/{cat_id}", response_model=CategoryResponse, tags=["Categories"])
def update_category(cat_id: str, payload: CategoryUpdate):
    pass
@app.delete("/api/categories/{cat_id}", response_model=MessageResponse, tags=["Categories"])
def delete_category(cat_id: str):
    pass
@app.get("/api/enterprises", response_model=List[EnterpriseResponse], tags=["Enterprises"])
def list_enterprises():
    pass
@app.post("/api/enterprises", response_model=EnterpriseResponse, status_code=201, tags=["Enterprises"])
def create_enterprise(payload: EnterpriseCreate):
    pass
@app.get("/api/enterprises/{ent_id}", response_model=EnterpriseResponse, tags=["Enterprises"])
def enterprise_detail(ent_id: str):
    pass
@app.put("/api/enterprises/{ent_id}", response_model=EnterpriseResponse, tags=["Enterprises"])
def update_enterprise(ent_id: str, payload: EnterpriseUpdate):
    pass
@app.delete("/api/enterprises/{ent_id}", response_model=MessageResponse, tags=["Enterprises"])
def delete_enterprise(ent_id: str):
    pass
@app.post("/api/enterprises/{ent_id}/products", response_model=ProductResponse, status_code=201, tags=["Products"])
def create_product(ent_id: str, payload: ProductCreate):
    pass
@app.put("/api/enterprises/{ent_id}/products/{prod_id}", response_model=ProductResponse, tags=["Products"])
def modify_product(ent_id: str, prod_id: str, payload: ProductUpdate):
    pass
@app.delete("/api/enterprises/{ent_id}/products/{prod_id}", response_model=MessageResponse, tags=["Products"])
def delete_product(ent_id: str, prod_id: str):
    pass
@app.get("/api/users", response_model=List[UserResponse], tags=["Users"])
def list_users():
    pass
@app.post("/api/users", response_model=UserResponse, status_code=201, tags=["Users"])
def create_user(payload: UserCreate):
    pass
@app.put("/api/users/{user_id}", response_model=UserResponse, tags=["Users"])
def update_user(user_id: str, payload: UserUpdate):
    pass
@app.delete("/api/users/{user_id}", response_model=MessageResponse, tags=["Users"])
def delete_user(user_id: str):
    pass
@app.post("/api/login", response_model=LoginResponse, tags=["Auth"])
def login(payload: LoginRequest):
    pass
@app.get("/api/auth/verify", response_model=MessageResponse, tags=["Auth"])
def verify_auth():
    pass
@app.get("/uploads/{name}", tags=["Uploads"])
def download_file(name: str):
    pass
@app.post("/api/upload", response_model=UploadResponse, status_code=201, tags=["Uploads"])
def upload_file(file: UploadFile = File(...)):
    pass
if __name__ == "__main__":
    openapi_schema = app.openapi()
    with open("openapi.json", "w", encoding="utf-8") as f:
        json.dump(openapi_schema, f, indent=2, ensure_ascii=False)
    print("OpenAPI schema written to openapi.json")