"""
Python script to access (at the moment, FRED) API data.

We currently import a csv with the list of FRED series_ids and HTML ids.
We then use these series to perform a python request and call FRED data.
It is then saved to local directory.
"""

import datetime
import json
import requests

import pandas as pd

from dateutil.relativedelta import relativedelta

# ______________________________________________________________________________
# 

def get_historical_data(series_id, file_name, num_years, source = 'fred'):
    print('Running.')
    """
    Get historical data for the past number yeas (num_years). 

    If FRED = source:
        - Return as a JSON with observations in ['observations'] with
        associated values and dates.
    """
    if source == 'fred':
        fred_key = secrets.fred_api_key
        series_id = series_id
        observation_start = (datetime.datetime.today() - relativedelta(years=num_years)).strftime('%Y-%m-%d')
        observation_end = datetime.datetime.today().strftime('%Y-%m-%d') # Today"
          

        # Observations returned in in descending order: 'sort_order=desc'
        url = 'https://api.stlouisfed.org/fred/series/observations?series_id='+series_id+'&observation_start='+observation_start+'&observation_end='+observation_end+'&api_key='+fred_key+'&sort_order=desc&file_type=json'

        file_name = file_name
        with open(file_name, 'w') as outfile:
            json.dump(requests.get(url).json(), outfile)
        return True

if __name__ == "__main__":
    # get_historical_data('CPIAUCSL', 'cpi.json', 19, 'fred') # One call
    fred_sources = pd.read_csv('fred_sources.csv')
    series_ids = fred_sources['series_id']
    my_ids = fred_sources['my_id']
    # Read csv which has file ids and FRED ids
    for series_id, idd in zip(series_ids, my_ids):
        get_historical_data(series_id, '{}.json'.format(idd), 19, 'fred')