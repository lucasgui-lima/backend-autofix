"""Gestão de Chamados de Manutenção — API (FastAPI).

Executar em desenvolvimento:
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
Documentação interativa: http://localhost:8000/docs
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import CORS_ORIGINS, DATABASE_URL
from .database import Base, engine
from .routers import analytics, auth_router, cadastros, chamados, tv, users

# Cria as tabelas no banco de dados (SQLite ou PostgreSQL)
# No PostgreSQL do Supabase, execute também backend/supabase-schema.sql
# para garantir que os índices sejam criados.
if DATABASE_URL.startswith("sqlite"):
    Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestão de Chamados de Manutenção",
    version="1.0.0",
    description="API do aplicativo de gestão de chamados (mobile + TV).",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(users.router)
app.include_router(cadastros.router)
app.include_router(chamados.router)
app.include_router(analytics.router)
app.include_router(tv.router)


@app.get("/", tags=["health"])
def health():
    return {"status": "ok", "app": "gestao-manutencao", "versao": "1.0.0"}
