import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# -------------------------------------------------------------
# Data
# -------------------------------------------------------------
# The CSV should be downloaded per lab instructions:
# wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Range limits for payload slider
min_payload = int(spacex_df['Payload Mass (kg)'].min())
max_payload = int(spacex_df['Payload Mass (kg)'].max())

# Launch site options (Task 1)
sites = sorted(spacex_df['Launch Site'].unique())
site_options = [{'label': 'All Sites', 'value': 'ALL'}] + [
    {'label': s, 'value': s} for s in sites
]


app = dash.Dash(__name__)
server = app.server  # so it can be discovered if deployed

app.layout = html.Div([
    html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center'}),

    # TASK 1: Launch Site Drop-down Input Component
    html.Div([
        dcc.Dropdown(
            id='site-dropdown',
            options=site_options,
            value='ALL',
            placeholder='Select a Launch Site here',
            searchable=True,
            clearable=False,
            style={'width': '100%'}
        )
    ], style={'width': '80%', 'margin': '0 auto'}),

    html.Br(),

    # TASK 2: Pie chart for launch success
    html.Div([
        dcc.Graph(id='success-pie-chart')
    ]),

    html.Br(),

    # TASK 3: Range Slider to Select Payload
    html.Div([
        html.P('Payload range (Kg):'),
        dcc.RangeSlider(
            id='payload-slider',
            min=0,
            max=10000,
            step=1000,
            value=[min_payload, max_payload],
            marks={
                0: '0',
                2500: '2500',
                5000: '5000',
                7500: '7500',
                10000: '10000'
            }
        )
    ], style={'width': '80%', 'margin': '0 auto'}),

    html.Br(),

    # TASK 4: Scatter chart
    html.Div([
        dcc.Graph(id='success-payload-scatter-chart')
    ])
])


# TASK 2: Callback to render success-pie-chart based on selected site
a = Output('success-pie-chart', 'figure')
b = Input('site-dropdown', 'value')

@app.callback(a, b)
def get_pie_chart(selected_site):
    if selected_site == 'ALL':
        # Show total successful launches per site
        df_success = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(
            df_success,
            names='Launch Site',
            title='Total Successful Launches by Site (All Sites)'
        )
        return fig
    else:
        # For a single site: show success vs failure counts
        site_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        outcome_counts = site_df['class'].value_counts().rename(index={0: 'Failure', 1: 'Success'}).reset_index()
        outcome_counts.columns = ['Outcome', 'Count']
        fig = px.pie(
            outcome_counts,
            names='Outcome',
            values='Count',
            title=f'Launch Outcomes for {selected_site}'
        )
        return fig

# TASK 4: Callback to render the success-payload-scatter-chart (scatter)
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'), Input('payload-slider', 'value')]
)
def update_scatter(selected_site, payload_range):
    low, high = payload_range
    # Filter by payload range first
    mask_payload = (spacex_df['Payload Mass (kg)'] >= low) & (spacex_df['Payload Mass (kg)'] <= high)
    filtered = spacex_df[mask_payload]

    # Then optionally filter by site
    if selected_site != 'ALL':
        filtered = filtered[filtered['Launch Site'] == selected_site]

    title = 'Correlation between Payload and Success for All Sites' if selected_site == 'ALL' else \
            f'Payload vs. Outcome for {selected_site}'

    fig = px.scatter(
        filtered,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        hover_data=['Launch Site', 'Booster Version', 'Flight Number'],
        title=title
    )
    return fig




# Run the app
if __name__ == '__main__':
    app.run(debug=True)

