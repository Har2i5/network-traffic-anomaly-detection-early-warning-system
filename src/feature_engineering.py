import pandas as pd
import numpy as np

def create_features(df):

    daily_ip = (
        df.groupby(['date','l_ipn'])['f']
        .sum()
        .reset_index()
    )

    daily_ip = daily_ip.sort_values(
        ['l_ipn','date']
    )

    daily_ip['rolling_mean'] = (
        daily_ip.groupby('l_ipn')['f']
        .transform(
            lambda x:
            x.rolling(
                7,
                min_periods=1
            ).mean()
        )
    )

    daily_ip['rolling_std'] = (
        daily_ip.groupby('l_ipn')['f']
        .transform(
            lambda x:
            x.rolling(
                7,
                min_periods=1
            ).std()
        )
    )

    daily_ip['rolling_std'] = (
        daily_ip['rolling_std']
        .fillna(0)
    )

    daily_ip['upper_limit'] = (
        daily_ip['rolling_mean']
        + 2*daily_ip['rolling_std']
    )

    daily_ip['anomaly'] = (
        daily_ip['f']
        > daily_ip['upper_limit']
    )

    daily_ip['lag_1'] = (
        daily_ip.groupby('l_ipn')['f']
        .shift(1)
    )

    daily_ip['lag_3'] = (
        daily_ip.groupby('l_ipn')['f']
        .shift(3)
    )

    daily_ip['lag_7'] = (
        daily_ip.groupby('l_ipn')['f']
        .shift(7)
    )

    daily_ip['pct_change'] = (
        daily_ip.groupby('l_ipn')['f']
        .pct_change()
    )

    daily_ip['rolling_max'] = (
        daily_ip.groupby('l_ipn')['f']
        .transform(
            lambda x:
            x.rolling(
                7,
                min_periods=1
            ).max()
        )
    )

    daily_ip['rolling_min'] = (
        daily_ip.groupby('l_ipn')['f']
        .transform(
            lambda x:
            x.rolling(
                7,
                min_periods=1
            ).min()
        )
    )

    daily_ip['momentum'] = (
        daily_ip.groupby('l_ipn')['f']
        .diff()
    )

    daily_ip['deviation_from_mean'] = (
        daily_ip['f']
        - daily_ip['rolling_mean']
    )

    daily_ip['z_score'] = (
        (daily_ip['f']
        - daily_ip['rolling_mean'])
        /
        (daily_ip['rolling_std']
        + 1e-5)
    )
    # ==========================================
    # Binary anomaly indicator
    # ==========================================

    daily_ip['anomaly_int'] = (
        daily_ip['anomaly']
        .astype(int)
    )

    # ==========================================
    # Consecutive anomaly count
    # ==========================================

    daily_ip['consecutive_anomalies'] = (

        daily_ip.groupby('l_ipn')
        ['anomaly_int']
        .rolling(
            window=3,
            min_periods=1
        )
        .sum()
        .reset_index(
            level=0,
            drop=True
        )

    )

    # ==========================================
    # Calendar Features
    # ==========================================

    daily_ip['day_of_week'] = (
        daily_ip['date']
        .dt.dayofweek
    )

    daily_ip['is_weekend'] = (
        daily_ip['day_of_week']
        >= 5
    ).astype(int)
    

    return daily_ip