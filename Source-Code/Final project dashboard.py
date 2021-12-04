import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html
import pandas as pd
import plotly.offline as pyo
import urllib
import API_caller as api

stateList = [{'label': 'Alabama', 'value': 'AL'},
             {'label': 'Alaska', 'value': 'AK'},
             {'label': 'Arizona', 'value': 'AZ'},
             {'label': 'Arkansas', 'value': 'AR'},
             {'label': 'California', 'value': 'CA'},
             {'label': 'Colorado', 'value': 'CO'},
             {'label': 'Connecticut', 'value': 'CT'},
             {'label': 'Delaware', 'value': 'DE'},
             {'label': 'Washington DC', 'value': 'DC'},
             {'label': 'Florida', 'value': 'FL'},
             {'label': 'Georgia', 'value': 'GA'},
             {'label': 'Hawaii', 'value': 'HI'},
             {'label': 'Idaho', 'value': 'ID'},
             {'label': 'Illinois', 'value': 'IL'},
             {'label': 'Indiana', 'value': 'IN'},
             {'label': 'Iowa', 'value': 'IA'},
             {'label': 'Kansas', 'value': 'KS'},
             {'label': 'Kentucky', 'value': 'KY'},
             {'label': 'Louisiana', 'value': 'LA'},
             {'label': 'Maine', 'value': 'ME'},
             {'label': 'Maryland', 'value': 'MD'},
             {'label': 'Massachusetts', 'value': 'MA'},
             {'label': 'Michigan', 'value': 'MI'},
             {'label': 'Minnesota', 'value': 'MN'},
             {'label': 'Mississippi', 'value': 'MS'},
             {'label': 'Missouri', 'value': 'MO'},
             {'label': 'Montana', 'value': 'MT'},
             {'label': 'Nebraska', 'value': 'NE'},
             {'label': 'Nevada', 'value': 'NV'},
             {'label': 'New Hampshire', 'value': 'NH'},
             {'label': 'New Jersey', 'value': 'NJ'},
             {'label': 'New Mexico', 'value': 'NM'},
             {'label': 'New York', 'value': 'NY'},
             {'label': 'North Carolina', 'value': 'NC'},
             {'label': 'North Dakota', 'value': 'ND'},
             {'label': 'Ohio', 'value': 'OH'},
             {'label': 'Oklahoma', 'value': 'OK'},
             {'label': 'Oregon', 'value': 'OR'},
             {'label': 'Pennsylvania', 'value': 'PA'},
             {'label': 'Rhode Island', 'value': 'RI'},
             {'label': 'South Carolina', 'value': 'SC'},
             {'label': 'South Dakota', 'value': 'SD'},
             {'label': 'Tennessee', 'value': 'TN'},
             {'label': 'Texas', 'value': 'TX'},
             {'label': 'Utah', 'value': 'UT'},
             {'label': 'Vermont', 'value': 'VT'},
             {'label': 'Virginia', 'value': 'VA'},
             {'label': 'Washington', 'value': 'WA'},
             {'label': 'West Virginia', 'value': 'WV'},
             {'label': 'Wisconsin', 'value': 'WI'},
             {'label': 'Wyoming', 'value': 'WY'}]
