import dash
import dash_bootstrap_components as dbc
import numpy as np
import plotly.graph_objs as go
from dash import Input, Output, dcc, html, State
import pandas as pd
import plotly.offline as pyo
import urllib
import API_caller as api
import ConversionCalc as calc

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

# Prepare Data
df = pd.read_csv('C:/Users/jauga/PycharmProjects/Final_Prject/Database/Complete_SEDS_only_RC.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# navbar styling
NAVBAR_STYLE = {
    'position': 'fixed',
    'top': 80,
    'left': 0,
    'bottom': 0,
    'width': '18rem',
    'padding': '2rem 1rem',
    'background-color': '#FF6544'
}

# styling for content inside
CONTENT_STYLE = {
    'margin-left': '10rem',
    'margin-right': '0rem',
    'padding': '1rem 2rem'
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
                dbc.NavLink("graph 2", href='/page-2', active='exact'),
                dbc.NavLink("graph 3", href='/page-3', active='exact'),
                dbc.NavLink("graph 4", href='/page-4', active='exact')
            ],
            horizontal='left',
            pills=True
        ),
    ]),
], style=NAVBAR_STYLE
)
content = dbc.Container(id='page-content', children=[], style=CONTENT_STYLE, className='main-spacing', fluid=True)

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
                    ], className='card-style card-spacing')
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
                    ], className='card-style'),
                ], width={'size': 5, 'offset': 0}),
            ], className='row-spacing'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('How much would you save?', className='text-white'),
                            html.P('Enter your yearly power bill and see how much only 4 solar panels could save you!',
                                   className='text-white'),
                            dcc.Textarea(id='calc-text', className='blue-background text-light'),
                            html.Br(),
                            dbc.Button(id='update-calc-card', className='calc-button-style text-dark',
                                       children='Calculate!'),
                            html.Br(),
                            html.H2(id='calc-output')

                        ], className='text-center')
                    ], className='card-style calc-spacing text-dark')
                ], width={'size': 6}),
            ], className='row-spacing row-spacing-vertical')
        ]

    # Line graph page
    elif pathname == '/page-1':
        content._ = 'main-spacing-linegraph'
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
                    dbc.Card([
                        dbc.CardBody([
                            html.H2('Electricity Consumption by Residential Sector', style={'textAlign': 'center'}),
                            dcc.Graph(id='line-graph1')
                        ]),
                    ], className='graph-style'),
                    html.Br(),
                    dbc.Card([
                        dbc.CardBody([
                            html.H2('Electricity Price in Residential Sector', style={'textAlign': 'center'}),
                            dcc.Graph(id='line-graph2')
                        ])
                    ], className='graph-style')
                ], width={'size': 10, 'offset': 1})
            ])
        ]

    # Bar graph page
    elif pathname == '/page-2':
        return [
            dbc.Row([
                dbc.Col([
                    html.H2('stackedbargraph', style={'textAlign': 'center'}),
                    dcc.Graph(id='stackedbar-graph')
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Slider(id='year-selector-slider',
                               min=1960,
                               max=2019,
                               step=1,
                               value=2019,
                               className='blue-background',
                               marks={
                                   1960: {'label': "1960", 'style': {'color': '#FF6544'}},
                                   1965: {'label': "1965", 'style': {'color': '#FF6544'}},
                                   1970: {'label': "1970", 'style': {'color': '#FF6544'}},
                                   1975: {'label': "1975", 'style': {'color': '#FF6544'}},
                                   1980: {'label': "1980", 'style': {'color': '#FF6544'}},
                                   1985: {'label': "1985", 'style': {'color': '#FF6544'}},
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


    elif pathname == '/page-3':

        return [
            dbc.Row([

                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2('Renewable Energy/Natural Gas Production per State Population'
                                    , style={'textAlign': 'center'}),
                            dcc.Graph(id='bubble-chart')])
                    ], className='graph-style')
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            dcc.Slider(id='year-selector-slider2',
                                       min=1960,
                                       max=2019,
                                       step=1,
                                       value=2019,
                                       className='slider-style',
                                       marks={
                                           1960: {'label': "1960", 'style': {'color': '#FF6544'}},
                                           1965: {'label': "1965", 'style': {'color': '#FF6544'}},
                                           1970: {'label': "1970", 'style': {'color': '#FF6544'}},
                                           1975: {'label': "1975", 'style': {'color': '#FF6544'}},
                                           1980: {'label': "1980", 'style': {'color': '#FF6544'}},
                                           1985: {'label': "1985", 'style': {'color': '#FF6544'}},
                                           1990: {'label': "1990", 'style': {'color': '#FF6544'}},
                                           1995: {'label': "1995", 'style': {'color': '#FF6544'}},
                                           2000: {'label': "2000", 'style': {'color': '#FF6544'}},
                                           2005: {'label': "2005", 'style': {'color': '#FF6544'}},
                                           2010: {'label': "2010", 'style': {'color': '#FF6544'}},
                                           2015: {'label': "2015", 'style': {'color': '#FF6544'}},
                                           2019: {'label': "2019", 'style': {'color': '#FF6544'}}
                                       })
                        ])
                    ], className='slider-style')
                ])
            ])
        ]

    elif pathname == '/page-4':
        filtered_df1 = api.create_pd_df('NGRCB')
        filtered_df1 = filtered_df1[filtered_df1['Year'] == '2019']

        heatmap_data = [go.Heatmap(x=filtered_df1['State'],
                                   y=filtered_df1['data'],
                                   z=filtered_df1['MSN'].values.tolist(),
                                   colorscale='Jet')]
        return [
            dbc.Row([
                dbc.Col([
                    html.H2('A Heatmap that shows information for Natural Gas', style={'textAlign': 'left'}),
                    dcc.Graph(id='heat-map', figure={'data': heatmap_data,
                                                     'layout': go.Layout(title='Residential Coal Used ',
                                                                         xaxis={'title': 'State'},
                                                                         yaxis={'title': 'Energy'},
                                                                         )}),

                ])
            ]),

        ]


