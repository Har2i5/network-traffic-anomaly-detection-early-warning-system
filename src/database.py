from sqlalchemy import create_engine

# DB_USER = "postgres"
# DB_PASSWORD = "postgres"
# DB_HOST = "localhost"
# DB_PORT = "5432"
# DB_NAME = "network_intelligence"

# # DATABASE_URL = (
# #     f"postgresql://{DB_USER}:{DB_PASSWORD}"
# #     f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# # )

# engine = create_engine(
#     "postgresql://postgres:postgres@host.docker.internal:5432/network_intelligence"
# )
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/network_intelligence"
)

engine = create_engine(DATABASE_URL)