yearList = [{'label': '1960', 'value': '1960'},
            {'label': '1961', 'value': '1961'},
            {'label': '1962', 'value': '1962'},
            {'label': '1963', 'value': '1963'},
            {'label': '1964', 'value': '1964'},
            {'label': '1965', 'value': '1965'},
            {'label': '1966', 'value': '1966'},
            {'label': '1967', 'value': '1967'},
            {'label': '1968', 'value': '1968'},
            {'label': '1969', 'value': '1969'},
            {'label': '1970', 'value': '1970'},
            {'label': '1971', 'value': '1971'},
            {'label': '1972', 'value': '1972'},
            {'label': '1973', 'value': '1973'},
            {'label': '1974', 'value': '1974'},
            {'label': '1975', 'value': '1975'},
            {'label': '1976', 'value': '1976'},
            {'label': '1977', 'value': '1977'},
            {'label': '1978', 'value': '1978'},
            {'label': '1979', 'value': '1979'},
            {'label': '1980', 'value': '1980'},
            {'label': '1981', 'value': '1981'},
            {'label': '1982', 'value': '1982'},
            {'label': '1983', 'value': '1983'},
            {'label': '1984', 'value': '1984'},
            {'label': '1985', 'value': '1985'},
            {'label': '1986', 'value': '1986'},
            {'label': '1987', 'value': '1987'},
            {'label': '1988', 'value': '1988'},
            {'label': '1989', 'value': '1989'},
            {'label': '1990', 'value': '1990'},
            {'label': '1991', 'value': '1991'},
            {'label': '1992', 'value': '1992'},
            {'label': '1993', 'value': '1993'},
            {'label': '1994', 'value': '1994'},
            {'label': '1995', 'value': '1995'},
            {'label': '1996', 'value': '1996'},
            {'label': '1997', 'value': '1997'},
            {'label': '1998', 'value': '1998'},
            {'label': '1999', 'value': '1999'},
            {'label': '2000', 'value': '2000'},
            {'label': '2001', 'value': '2001'},
            {'label': '2002', 'value': '2002'},
            {'label': '2003', 'value': '2003'},
            {'label': '2004', 'value': '2004'},
            {'label': '2005', 'value': '2005'},
            {'label': '2006', 'value': '2006'},
            {'label': '2007', 'value': '2007'},
            {'label': '2008', 'value': '2008'},
            {'label': '2009', 'value': '2009'},
            {'label': '2010', 'value': '2010'},
            {'label': '2011', 'value': '2011'},
            {'label': '2012', 'value': '2012'},
            {'label': '2013', 'value': '2013'},
            {'label': '2014', 'value': '2014'},
            {'label': '2015', 'value': '2015'},
            {'label': '2016', 'value': '2016'},
            {'label': '2017', 'value': '2017'},
            {'label': '2018', 'value': '2018'},
            {'label': '2019', 'value': '2019'}]

# Load csv into dataframe
df = pd.read_csv('C:/Users/jauga/PycharmProjects/Final_Prject/Database/Complete_SEDS_only_RC.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# navbar styling
NAVBAR_STYLE = {
    'position': 'fixed',
    'top': 80,
    'left': 0,
    'bottom': 20,
    'width': '18rem',
    'padding': '2rem 1rem',
    'background-color': '#FF6544'
}

# styling for content inside
CONTENT_STYLE = {
    'margin-left': '10rem',
    'margin-right': '0rem',
    'padding': '1rem 2rem',
    # 'background-color': '#FF6544'
}

navbar = dbc.Card([
    dbc.CardBody([
        html.H2("Navbar", className="display-4"),
        html.Hr(),
        html.P(
            "Select graphs here!", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("About", href='/', active='exact'),
                dbc.NavLink("Electricity Usage and Price", href='/page-1', active='exact'),
                dbc.NavLink("graph 2", href='/page-2', active='exact')
            ],
            horizontal='left',
            pills=True
        ),
    ]),
], style=NAVBAR_STYLE
)
content = dbc.Container(id='page-content', children=[], style=CONTENT_STYLE, fluid=True, className='main-spacing')

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1('Personal Solar Energy'),
            html.H2('A future that lasts longer than any other')
        ], width={'size': 9, 'offset': 2}, className='text-center text-white title-style')
    ]),

    dcc.Location(id='url'),
    dbc.Row([
        dbc.Col(navbar, width=2),
        dbc.Col(content, width=10, style={'margin-left': '9rem'})
    ])
], fluid=True)


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def render_page_content(pathname):
    # About page
    if pathname == '/':
        return [
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Introduction'),
                            html.P('As our world continues to advance technologically we threaten the '
                                   'environments around us, our advancements have caused our ecosystems '
                                   'around earth to rapidly deteriorate, the destruction of our home is '
                                   'primarily caused by our expulsion of CO2 into the atmosphere by burning '
                                   'fossil fuels. This tragic loss of biodiversity comes as a forewarning to '
                                   'the humans on earth; Our planet will not be able to sustain us under its '
                                   'current treatment. Our use of fossil fuels is amazing as we can see the '
                                   'accomplishments of humanity over the past 100 years, but should we '
                                   'continue to strive for progress using the means of such a destructive '
                                   'tool, we will not live to see what humanity can produce with our '
                                   'limitless potential.')
                        ])
                    ], className='card-style'),
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Our Data'),
                            html.P(
                                'Our data was acquired from the U.S. Energy Information Administration who is tasked '
                                'with conducting comprehensive data collection that covers the full spectrum of energy '
                                'sources, end uses, and energy flows. We have used their public API to acquire in '
                                'depth data about individual state production, consumption, and expenditure of '
                                'residential sector energy. With this we have developed several graphs to articulate '
                                'the need, and demonstrate the lack of usage, of solar panels.')
                            ])
                    ], className='card-spacing card-style')
                ], width={'size': 6}),
                dbc.Col([
                    dbc.Card([
                        dbc.CardImg(
                            src='https://coral.org/wp-content/uploads/2021/09/CoralReef_FrenchPolynesia-1024x681.jpg',
                            alt='Coral Reef from French Polynesia',
                            top=True),
                        dbc.CardBody(
                            html.P('Coral Reef located in French Polynesia')
                        )
                    ], className='card-style')
                ], width={'size': 6})
            ], justify='around'),
        ]
    # Line graph page
    elif pathname == '/page-1':
        return [
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(id='state-selector-dropdown',
                                 placeholder='State',
                                 options=stateList,
                                 className='text-dark',
                                 clearable=False,
                                 value='NC',
                                 style={'background-color': '#FF6544'})
                ], width={'size': 1, 'offset': 11}),

                dbc.Col([
                    html.H2('Electricity Consumption by Residential Sector', style={'textAlign': 'center'}),
                    dcc.Graph(id='line-graph1'),
                    html.Br(),
                    html.H2('Electricity Price in Residential Sector', style={'textAlign': 'center'}),
                    dcc.Graph(id='line-graph2')
                ], width={'size': 10, 'offset': 1})
            ])
        ]
    # Bar graph page
    elif pathname == '/page-2':
        return [
            dbc.Row([
                dbc.Col([
                    html.H2('Bar graph showing very cool data!', style={'textAlign': 'center'}),
                    dcc.Graph(id='bar-graph')
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Slider(id='year-selector-slider',
                               min=1989,
                               max=2019,
                               step=1,
                               value=2019,
                               className='blue-background',
                               marks={
                                   1989: {'label': "1989", 'style': {'color': '#FF6544'}},
                                   1990: {'label': "1990", 'style': {'color': '#FF6544'}},
                                   1995: {'label': "1995", 'style': {'color': '#FF6544'}},
                                   2000: {'label': "2000", 'style': {'color': '#FF6544'}},
                                   2005: {'label': "2005", 'style': {'color': '#FF6544'}},
                                   2010: {'label': "2010", 'style': {'color': '#FF6544'}},
                                   2015: {'label': "2015", 'style': {'color': '#FF6544'}},
                                   2019: {'label': "2019", 'style': {'color': '#FF6544'}}
                               })
                ])
            ])
        ]


