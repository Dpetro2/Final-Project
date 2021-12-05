import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html
import pandas as pd
import plotly.offline as pyo
import urllib
import API_caller as api


def cost_converter(state, value):
    consume_df = api.create_pd_df('TERPB')
    price_df = api.create_pd_df('TERCD')

    consume_df = consume_df[consume_df['Year'] == '2019']
    consume_df = consume_df[consume_df['State'] == state]
    price_df = price_df[price_df['Year'] == '2019']
    price_df = price_df[price_df['State'] == state]

    return np.round(convert_dollar_to_btu(value, 4, price_df), decimals=2)


def convert_dollar_to_btu(dollars, num_panels, price_df):
    btu = dollars / price_df['data']
    btu_per_panel = 1706000
    btu = btu * 1000000

    btu = btu - (btu_per_panel * num_panels)

    return btu / 1000000 * price_df['data']
