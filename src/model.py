from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestRegressor


def build_model():

    model = Pipeline(

        [

            ("scaler", StandardScaler()),

            ("rf", RandomForestRegressor(

                n_estimators=250,

                random_state=42,

                max_depth=12

            ))

        ]

    )

    return model