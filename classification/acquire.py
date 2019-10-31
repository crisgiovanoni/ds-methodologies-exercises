import pandas as pd
import numpy as np

import env

def get_titanic_data():
    """
    Returns the titanic data from the codeup data science database as a pandas data frame.
    """
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/titanic_db'
    query = """
    SELECT *
    FROM passengers
    """
    df = pd.read_sql(query, url)
    return df

def get_iris_data():
    """
    Returns the data from the iris_db on the codeup data science database as a pandas data frame.
    The returned data frame should include the actual name of the species in addition to the species_ids.
    """
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/iris_db'
    query = """
    SELECT *
    FROM measurements
    JOIN species
	    USING(species_id)
    """
    df = pd.read_sql(query, url)
    return df