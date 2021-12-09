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
df = pd.read_csv('C:/Users/cahun/PycharmProjects/FinalProject/Database/Complete_SEDS_only_RC.csv')

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
    'padding': '1rem 2rem'
    # 'background-color': '#FF6544'
}

navbar = dbc.Card([
    dbc.CardBody([
        html.H2("Navbar", className="display-4"),
        html.Hr(),
        html.P(
            "Select pages here!", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("About", href='/', active='exact'),
                dbc.NavLink("Electricity trends", href='/page-1', active='exact'),
                dbc.NavLink("Comparison of energy sources", href='/page-2', active='exact'),
                dbc.NavLink("Energy source prices", href='/page-3', active='exact'),
                dbc.NavLink("Electricity expenditure vs solar energy usage", href='/page-4', active='exact'),
                dbc.NavLink("Learn more", href='/page-5', active='exact')
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
            html.H1('Solar Savings'),
            html.H2('A Future That Lasts Longer Than Any Other!')
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
                ], width={'size': 6, 'offset': 0}),
            ], className='row-spacing'),
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
                                 style={'background-color': '#FF6544'}),
                    html.Br()
                ], width={'size': 2, 'offset': 10})
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2('Electricity Usage', style={'textAlign': 'center'}),
                            dcc.Graph(id='line-graph1')
                        ]),
                    ], className='graph-style'),
                    html.Br(),
                ], width={'size': 10, 'offset': 0}),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Usage Graph', className='text-center'),
                            html.P('In this graph we can see over time the steady increase of the usage of '
                                   'electricity, this trend has been recognized by many different groups and is sure '
                                   'to continue as we move forward developing new technology.')
                        ])
                    ], className='card-style card-spacing')
                ])
            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2('Electricity Price', style={'textAlign': 'center'}),
                            dcc.Graph(id='line-graph2')
                        ])
                    ], className='graph-style'),
                ], width={'size': 10, 'offset': 0, 'order': 2}),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Price Graph', className='text-center'),
                            html.P('In this graph we can see over time the steady increase of the price of '
                                   'electricity, when observed individually it only makes sense that as the demand '
                                   'increases so does the price however, paired with the graph above we can see how '
                                   'our future will see paying more money for more energy as both have experienced this'
                                   ' trend.')
                        ])
                    ], className='card-style card-spacing')
                ], width={'size': 2, 'offset': 0, 'order': 1})
            ])
        ]

    # Bar graph page
    elif pathname == '/page-2':
        return [
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Consumption Chart', className='text-center'),
                            html.P(
                                'This chart displays a comparison of some of the most commonly utilized energy sources, In it '
                                'we can see just how under utilized solar energy is in residential homes and '
                                'businesses. The primary energy source for homes is natural gas, and as seen '
                                'before the cost of using is unsustainable, if this pattern continues ultimatley '
                                'we will see the inability for people to have the electricity needed to power '
                                'their homes.')
                        ])
                    ], className='card-style'),
                    html.Br()
                ], width={'size': 8, 'offset': 2})
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2('Energy Used from Different Energy Sources', style={'textAlign': 'center'}),
                            dcc.Graph(id='stackedbar-graph')
                        ])
                    ], className='graph-style')
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dcc.Slider(id='year-selector-slider',
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
                    ], className='slider-style')
                ], width={'size': 10, 'offset': 1})
            ])
        ]

    # Muliline graph
    elif pathname == '/page-3':
        return [
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('MultiLine Chart', className='text-center'),
                            html.P('Below is a multi line chart comparing a given state\'s natural gas, '
                                   'petroleum, and kerosene prices. We can see that overtime the prices of each '
                                   'of these fossil fuels have continuously increased, seeing this we can understand '
                                   'that as the fossil fuels get used up and earth\'s supply dwindles these prices will '
                                   'only continue to rise. As these resources continue to become more expensive '
                                   'people will look for alternatives like solar energy as the way to cheaply acquire '
                                   'electricity. While these prices trend up, the price of solar energy continues to decrease as '
                                   'installing panels becomes cheaper and the returns from solar panels is '
                                   'absolutely free every year!')
                        ])
                    ], className='card-style'),
                    html.Br()
                ], width={'size': 10, 'offset': 1})
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Dropdown(id='state-selector-dropdown2',
                                 placeholder='State',
                                 options=stateList,
                                 className='text-dark',
                                 clearable=False,
                                 value='NC',
                                 style={'background-color': '#FF6544', 'margin-bottom': '1rem', 'margin-right': '1rem',
                                        'margin-top': '1rem'})
                ], width={'size': 2, 'offset': 10})
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2(
                                'Price\'s of Different Energy Sources',
                                style={'textAlign': 'center'}),
                            dcc.Graph(id='multiline-graph')
                        ])
                    ], className='graph-style')

                ])
            ]),

        ]

    # bubble chart
    elif pathname == '/page-4':
        return [
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Bubble Chart', className='text-center'),
                            html.H5('In the bubble chart below the height of the bubble is determined by how much '
                                    'each state spent on electricity, while the x-axis shows the population of each '
                                    'state. The size of each bubble is that states total solar energy usage.',
                                    className='text-center'),
                            html.P('This comparison shows us that despite california having a larger population than '
                                   'Texas, California spent less in the year 2019 on purchasing energy, '
                                   'this corelation likely has many more points to it however, the amount of solar '
                                   'energy that California produces (as seen in the stacked bar chart) shows that '
                                   'their way of producing energy for home owners is ultimately cheaper.',
                                   style={'margin-top': '2rem'})
                        ])
                    ], className='card-style'),
                    html.Br()
                ], width={'size': 10, 'offset': 1})
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2('Comparison of expenditure to state population and consumption of Solar energy'
                                    , style={'textAlign': 'center'}),
                            dcc.Graph(id='bubble-chart')])
                    ], className='graph-style', )
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
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
                    ], className='slider-style')
                ], width={'size': 10, 'offset': 1})
            ])
        ]

    # learn more!
    elif pathname == '/page-5':
        return [
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H3('What can we do?'),
                            html.P(
                                'Seeing the persistent rise of prices and consumption can leave you feeling like the end is already here. How can someone avoid the inevitable cost of energy as we march forward, and how can we prevent more damage to the environment?'),
                            html.H4('Install Solar Panels!'),
                            html.P(
                                'Installing solar panels is the best way for you to reduce your usage of fossil fuels as a means to power your home and save money longterm as prices continue to increase. Solar panels return energy straight back into your home, and once set up they pay for themselves and more overtime. By swapping to solar energy you could save money every year on your power bill by producing the energy yourself! This way we save on both cash and CO2 emissions')
                        ])
                    ], className='card-style')
                ], width={'size': 10}),

            ]),

            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H2('How much would you save?', className='text-white'),
                            html.P(
                                'Select your state, enter your yearly power bill on the left and enter the number of solar panels you\'d want on the right and see how much you could save!',
                                className='text-white'),
                            dcc.Dropdown(id='state-selector-dropdown2',
                                         placeholder='State',
                                         options=stateList,
                                         className='text-dark',
                                         clearable=False,
                                         value='NC',
                                         style={'background-color': '#FF6544'}),
                            dcc.Textarea(id='calc-text', className='blue-background text-white textbox-style'),
                            dcc.Textarea(id='solar-text',
                                         className='blue-background text-white textbox-style textbox-spacing'),
                            html.Br(),
                            html.Button(id='update-calc-card', className='calc-button-style text-dark',
                                        children='Calculate!'),
                            html.Br(),
                            html.H4(id='calc-output', className='text-white'),
                            html.H4(id='calc-output2', className='text-white')

                        ], className='text-center')
                    ], className='card-style calc-spacing text-dark')
                ], width={'size': 4, 'offset': 0}),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H3('Wanna know more?'),
                            html.P('Transitioning our world to solar energy is a complicated process that will take a lot of time, but if you\'re interested in getting ahead of everyone else, you can learn more by clicking the button below!')
                        ]),
                            dbc.Button('Learn More!', href= 'https://www.energysage.com/solar-panels/nc/', className='blue-background', style={'margin-top': '2rem'})
                    ], className='card-style', style={'margin-top': '4rem'})
                ], width={'size': 2, 'offset': 0}),
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Iframe(width="650", height="450", src="https://www.youtube.com/embed/HJYEKrIRGNE",
                                        title="YouTube video player",
                                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture")
                        ])
                    ], className='card-style', style={'margin-left': '4rem', 'width': '680px', 'margin-top': '1rem'})
                ], width={'size': 5, 'offset': 0})
            ])
        ]


