import pandas as pd
import requests
from os import path

from pprint import pprint

# def get_grocery(dict):
#     """
#     Argument: String of Dictionary with quoation marks.
#     Returns data in json format.
#     """
#     response = pd.DataFrame(requests.get(f"https://python.zach.lol/api/v1/{dict}").json())
#     return response

# def get_sales():
#     sales = get_grocery("sales")
#     sales = pd.DataFrame(sales["payload"]["sales"])
#     sales = sales[["sale_id","sale_date","sale_amount","store"]].set_index("sale_id")
#     return sales

# def get_germany():
#     germany = pd.read_csv("/Users/cris/codeup-data-science/ds-methodologies-exercises/time_series/opsd_germany_daily.csv")
#     return germany

BASE_URL = 'https://python.zach.lol'
API_BASE = BASE_URL + '/api/v1'

def get_store_data_from_api():
    url = API_BASE + '/stores'
    response = requests.get(url)
    data = response.json()
    return pd.DataFrame(data['payload']['stores'])

def get_item_data_from_api():
    url = API_BASE + '/items'
    response = requests.get(url)
    data = response.json()

    stores = data['payload']['items']

    while data['payload']['next_page'] is not None:
        print('Fetching page {} of {}'.format(data['payload']['page'] + 1, data['payload']['max_page']))
        url = BASE_URL + data['payload']['next_page']
        response = requests.get(url)
        data = response.json()
        stores += data['payload']['items']

    return pd.DataFrame(stores)

def get_sale_data_from_api():
    url = API_BASE + '/sales'
    response = requests.get(url)
    data = response.json()

    stores = data['payload']['sales']

    while data['payload']['next_page'] is not None:
        print('Fetching page {} of {}'.format(data['payload']['page'] + 1, data['payload']['max_page']))
        url = BASE_URL + data['payload']['next_page']
        response = requests.get(url)
        data = response.json()
        stores += data['payload']['sales']

    return pd.DataFrame(stores)

def get_store_data(use_cache=True):
    if use_cache and path.exists('stores.csv'):
        return pd.read_csv('stores.csv')
    df = get_store_data_from_api()
    df.to_csv('stores.csv', index=False)
    return df

def get_item_data(use_cache=True):
    if use_cache and path.exists('items.csv'):
        return pd.read_csv('items.csv')
    df = get_item_data_from_api()
    df.to_csv('items.csv', index=False)
    return df

def get_sale_data(use_cache=True):
    if use_cache and path.exists('sales.csv'):
        return pd.read_csv('sales.csv')
    df = get_sale_data_from_api()
    df.to_csv('sales.csv', index=False)
    return df

def get_all_data():
    sales = get_sale_data()
    items = get_item_data()
    stores = get_store_data()

    sales = sales.rename(columns={'item': 'item_id', 'store': 'store_id'})

    return sales.merge(items, on='item_id').merge(stores, on='store_id')

def get_opsd_data(use_cache=True):
    if use_cache and path.exists('opsd.csv'):
        return pd.read_csv('opsd.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    df.to_csv('opsd.csv', index=False)
    return df