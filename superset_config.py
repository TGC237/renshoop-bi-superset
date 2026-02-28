import os

# Construction de l'URI PostgreSQL pour le conteneur 'postgres'
# Format: postgresql://user:password@hostname:port/db_name
DATABASE_USER = os.getenv("DB_USER", "superset_admin")
DATABASE_PASSWORD = os.getenv("DB_PASS")
DATABASE_HOST = os.getenv("DB_HOST", "postgres")
DATABASE_PORT = os.getenv("DB_PORT", "5432")
DATABASE_DB = os.getenv("DB_NAME", "superset")

SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"

# Sécurité indispensable pour Cloudflare + NPM
ENABLE_PROXY_FIX = True
SECRET_KEY = os.getenv("SUPERSET_SECRET_KEY")

# Cache Redis (Utilise le conteneur superset_redis qu'on va lancer)
CACHE_CONFIG = {
    'CACHE_TYPE': 'RedisCache',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_REDIS_HOST': 'superset_redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
}