# CALLBACKS

# callback for linegraph
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
             'layout': go.Layout(title='Electricity Consumed by ' + selectedState,
                                 xaxis={'title': 'Year'},
                                 yaxis={'title': 'Billion BTU'})},
            {'data': line_graph_data2,
             'layout': go.Layout(title='Electricity price in ' + selectedState,
                                 xaxis={'title': 'Year'},
                                 yaxis={'title': 'Dollars per Million BTU'})
             }]


# callback for bargraph
@app.callback(
    Output('stackedbar-graph', 'figure'),
    Input('year-selector-slider', 'value')
)
def update_figure(selectedYear):
    trace_1_data = api.create_pd_df('NGRCB')
    trace_2_data = api.create_pd_df('PARCP')
    trace_3_data = api.create_pd_df('SORCB')
    trace_4_data = api.create_pd_df('KSRCB')

    trace_1_data = trace_1_data[trace_1_data['Year'] == str(selectedYear)]
    trace_2_data = trace_2_data[trace_2_data['Year'] == str(selectedYear)]
    trace_3_data = trace_3_data[trace_3_data['Year'] == str(selectedYear)]
    trace_4_data = trace_4_data[trace_4_data['Year'] == str(selectedYear)]

    trace1 = go.Bar(
        x=trace_1_data['State'],
        y=trace_1_data['data'],
        name='Natural Gas',
        marker={'color': 'blue'})

    trace2 = go.Bar(
        x=trace_2_data['State'],
        y=trace_2_data['data'],
        name='Petroleum',
        marker={'color': 'green'})

    trace3 = go.Bar(
        x=trace_3_data['State'],
        y=trace_3_data['data'],
        name='Solar Energy',
        marker={'color': 'orange'})

    trace4 = go.Bar(
        x=trace_4_data['State'],
        y=trace_4_data['data'],
        name='Kerosene',
        marker={'color': 'crimson'}, )

    stackedbar_graph_data = [trace1, trace2, trace3, trace4]

    return {'data': stackedbar_graph_data,
            'layout': go.Layout(title='Energy Resources Consumed by State in ' + str(selectedYear),
                                showlegend=True,
                                barmode='stack',
                                xaxis={'title': 'Energy usage', 'categoryorder': 'total descending'},
                                yaxis={'title': 'Billion BTU'})}


