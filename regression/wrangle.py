import pandas as pd
import numpy as np

import env

def get_db_url(db):
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'

def get_data_from_mysql():
    query = '''
    SELECT customer_id, monthly_charges, tenure, total_charges
    FROM customers
    WHERE contract_type_id = 3
    ORDER BY total_charges DESC;
    '''
    df = pd.read_sql(query, get_db_url("telco_churn"))
    return df

# df = get_data_from_mysql()

# def clean_data(df):
#     df = df[['customer_id', 'total_charges', 'monthly_charges', 'tenure']]
#     df.total_charges = df.total_charges.str.strip().replace('', np.nan).astype(float)
#     df = df.dropna()
#     return df

def clean_data(df):
    df = df[df.total_charges != ' ']
    df.total_charges = df.total_charges.astype(float)
    return df

# clean_data(df)
    
def wrangle_telco():
    return clean_data(get_data_from_mysql())

# data = wrangle_telco()
# data.head()