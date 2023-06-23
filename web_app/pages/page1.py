from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go


# Incorporate data
df = pd.read_csv('train_churn.csv')

# Численные признаки
num_cols = ['ClientPeriod','MonthlySpending','TotalSpent']

# Категориальные признаки
cat_cols = ['Gender', 'IsSeniorCitizen', 'HasPartner', 'HasChild', 'HasPhoneService', 'HasMultiplePhoneNumbers','HasInternetService',
    'HasOnlineSecurityService', 'HasOnlineBackup', 'HasDeviceProtection','HasTechSupportAccess', 'HasOnlineTV', 'HasMovieSubscription',
    'HasContractPhone', 'IsBillingPaperless', 'PaymentMethod'
]

# App layout
layout = dbc.Container([
    dbc.Row([
        dcc.Markdown([
            '''
            Предсказание оттока клиентов – одна из важных практических задач машинного обучения. 
            Телеком компании используют разные алгоритмы и методы анализа данных для того, чтобы 
            удержать существующих клиентов, предложив им какие-то бонусы. 

            Проанализируем открытые данные и посмотрим, от чего может зависеть поведение абонента.
            '''
        ],
            className="app-markdown"
        ),
    ], className="row-with-markdown"),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardHeader('Распределение численных признаков'),
                    dbc.CardBody(
                        [
                            dbc.RadioItems(options=[{"label": x, "value": x} for x in num_cols],
                                value='ClientPeriod',
                                inline=True,
                                id='radio-buttons-final-num')
                        ],
                    )
                ],
                className="card-custom",
                style={'margin-top':'5px',
                       'margin-bottom':'50px'}
            )
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(data=df.to_dict('records'),
                                 page_size=12,
                                 style_table={'overflowX': 'auto'},
                                 style_cell={
                                     'font-family': 'Calibri Light',
                                     'font-size': '18px'
                                 })
        ], width=6),

        dbc.Col([
            dcc.Graph(figure={}, id='my-first-graph-final-num')
        ], width=6),
    ]),
    dbc.Row([
        dcc.Markdown(['''
            По распределениям числовых признаков видим, что:\n
            * Пользователи сразу понимают, что телеком компания им не подходит. Основная масса клиентов уходит через 1-10 месяцев пользования услугами.
            * Ежемесячный платеж больше у ушедших клиентов.
            * Размер трат в целом также больше у ушедших абонентов.
        '''], className="app-markdown"),
    ], className="row-with-markdown"),
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardHeader('Распределение категориальных признаков', className='cardheader-custom'),
                    dbc.CardBody(
                        [
                            dbc.RadioItems(options=[{"label": x, "value": x} for x in cat_cols],
                                           value='Gender',
                                           inline=True,
                                           id='radio-buttons-final-cat',
                                           className='form-check-inline',
                                           ),
                        ]
                    )
                ],
                className="card-custom",
            )
        ], width=6),
        dbc.Col([
            dcc.Graph(figure={}, id='my-first-graph-final-cat'),
        ], width=6),
    ]),
    dbc.Row([
        dcc.Markdown(['''
            По распределениям категориальных признаков заметны следующие закономерности:\n
            * Уходящие клиенты подключали меньше дополнительных услуг.
            * Уходящие клиенты предпочитали онлайн-оплату и счета.
            * Чаще всего уходящие клиенты – это пожилые граждане.
        '''], className="app-markdown"),
    ], className="row-with-markdown")
], fluid=True)

# Add controls to build the interaction
@callback(
    [Output(component_id='my-first-graph-final-num', component_property='figure'),
    Output(component_id='my-first-graph-final-cat', component_property='figure')],
    [Input(component_id='radio-buttons-final-num', component_property='value'),
    Input(component_id='radio-buttons-final-cat', component_property='value')]
)
def update_graph(num_chosen, cat_chosen):
    num_fig = px.histogram(df, x=num_chosen, marginal="box", color='Churn', title=f"\'{num_chosen}\' distribution")
    cat_fig = px.histogram(df, x=cat_chosen, color='Churn',title=f"\'{cat_chosen}\' proportion")
    return num_fig, cat_fig
