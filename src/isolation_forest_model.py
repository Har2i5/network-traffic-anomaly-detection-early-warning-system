from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

def run_isolation_forest(df):

    features = [
        'f',
        'lag_1',
        'lag_3',
        'lag_7',
        'pct_change',
        'rolling_max',
        'rolling_min',
        'momentum',
        'deviation_from_mean',
        'z_score'
    ]

    clean = df.dropna(
        subset=features
    ).copy()

    clean['anomaly_isoforest'] = 0

    for ws in clean['l_ipn'].unique():

        sub = clean[
            clean['l_ipn']
            ==
            ws
        ]

        scaler = StandardScaler()

        X = scaler.fit_transform(
            sub[features]
        )

        iso = IsolationForest(
            contamination=0.05,
            random_state=42
        )

        preds = iso.fit_predict(X)

        clean.loc[
            sub.index,
            'anomaly_isoforest'
        ] = (
            preds == -1
        ).astype(int)

    return clean