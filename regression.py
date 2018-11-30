import pandas as pd
# import numpy as np
# from pandas.plotting import scatter_matrix
# import matplotlib.pyplot as plt
# import seaborn as sns
# from matplotlib import pyplot
# from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

def linear(X, y):
    X = sm.add_constant(X)
    result = sm.OLS(y,X).fit()
    # predictions = result_train.predict(X_train)
    # print('TRAINING MODEL')
    print(result.summary())
    return result

if __name__ == '__main__':
    df_zone = pd.read_csv('/Users/janestout/Desktop/taxi_data/taxi _zone_lookup.csv')
    df = pd.read_csv('/Users/janestout/Desktop/taxi_data/taxi_subsample.csv')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    pd.options.display.max_columns = 200

    dict_payment_type = {1: 'Credit card', 2: 'Cash', 3: 'No charge', 4: 'Dispute', 5: 'Unknown', 6: 'Voided trip'}
    df['payment_type_names'] = df['payment_type'].replace(dict_payment_type)

    Borough_dict = pd.Series(df_zone.Borough.values,index=df_zone.LocationID).to_dict()
    df['PU_Borough_names'] = df['PULocationID'].replace(Borough_dict)

    df = df[['PU_Borough_names', 'trip_distance', 'tip_amount']]
    X = df[['PU_Borough_names']]
    # X = df[['PU_Borough_names', 'trip_distance']]
    y = df[['tip_amount']]
    X = pd.get_dummies(X, columns=['PU_Borough_names'])
    X.drop(['PU_Borough_names_Queens'], axis=1, inplace=True)

    print(linear(X,y))
