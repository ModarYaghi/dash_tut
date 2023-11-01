from dash import Dash, html, dcc


def render(app: Dash) -> html.Div:
    all_nations = ["South Korea", "China", "Canada"]
    return html.Div(
        children=[
            html.H6("Nation"),
            dcc.Dropdown(
                options=[{"label": nation, "value": nation} for nation in all_nations],
                value=all_nations,
                multi=True
            )
        ]
    )