# callback for calc button
@app.callback(Output('calc-output', 'children'),
              Output('calc-output2', 'children'),
              Input('update-calc-card', 'n_clicks'),
              State('calc-text', 'value'),
              State('solar-text', 'value'),
              State('state-selector-dropdown2', 'value'))
def update_calc(n_clicks, text, panels, state):
    if type(text) is None:
        return
    elif str.isnumeric(text) == 0 or str.isnumeric(panels) == 0:
        return ['whoops, that is not a number']
    else:
        x = float(text)
        y = calc.cost_converter(state, int(text), int(panels))
        z = np.round(x - y, decimals=2)
        return ['Your new bill could be ' + str(calc.cost_converter(state, int(text), int(panels))) + ' per year!',\
               'Saving you ' + str(z) + ' per year!']


# callback for bubble chart
@app.callback(
    Output('bubble-chart', 'figure'),
    Input('year-selector-slider2', 'value')
)
def update_figure(selectedYear):
    print('callback')
    bubble_Graph_Data1 = api.create_pd_df('ESRCV')
    bubble_Graph_Data2 = api.create_pd_df('TPOPP')
    bubble_Graph_Data3 = api.create_pd_df('SORCB')

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
            'layout': go.Layout(title='Comparison of state expenditure to population and consumption of Solar energy '
                                      + str(selectedYear),
                                xaxis={'title': 'Thousand people'},
                                yaxis={'title': 'Million Dollars'},
                                height=750)}


# call back for multi line
@app.callback(
    Output('multiline-graph', 'figure'),
    Input('state-selector-dropdown2', 'value')
)
def update_figure(selectedState):
    trace_1_data = api.create_pd_df('PARCD')
    trace_2_data = api.create_pd_df('KSRCD')
    trace_3_data = api.create_pd_df('NGRCD')

    trace_1_data = trace_1_data[trace_1_data['State'] == str(selectedState)]
    trace_2_data = trace_2_data[trace_2_data['State'] == str(selectedState)]
    trace_3_data = trace_3_data[trace_3_data['State'] == str(selectedState)]

    trace1 = go.Scatter(x=trace_1_data['Year'], y=trace_1_data['data'], mode='lines', name='Petroleum')
    trace2 = go.Scatter(x=trace_2_data['Year'], y=trace_2_data['data'], mode='lines', name='Kerosene')
    trace3 = go.Scatter(x=trace_3_data['Year'], y=trace_3_data['data'], mode='lines', name='Natural Gas')
    data_multiline = [trace1, trace2, trace3]

    return {'data': data_multiline,
            'layout': go.Layout(title='Prices of Petroleum, Kerosene, and Natural gas in ' + selectedState,
                                xaxis={'title': 'Year'},
                                yaxis={'title': 'Dollars per million BTU'})}


if __name__ == '__main__':
    app.run_server()
