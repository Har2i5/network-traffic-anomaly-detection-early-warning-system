from prophet import Prophet
import numpy as np
import pandas as pd

def forecast_all_workstations(df):

    forecasts = []

    for ws in sorted(
        df['l_ipn'].unique()
    ):

        ws_df = (
            df[df['l_ipn']==ws]
            [['date','f']]
            .copy()
        )

        ws_df.columns = [
            'ds',
            'y'
        ]

        ws_df['y'] = np.log1p(
            ws_df['y']
        )

        model = Prophet()

        model.fit(ws_df)

        future = (
            model.make_future_dataframe(
                periods=7
            )
        )

        fc = model.predict(
            future
        )

        fc['l_ipn'] = ws

        forecasts.append(fc)

    return pd.concat(
        forecasts
    )