# callback for linegraphs
@app.callback(
    [Output('line-graph1', 'figure'),
     Output('line-graph2', 'figure')],
    [Input('state-selector-dropdown', 'value')]
)
def update_figure(selectedState):
    line_graph_data1 = api.create_pd_df('ESRCB')
    line_graph_data2 = api.create_pd_df('ESRCD')

    line_graph_data1 = line_graph_data1[line_graph_data1['State'] == selectedState]
    line_graph_data2 = line_graph_data2[line_graph_data2['State'] == selectedState]

    line_graph_data1 = [
        go.Scatter(x=line_graph_data1['Year'], y=line_graph_data1['data'], mode='lines', marker={'color': '#483CA2'})]
    line_graph_data2 = [
        go.Scatter(x=line_graph_data2['Year'], y=line_graph_data2['data'], mode='lines', marker={'color': '#483CA2'})]
    return [{'data': line_graph_data1,
             'layout': go.Layout(title='Electricity Consumed by the residential sector of ' + selectedState,
                                 xaxis={'title': 'Year'},
                                 yaxis={'title': 'Billion BTU'})},
            {'data': line_graph_data2,
             'layout': go.Layout(title='Electricity price in the residential sector of ' + selectedState,
                                 xaxis={'title': 'Year'},
                                 yaxis={'title': 'Dollars per Million BTU'})
             }]


