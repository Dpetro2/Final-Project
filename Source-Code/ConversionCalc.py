import numpy as np
import API_caller as api


def cost_converter(state, money, panels):

    price_df = api.create_pd_df('TERCD')
    price_df = price_df[price_df['Year'] == '2019']
    price_df = price_df[price_df['State'] == state]

    return float(np.round(convert_dollar_to_btu(money, panels, price_df), decimals=2))


def convert_dollar_to_btu(dollars, num_panels, price_df):
    btu = dollars / price_df['data']
    btu_per_panel = 1706000
    btu = btu * 1000000

    btu = btu - (btu_per_panel * num_panels)

    return btu / 1000000 * price_df['data']