@app.callback(
    [Output('line-graph1', 'figure'),
     Output('line-graph2', 'figure')],
    [Input('state-selector-dropdown', 'value')]
)
def update_figure(selectedState):
    filtered_df1 = api.create_pd_df('ESRCB')
    filtered_df1 = filtered_df1[filtered_df1['State'] == selectedState]

    filtered_df2 = df[df['state'] == selectedState]
    filtered_df2 = filtered_df2[filtered_df2['MSN'] == 'ESRCD']

    line_graph_data1 = [
        go.Scatter(x=filtered_df1['Year'], y=filtered_df1['data'], mode='lines', marker={'color': '#483CA2'})]
    line_graph_data2 = [
        go.Scatter(x=filtered_df2['Year'], y=filtered_df2['data'], mode='lines', marker={'color': '#483CA2'})]
    return [{'data': line_graph_data1,
             'layout': go.Layout(title='Electricity Consumed by the residential sector of ' + selectedState,
                                 xaxis={'title': 'Year'},
                                 yaxis={'title': 'Billion BTU'})},
            {'data': line_graph_data2,
             'layout': go.Layout(title='Electricity price in the residential sector of ' + selectedState,
                                 xaxis={'title': 'Year'},
                                 yaxis={'title': 'Dollars per Million BTU'})
             }]


@app.callback(
    Output('bar-graph', 'figure'),
    Input('year-selector-slider', 'value')
)
def update_figure(selectedYear):
    filtered_df1 = df[df['Year'] == selectedYear]
    filtered_df1 = filtered_df1[filtered_df1['MSN'] == 'SORCB']

    bar_graph_data = [go.Bar(x=filtered_df1['state'], y=filtered_df1['data'])]
    return {'data': bar_graph_data,
            'layout': go.Layout(title='Residential Solar Energy Consumed by State in ',
                                xaxis={'title': 'State'},
                                yaxis={'title': 'Billion Btu'})}


if __name__ == '__main__':
    app.run_server()
