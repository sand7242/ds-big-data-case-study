from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.grid_search import GridSearchCV
import pandas as pd
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

'''
Determine Features for predicting tip amount
'''

def clean_prepare_data(df):
    df = pd.get_dummies(df,columns = ['vendor_id','rate_code','payment_type'])
    df.drop(['total_amount','pickup_datetime','dropoff_datetime','hack_license','medallion'],axis = 1,inplace = 1)
    df.dropna(inplace = 1)

    y = df.pop('tip_amount').values
    x = df.values
    return x,y,df

def rf_cross_val(x,y):
    X_train, X_test, y_train, y_test = train_test_split(x,y,test_size = 0.33, random_state = 42)

    random_forest_grid = {'n_estimators': [100],
                                    'n_jobs': [-1]}

    rf_gridsearch = GridSearchCV(RandomForestRegressor(),
                                 random_forest_grid,
                                 n_jobs=-1,
                                 verbose=True,
                                 cv=3)

    rf_gridsearch.fit(X_train, y_train)

    print ("best parameters:", rf_gridsearch.best_params_)

    best_rf_model = rf_gridsearch.best_estimator_

    y_pred = best_rf_model.predict(X_test)

    print ("Accuracy with best rf:", cross_val_score(best_rf_model, X_test, y_test).mean())

    rf = RandomForestRegressor(n_estimators=10, n_jobs = -1)

    print ("Accuracy with default param rf:", cross_val_score(rf, X_test, y_test).mean())
    return best_rf_model

def plot_important_features(best_rf_model,df):
    futures = zip(df.columns.tolist(),best_rf_model.feature_importances_)
    futures.sort(key = lambda x:x[1],reverse = 1)

    labels = []
    fracs = []
    total = 0

    for f,v in futures:
        if total < .90:
            print (f,v)
            labels.append(f)
            fracs.append(v)
            total += v
    labels = ['Fare Amount','Credit Card','Dropoff Lon','Dropoff Lat','Pickup Lon','Trip Time','Features Left Off']
    fracs.append(1-sum(fracs))
    explode = [0]*len(fracs)
    explode[-1] = 0.1

    figure(1,figsize=(6,6),frameon = 0)
    title('%1.1f%% Feature Importance'% (sum(fracs[:-1])*100))
    colors = ['royalblue','g','r','c','m','gold','darkgray']
    pie(fracs, explode=explode, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90,colors = colors)
    plt.show()

if __name__ == '__main__':
    # data_path = '/Users/janestout/Desktop/taxi_data/yellow_tripdata_2017-01.csv'
    # df = pd.read_csv(data_path)
    # df=df.sample(frac=0.001, replace=False)
    # df.to_csv('/Users/janestout/Desktop/taxi_data/taxi_subsample.csv')
    df = pd.read_csv('/Users/janestout/Desktop/taxi_data/taxi_subsample.csv')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    pd.options.display.max_columns = 200
    # x,y,df = clean_prepare_data(df)
    # best_rf_model = rf_cross_val(x,y)
    # plot_important_features(best_rf_model,df)
