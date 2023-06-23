import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,
                external_stylesheets=[dbc.themes.LUX, '/assets/custom.css'],
                meta_tags=[{"name": "viewport", "content": "width=device-width"}],
                suppress_callback_exceptions=True)

app.title = 'Telecom churn'
app._favicon = ('phone-vibrate.png')