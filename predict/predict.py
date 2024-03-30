import pandas as pd
import xgboost as xg
#xgboost: used to build models to predict outcomes/classify/regression models
import matplotlib.pyplot as plot

#load dataset, interchangable
#TODO: implement dynamic non-csv dataset so it doesn't have to be static as one csv file: AAPL for sake of demonstration

data = pd.read_csv('/Users/mattanto/Desktop/quantspec/predict/AAPL_data.csv')
#show data
#print(data)

#data['close'].plot()

train_data = data.iloc[:int(.99*len(data)), :]

test_data = data.iloc[int(.99*len(data)):, :]

features = ['open', 'volume']
target = 'close'

#create model/train

model = xg.XGBRegressor()

model.fit(train_data[features], train_data[target])

#predict display predictions from test data
prediction = model.predict(test_data[features])

print('Model Predictions:\n')

#unrefined vals
print(prediction)

#actual vals
print("Actual Vals:")
print(test_data[target])
