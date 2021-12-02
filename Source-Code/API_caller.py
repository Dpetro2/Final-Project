import dash
import pandas as pd
import urllib
import json

__eia_key = 'ad322cda271997fdc729b8e18c98bddd'
__state_list = ['AL',
              'AK',
              'AZ',
              'AR',
              'CA',
              'CO',
              'CT',
              'DE',
              'DC',
              'FL',
              'GA',
              'HI',
              'ID',
              'IL',
              'IN',
              'IA',
              'KS',
              'KY',
              'LA',
              'ME',
              'MD',
              'MA',
              'MI',
              'MN',
              'MS',
              'MO',
              'MT',
              'NE',
              'NV',
              'NH',
              'NJ',
              'NM',
              'NY',
              'NC',
              'ND',
              'OH',
              'OK',
              'OR',
              'PA',
              'RI',
              'SC',
              'SD',
              'TN',
              'TX',
              'UT',
              'VT',
              'VA',
              'WA',
              'WV',
              'WI',
              'WY']


def __api_series_query_url_maker(msn):
    api_key = __eia_key
    eia_url = 'http://api.eia.gov/series/?api_key=' + api_key
    series_id = '&series_id='
    for x in __state_list:
        series_id = series_id + 'SEDS.' + msn + '.' + x + '.A;'

    final_url = eia_url + series_id
    return final_url


def create_pd_df(msn):
    #loading json from API
    json_obj = urllib.request.urlopen(__api_series_query_url_maker(msn))
    data = json.load(json_obj)
    df = data['series']
    pd_df_list = []

    #loop to put each call into list
    for i, j in enumerate(__state_list):
        sub_df = df[i]
        state = sub_df['series_id'][11] + sub_df['series_id'][12]
        id = sub_df['series_id'][5] + sub_df['series_id'][6] + sub_df['series_id'][7] + sub_df['series_id'][8] + sub_df['series_id'][9]
        sub_df = sub_df['data']
        pd_df = pd.DataFrame(sub_df, columns=['Year', 'data'])
        pd_df['State'] = state
        pd_df['MSN'] = id
        pd_df_list.append(pd_df)
    #compiles list into pandas dataframe
    pd_df = pd.concat(pd_df_list)
    return pd_df
