import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

us_locations = pd.read_csv('us-shark-attack-data')
us_agg_data = us_locations.groupby(['Location', 'Latitude', 'Longitude'], as_index=False).size()
us_agg_data.rename(columns={'size': 'Count'}, inplace=True)
us_agg_data['Region'] = 'USA'

aus_location = pd.read_csv('australia-shark-attack-data')
aus_agg_data = aus_location.groupby(['Location', 'Latitude', 'Longitude'], as_index=False).size()
aus_agg_data.rename(columns={'size': 'Count'}, inplace=True)
aus_agg_data['Region'] = 'Australia'

south_africa_location = pd.read_csv('southafrica-shark-attack-data')
south_agg_data = south_africa_location.groupby(['Location', 'Latitude', 'Longitude'], as_index=False).size()
south_agg_data.rename(columns={'size': 'Count'}, inplace=True)
south_agg_data['Region'] = 'South Africa'

combined_data = pd.concat([us_agg_data, aus_agg_data, south_agg_data], ignore_index=True)

map_fig = px.scatter_geo(combined_data, lat='Latitude', lon='Longitude', hover_name='Location', size='Count', color='Region')

region_counts = combined_data.groupby('Region')['Count'].sum().reset_index()
bar_trace = go.Bar(x=region_counts['Region'], y=region_counts['Count'], name='Fatal Shark Attacks')

fig = make_subplots(rows=1, cols=2, column_widths=[0.7, 0.3], specs=[[{'type': 'geo'}, {'type': 'xy'}]], subplot_titles=['Shark Attack Map', 'Attacks by Region'])

for trace in map_fig.data:
    fig.add_trace(trace, row=1, col=1)

fig.add_trace(bar_trace, row=1, col=2)

fig.update_layout(height=600, title_text='Fatal Shark Attack Data', showlegend=False)
fig.show()