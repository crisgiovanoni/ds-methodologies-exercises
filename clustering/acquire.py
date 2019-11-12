# Standard
import pandas as pd
import numpy as np
import env


def get_db_url(db):
    """
    Produces a url from env credentials
    >> Input:
    database
    << Output:
    url
    """
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{db}'

def get_sql_zillow():
    """
    Queries from zillow database with the following conditions:
    - Single-unit properties
    - 
    >> Input:
    database
    << Output:
    url
    """
    query = '''
    SELECT * FROM properties_2017
    LEFT JOIN airconditioningtype
	    USING(airconditioningtypeid)
    LEFT JOIN architecturalstyletype
	    USING(architecturalstyletypeid)
    LEFT JOIN buildingclasstype
	    USING(buildingclasstypeid)
    LEFT JOIN heatingorsystemtype
	    USING(heatingorsystemtypeid)
    JOIN predictions_2017
	    USING(parcelid)
    LEFT JOIN propertylandusetype
	    USING(propertylandusetypeid)
    LEFT JOIN storytype
	    USING(storytypeid)
    LEFT JOIN typeconstructiontype
	    USING(typeconstructiontypeid)
    WHERE latitude is not null and longitude is not null
    ''' 
    df = pd.read_sql(query, get_db_url("zillow"))
    return df


def standardize_missing(df):
    """
    Converts true null values in various funky format to np.nan
    """
    missing = ["", " ", None]
    for col in df.columns:
        df[col] = df[col].replace(missing, np.nan)
    return df

def handle_missing_values(df, prop_required_column = .5, prop_required_row = .75):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df-p