# callback for bargraphs
@app.callback(
    Output('stackedbar-graph', 'figure'),
    Input('year-selector-slider', 'value')
)
def update_figure(selectedYear):
    trace_1_data = api.create_pd_df('CLRCB')
    trace_2_data = api.create_pd_df('PARCP')
    trace_3_data = api.create_pd_df('NGRCB')
    trace_4_data = api.create_pd_df('SORCB')

    trace_1_data = trace_1_data[trace_1_data['Year'] == str(selectedYear)]
    trace_2_data = trace_2_data[trace_2_data['Year'] == str(selectedYear)]
    trace_3_data = trace_3_data[trace_3_data['Year'] == str(selectedYear)]
    trace_4_data = trace_4_data[trace_4_data['Year'] == str(selectedYear)]

    trace_1_data = trace_1_data.groupby(['State']).agg(
        {'data': 'sum'}).reset_index()
    trace_2_data = trace_2_data.groupby(['State']).agg(
        {'data': 'sum'}).reset_index()
    trace_3_data = trace_3_data.groupby(['State']).agg(
        {'data': 'sum'}).reset_index()
    trace_4_data = trace_4_data.groupby(['State']).agg(
        {'data': 'sum'}).reset_index()

    trace1 = go.Bar(
        x=trace_1_data['State'],
        y=trace_1_data['data'],
        name='Coal',
        marker={'color': 'Black'})

    trace2 = go.Bar(
        x=trace_2_data['State'],
        y=trace_2_data['data'],
        name='Petroleum',
        marker={'color': 'grey'})

    trace3 = go.Bar(
        x=trace_3_data['State'],
        y=trace_3_data['data'],
        name='Natural Gas',
        marker={'color': 'blue'})

    trace4 = go.Bar(
        x=trace_4_data['State'],
        y=trace_4_data['data'],
        name='Solar Energy',
        marker={'color': 'orange'})

    stackedbar_graph_data = [trace1, trace2, trace3, trace4]

    return {'data': stackedbar_graph_data,
            'layout': go.Layout(title='Residential Solar Energy Consumed by State in ' + str(selectedYear),
                                showlegend=True,
                                barmode='stack',
                                xaxis={'categoryorder': 'category descending'},
                                yaxis={'title': 'Energy usage'})}


# callback for about page button
@app.callback(
    [Output('calc-output', 'children')],
    [Input('update-calc-card', 'n_clicks')],
    [State('state-selector-dropdown', 'value'),
     State('calc-text', 'value')]
)
def update_calc(n_clicks, state, money):
    print('WE GOT CLICKED')
    if (n_clicks > 1):
        print(n_clicks)
    return ['You Saved ']


@app.callback(
    Output('bubble-chart', 'figure'),
    Input('year-selector-slider2', 'value')
)
def update_figure(selectedYear):
    bubble_Graph_Data1 = api.create_pd_df('NGMPB')
    bubble_Graph_Data2 = api.create_pd_df('REPRB')
    bubble_Graph_Data3 = api.create_pd_df('TPOPP')

    bubble_Graph_Data1 = bubble_Graph_Data1[bubble_Graph_Data1['Year'] == str(selectedYear)]
    bubble_Graph_Data2 = bubble_Graph_Data2[bubble_Graph_Data2['Year'] == str(selectedYear)]
    bubble_Graph_Data3 = bubble_Graph_Data3[bubble_Graph_Data3['Year'] == str(selectedYear)]

    bubble_chart_data = [go.Scatter(x=bubble_Graph_Data2['data'],
                                    y=bubble_Graph_Data1['data'],
                                    text=bubble_Graph_Data1['State'],
                                    mode='markers',
                                    marker=dict(size=bubble_Graph_Data3['data'] / 100,
                                                color=bubble_Graph_Data1['data'] / 30000,
                                                colorscale="temps",
                                                showscale=True),
                                    )]
    return {'data': bubble_chart_data,
            'layout': go.Layout(title='Renewable Energy/Natural Gas Production per State Population '
                                      + str(selectedYear),
                                xaxis={'title': 'Renewable Energy'},
                                yaxis={'title': 'Natural Gas'},
                                height=750)}


if __name__ == '__main__':
    app.run_server()
