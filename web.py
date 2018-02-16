import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc

import plotly.graph_objs as go

import data

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1('Retailer Affinity'),
    html.Br(),
    html.P('Select a Parent Brand'),
    dcc.Dropdown(
       id='brand-choice',
       value='Red Bull',
       options=[
           {'label': 'Red Bull', 'value': 'Red Bull'},
           {'label': '5 Hour Energy', 'value': '5 Hour Energy'},
           {'label': 'Monster', 'value': 'Monster'},
           {'label': 'Rockstar', 'value': 'Rockstar'},
       ]
   ),
  dcc.Graph(id='brand-graph'),
])

@app.callback(Output('brand-graph','figure'),[Input('brand-choice','value')])
def create_figure(choice):
    retailer = data.retailer_affinity(choice)
    x_data=[]
    y_data=[]
    for values in retailer:
        x_data.append(values[0])
        y_data.append(values[1])
    info=[go.Bar(
        x=x_data,
        y=y_data
    )]
    return {
        'data':info,
        'layout': {
            'title': 'Strongest Retailer Affinity',
            'xaxis':{'title': 'Retailers'},
            'yaxis':{'title': 'Total Units Sold'}
        }
    }

if __name__ == '__main__':
    app.run_server()
