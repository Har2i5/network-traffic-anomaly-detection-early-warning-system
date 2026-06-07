def calculate_risk(df):

    df['risk_score'] = (

        0.35*abs(df['z_score'])

        +

        0.25*abs(
            df['pct_change']
        )

        +

        0.25*
        df[
            'consecutive_anomalies'
        ]

        +

        0.15*
        df[
            'anomaly_isoforest'
        ]

    )

    return df