"""Configurações centrais do backend.

Variáveis de ambiente (obrigatórias em produção):
  DATABASE_URL  → PostgreSQL do Supabase
                  ex.: postgresql+psycopg2://postgres:[PASSWORD]@[HOST]:5432/postgres
  SECRET_KEY    → chave longa e aleatória (ex.: `openssl rand -hex 32`)
  CORS_ORIGINS  → origens permitidas (separadas por vírgula)
  RENDER_EXTERNAL_URL → usado automaticamente pelo Render.com
"""
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "TROQUE-ESTA-CHAVE-EM-PRODUCAO-9f8a7b6c")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "720"))  # 12h

# Em produção: DATABASE_URL com PostgreSQL do Supabase.
# Em desenvolvimento: SQLite (padrão) ou defina DATABASE_URL manualmente.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./manutencao.db")

# Origens liberadas para CORS (app Flet web, TV, etc.)
# Em produção, restrinja às URLs do seu app (ex.: https://seuapp.vercel.app)
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
