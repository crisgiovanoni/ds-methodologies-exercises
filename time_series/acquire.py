import pandas as pd
import requests
from pprint import pprint

def get_grocery(dict):
    """
    Argument: String of Dictionary with quoation marks.
    Returns data in json format.
    """
    response = pd.DataFrame(requests.get(f"https://python.zach.lol/api/v1/{dict}").json())
    return response

def get_sales():
    sales = get_grocery("sales")
    sales = pd.DataFrame(sales["payload"]["sales"])
    sales = sales[["sale_id","sale_date","sale_amount","store"]].set_index("sale_id")
    return sales

def get_germany():
    germany = pd.read_csv("/Users/cris/codeup-data-science/ds-methodologies-exercises/time_series/opsd_germany_daily.csv")
    return germany