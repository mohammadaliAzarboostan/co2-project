import joblib

import pandas as pd



model = joblib.load("../models/model.pkl")



sample = pd.DataFrame(

{

"engine":[2.5],

"cylandr":[4],

"fuelcity":[10],

"fuelwy":[7],

"fuelcomb":[8.5]

}

)



result = model.predict(sample)

print(result[0])