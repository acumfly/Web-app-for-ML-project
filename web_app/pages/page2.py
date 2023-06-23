from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
import catboost
import joblib

df = pd.read_csv('C:/Users/Анастасия/PycharmProjects/web_app/train_churn.csv')


# App layout
layout = dbc.Container([
    dbc.Row([
        html.Div(html.H5('Введите данные о клиенте:'),
                 style={'padding': '5px',
                        'margin-top': '15pt',
                        'margin-bottom': '5pt',
                        'margin-left': '15pt',
                        'margin-right':'15pt'}
                 )
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(['Персональная информация:'],
                     className='features-title'
                     ),
            html.Div(
                children=([
                    html.Div(children="Gender", className="menu-title"),
                    dcc.Dropdown(
                        id="Gender-ans",
                        options=[
                            {"label":ans, "value":ans}
                            for ans in np.sort(df.Gender.unique())
                        ],
                        value="Female",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                    html.Div(children="Is Senior Citizen", className="menu-title"),
                    dcc.Dropdown(
                        id="IsSeniorCitizen-ans",
                        options=[
                            {"label":ans, "value":ans}
                            for ans in np.sort(df.IsSeniorCitizen.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                    html.Div(children="Has Partner", className="menu-title"),
                    dcc.Dropdown(
                        id="Partner-ans",
                        options=[
                            {"label":ans, "value":ans}
                            for ans in np.sort(df.HasPartner.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                    html.Div(children="Has Child", className="menu-title"),
                    dcc.Dropdown(
                        id="Child-ans",
                        options=[
                            {"label":ans, "value":ans}
                            for ans in np.sort(df.HasChild.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                    html.Div(children="Has Contract Phone", className="menu-title"),
                    dcc.Dropdown(
                        id="ContractPhone-ans",
                        options=[
                            {"label":ans, "value":ans}
                            for ans in np.sort(df.HasContractPhone.unique())
                        ],
                        value="Month-to-month",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                    html.Div(children="Billing is Paperless", className="menu-title"),
                    dcc.Dropdown(
                        id="Billing-ans",
                        options=[
                            {"label":ans, "value":ans}
                            for ans in np.sort(df.IsBillingPaperless.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                    html.Div(children="Payment Method", className="menu-title"),
                    dcc.Dropdown(
                        id="PaymentMethod-ans",
                        options=[
                            {"label":ans, "value":ans}
                            for ans in np.sort(df.PaymentMethod.unique())
                        ],
                        value='Bank transfer (automatic)',
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                ]),
            )
        ]),
        dbc.Col([
            html.Div(['Интернет обслуживание:'],
                     className='features-title'
                     ),
            html.Div(
                children=([
                    html.Div(children="Has Internet Service", className="menu-title"),
                    dcc.Dropdown(
                        id="InternetService-ans",
                        options=[
                            {"label": ans, "value": ans}
                            for ans in np.sort(df.HasInternetService.unique())
                        ],
                        value="DSL",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                    html.Div(children="Has Online Security Service", className="menu-title"),
                    dcc.Dropdown(
                        id="OnlineSec-ans",
                        options=[
                            {"label": ans, "value": ans}
                            for ans in np.sort(df.HasOnlineSecurityService.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                    html.Div(children="Has Online Backup", className="menu-title"),
                    dcc.Dropdown(
                        id="OnlineBack-ans",
                        options=[
                            {"label": ans, "value": ans}
                            for ans in np.sort(df.HasOnlineBackup.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    )
                ]),
            ),
            html.Div('Телефонное обслуживание:',
                     style={'margin-top': '10pt'},
                     className='features-title'
                     ),
            html.Div(
                children=([
                    html.Div(children="Has Phone Service", className="menu-title"),
                    dcc.Dropdown(
                        id="PhoneService-ans",
                        options=[
                            {"label": ans, "value": ans}
                            for ans in np.sort(df.HasPhoneService.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                    html.Div(children="Has Multiple Phone Numbers", className="menu-title"),
                    dcc.Dropdown(
                        id="MultNumbers-ans",
                        options=[
                            {"label": ans, "value": ans}
                            for ans in np.sort(df.HasMultiplePhoneNumbers.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                ]),
            )
        ]),
        dbc.Col([
        html.Div(['ТВ:'], className='features-title'),
            html.Div(
                children=([
                    html.Div(children="Has Online TV", className="menu-title"),
                    dcc.Dropdown(
                        id="OnlineTV-ans",
                        options=[
                            {"label": ans, "value": ans}
                            for ans in np.sort(df.HasOnlineTV.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                    html.Div(children="Has Movie Subscription", className="menu-title"),
                    dcc.Dropdown(
                        id="MovieSubscription-ans",
                        options=[
                            {"label": ans, "value": ans}
                            for ans in np.sort(df.HasMovieSubscription.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                ]),
                # style={"display": "flex", "flex-wrap": "wrap", "align-items": "center"}
            ),
            html.Div(
                children=([
                    html.Div(['Поддержка:'],
                     className='features-title'
                     ),
                    html.Div(children="Has Device Protection", className="menu-title"),
                    dcc.Dropdown(
                        id="DeviceProtection-ans",
                        options=[
                            {"label": ans, "value": ans}
                            for ans in np.sort(df.HasDeviceProtection.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                    html.Div(children="Has Tech Support Access", className="menu-title"),
                    dcc.Dropdown(
                        id="TechSupport-ans",
                        options=[
                            {"label": ans, "value": ans}
                            for ans in np.sort(df.HasTechSupportAccess.unique())
                        ],
                        value="No",
                        clearable=False,
                        className="dropdown",
                        style={'textOverflow': 'ellipsis', 'whiteSpace': 'nowrap'}
                    ),
                ]),
                style={"margin-top":'55pt'}
            ),
        ]),
    ]),
    dbc.Row([
        html.Div([
            html.Div(
                children=([
                    html.Div(children="Client Period", className="menu-title"),
                    dcc.Input(
                        id="ClientPeriod-ans", type="number",
                        debounce=True, placeholder="months", value=0
                    )
                ])
            ),
            html.Div(
                children=([
                    html.Div(children="Monthly Spending", className="menu-title"),
                    dcc.Input(
                        id="MonthlySpending-ans", type="number",
                        debounce=True, value=0
                    )
                ]),
            ),
            html.Div(
                children=([
                    html.Div(children="Total Spent", className="menu-title"),
                    dcc.Input(
                        id="TotalSpent-ans", type="number",
                        debounce=True, value=0
                    )
                ]),
            ),
            html.Div([
                dbc.Button("Вероятность ухода", id='PredictButton', n_clicks=0, color="primary", size="sm"),
            ], style={'margin-top': '15pt'}),
            html.Span(id="Predict-val", style={"verticalAlign": "middle", 'margin-top': '15pt'})
        ], style={"display": "flex", "flex-wrap": "wrap", "align-items": "center", "gap": "10px", "margin-top":"17pt"}),
    ])
])

@callback(
    Output("Predict-val", 'children'),
    Input('PredictButton', 'n_clicks'),
    [State("ClientPeriod-ans", "value"),
    State("MonthlySpending-ans", "value"),
    State("TotalSpent-ans", "value"),
    State("Gender-ans", "value"),
    State("IsSeniorCitizen-ans", "value"),
    State("Partner-ans", "value"),
    State("Child-ans", "value"),
    State("PhoneService-ans", "value"),
    State("MultNumbers-ans", "value"),
    State("InternetService-ans", "value"),
    State("OnlineSec-ans", "value"),
    State("OnlineBack-ans", "value"),
    State("DeviceProtection-ans", "value"),
    State("TechSupport-ans", "value"),
    State("OnlineTV-ans", "value"),
    State("MovieSubscription-ans", "value"),
    State("ContractPhone-ans", "value"),
    State("Billing-ans", "value"),
    State("PaymentMethod-ans", "value")],
)

def get_inputs(n_clicks, *args):
    if n_clicks==0:
        return ""
    model = joblib.load("C:/Users/Анастасия/PycharmProjects/web_app/CB_trained.sav")
    X = []
    for arg in args:
        X.append(arg)
    preds = model.predict_proba(X)
    return np.around(preds[1], 2)

