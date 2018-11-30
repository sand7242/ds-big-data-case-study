import pandas as pd
import matplotlib.pyplot as plt

def pay_Bor(df):
    df_payment_type_names = df['payment_type_names']
    df_PU_Borough_names = df['PU_Borough_names']
    df_crosstabs_Borough_PU = pd.crosstab(df_payment_type_names,df_PU_Borough_names, normalize='columns')
    df_crosstabs_Borough_PU.plot(kind='bar')
    plt.xticks(rotation=60, horizontalalignment='right')
    plt.xlabel('Payment Type', weight='bold')
    plt.ylabel('Proportion Payment Type per Borough', weight='bold')
    plt.legend(title='Borough', loc='upper right')
    plt.title('Payment Type by Borough', weight='bold', fontsize=15)
    plt.tight_layout()
    plt.show()

def pay_Zone(df):
    df_payment_type_names = df['payment_type_names']
    df_PU_Zone_names = df['PU_Zone_names']
    df_crosstabs_Zone_PU = pd.crosstab(df_payment_type_names,df_PU_Zone_names, normalize='columns')
    df_crosstabs_Zone_PU.plot(kind='bar')
    plt.xticks(rotation=60, horizontalalignment='right')
    plt.xlabel('Payment Type', weight='bold')
    plt.ylabel('Proportion Payment Type per Zone', weight='bold')
    plt.legend(title='Zone', loc='upper right')
    plt.title('Payment Type by Zone', weight='bold', fontsize=15)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    df_zone = pd.read_csv('/Users/janestout/Desktop/taxi_data/taxi _zone_lookup.csv')
    df = pd.read_csv('/Users/janestout/Desktop/taxi_data/taxi_subsample.csv')
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    pd.options.display.max_columns = 200

    dict_payment_type = {1: 'Credit card', 2: 'Cash', 3: 'No charge', 4: 'Dispute', 5: 'Unknown', 6: 'Voided trip'}
    df['payment_type_names'] = df['payment_type'].replace(dict_payment_type)

    Borough_dict = pd.Series(df_zone.Borough.values,index=df_zone.LocationID).to_dict()
    df['PU_Borough_names'] = df['PULocationID'].replace(Borough_dict)
    # df['DO_Borough_names'] = df['DOLocationID'].replace(Borough_dict)
    # #
    # Zone_dict = pd.Series(df_zone.Zone.values,index=df_zone.LocationID).to_dict()
    # df['PU_Zone_names'] = df['PULocationID'].replace(Zone_dict)
    #
    # service_zone_dict = pd.Series(df_zone.service_zone.values,index=df_zone.LocationID).to_dict()
    # df['PU_service_zone_names'] = df['PULocationID'].replace(service_zone_dict)

    print(pay_Bor(df))
    # print(pay_Zone(df))
