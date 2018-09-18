import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

# Boostrap CSS.
app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})  # noqa: E501

df = pd.read_csv('Customer.csv')


def generate_table(dataframe, max_rows=4):
    return html.Table(
                      # Header
                      [html.Tr([html.Th(col) for col in dataframe.columns])] +
                      
                      # Body
                      [html.Tr([
                                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                                ]) for i in range(min(len(dataframe), max_rows))]
                      )
app.layout = html.Div(
                      html.Div([
                                # Header
                                html.Div([
                                          html.H1(children="Sparty's Analytics",
                                                  className='nine columns'),
                                          html.Img(
                                                   src="https://static1.squarespace.com/static/587d38b25016e1170b8ac882/t/5ad3a79470a6ad118a8d7722/1523820445424/",
                                                   className='three columns',
                                                   style={
                                                   'height': '7%',
                                                   'width': '7%',
                                                   'float': 'right',
                                                   'position': 'relative',
                                                   'padding-top': 0,
                                                   'padding-right': 0
                                                   },
                                                   ),
                                          html.Div(children='''
                                             Terminations:
                                             ''',
                                                   className='nine columns'
                                                   )
                                          ], className="row"
                                         ),
                                # Graph 1 and 2
                                html.Div([
                                          html.Div([
                                                    dcc.Graph(
                                                              id='example-graph',
                                                              figure={
                                                              'data': [
                                                                        go.Histogram(
                                                                               x=df['PaymentMethod'],
                                                            
                                                                       )
                                                              ],

                                                              }
                                                              )], className= 'six columns'
                                                   ),
                                          html.Div(
                                                    children=[
                                                              html.H4(children='My Table'),
                                                              generate_table(df)], className= 'six columns'
                                                   )
                                          ], className="row"),
                                # Graph 1 and 2
                                html.Div([
                                          html.Div([
                                              dcc.Graph(
                                                        id='life-exp-vs-gdp',
                                                        figure={
                                                        'data': [
                                                                 go.Scatter(
                                                                            x=df[df['gender'] == i]['tenure'],
                                                                            y=df[df['gender'] == i]['MonthlyCharges'],
                                                                            text=df[df['gender'] == i]['customerID'],
                                                                            mode='markers',
                                                                            opacity=0.7,
                                                                            marker={
                                                                            'size': 15,
                                                                            'line': {'width': 0.5, 'color': 'white'}
                                                                            },
                                                                            name=i
                                                                            ) for i in df.gender.unique()
                                                                 ],
                                                        'layout': go.Layout(
                                                                            xaxis={'type': 'log', 'title': 'Tenure'},
                                                                            yaxis={'title': 'Monthly Charges'},
                                                                            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                                                                            legend={'x': 0, 'y': 1},
                                                                            hovermode='closest'
                                                                            )
                                                        }
                                                        
                                                )], className= 'six columns' )
                                          ], className="row")
                                
                                ], className='ten columns offset-by-one')
                      )



if __name__ == '__main__':
    app.run_server(debug=True)


