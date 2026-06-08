import pandas as pd
from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/network_intelligence"
)

engine = create_engine(DATABASE_URL)

pd.read_sql(
    "SELECT * FROM traffic_features",
    engine
).to_csv("data/traffic_features.csv", index=False)

pd.read_sql(
    "SELECT * FROM traffic_forecasts",
    engine
).to_csv("data/traffic_forecasts.csv", index=False)

pd.read_sql(
    "SELECT * FROM risk_scores",
    engine
).to_csv("data/risk_scores.csv", index=False)

print("Export complete")