from ingestion import load_data

from feature_engineering import create_features

from isolation_forest_model import run_isolation_forest

from forecasting import forecast_all_workstations

from risk_scoring import calculate_risk

from save_results import (
    save_features,
    save_forecasts,
    save_raw_data,
    save_risk_scores
)

# Load Data
df = load_data(
    "data/cs448b_ipasn.csv"
)

# Feature Engineering
features = create_features(df)

# Isolation Forest
features = run_isolation_forest(features)

print(features.columns.tolist())

# Risk Scoring
risk_df = calculate_risk(features)

# Forecasting
forecast_df = forecast_all_workstations(features)

raw_df = df.copy()


# Save to Postgres
save_features(features)

save_forecasts(forecast_df)

save_risk_scores(risk_df)

save_raw_data(raw_df)

print("Pipeline completed successfully.")