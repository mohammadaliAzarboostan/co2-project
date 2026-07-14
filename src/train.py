import joblib

import os

from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_absolute_error

from sklearn.metrics import mean_squared_error

from sklearn.metrics import r2_score

from preprocess import DataLoader

from model import build_model



loader = DataLoader("../data/co22.csv")

X, y = loader.split()



X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)



model = build_model()

model.fit(X_train, y_train)



prediction = model.predict(X_test)



print("="*40)

print("Training Result")

print("="*40)

print()

print("MAE :", mean_absolute_error(y_test,prediction))

print()

print("RMSE :", mean_squared_error(y_test,prediction,squared=False))

print()

print("R2 :", r2_score(y_test,prediction))

print()

os.makedirs("../models",exist_ok=True)

joblib.dump(model,"../models/model.pkl")

print("Model Saved Successfully")