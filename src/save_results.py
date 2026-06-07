from database import engine

def save_features(features_df):

    features_df.to_sql(
        "traffic_features",
        engine,
        if_exists="replace",
        index=False
    )


def save_forecasts(forecasts_df):

    forecasts_df.to_sql(
        "traffic_forecasts",
        engine,
        if_exists="replace",
        index=False
    )


def save_risk_scores(risk_df):

    risk_df.to_sql(
        "risk_scores",
        engine,
        if_exists="replace",
        index=False
    )
    
def save_raw_data(raw_df):

    raw_df.to_sql(
        "network_raw",
        engine,
        if_exists="replace",
        index=False
    )