"""
Multiple Row Selection - without check boxes.  Use shift click or ctr click to select
"""
import dash

import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)


columnDefs = [
    {"field": "athlete"},
    {"field": "age"},
    {"field": "country"},
    {"field": "year"},
    {"field": "date"},
    {"field": "sport"},
    {"field": "gold"},
    {"field": "silver"},
    {"field": "bronze"},
    {"field": "total"},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid has multi-select rows.  Use shift click or ctr click to select rows"
        ),
        html.Div(id="selections-multiple-output"),
        dag.AgGrid(
            id="selection-multiple-grid",
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            columnSize="sizeToFit",
            defaultColDef={"resizable": True, "sortable": True, "filter": True, "minWidth": 125,},
            dashGridOptions={"rowSelection":"multiple"},
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("selections-multiple-output", "children"),
    Input("selection-multiple-grid", "selectedRows"),
)
def selected(selected):
    if selected:
        selected_athlete = [s["athlete"] for s in selected]
        return f"You selected athletes: {selected_athlete}"
    return "No selections"


if __name__ == "__main__":
    app.run_server(debug=True)
