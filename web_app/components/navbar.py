from dash import html
import dash_bootstrap_components as dbc


def Navbar():
    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Get prediction", href="/page2"))
            ],
            brand=html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/telephone-outbound.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Telecom Churn Analytics", className="ms-2")),
                    ],
                    align="center",
                    className="g-0"
                ),
                href="/page1",
                style={"textDecoration": "none"},
            ),
            color="primary",
            dark=True,
        )
    ])
    return layout
