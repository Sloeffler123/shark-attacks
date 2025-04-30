import pandas as pd
import plotly.express as px

us_locations = pd.read_csv('us-shark-attack-data')
us_agg_data = us_locations.groupby(['Location', 'Latitude', 'Longitude'], as_index=False).size()
us_agg_data.rename(columns={'size': 'Count'}, inplace=True)

aus_location = pd.read_csv('australia-shark-attack-data')
aus_agg_data = aus_location.groupby(['Location', 'Latitude', 'Longitude'], as_index=False).size()
aus_agg_data.rename(columns={'size': 'Count'}, inplace=True)

south_africa_location = pd.read_csv('southafrica-shark-attack-data')
south_agg_data = south_africa_location.groupby(['Location', 'Latitude', 'Longitude'], as_index=False).size()
south_agg_data.rename(columns={'size': 'Count'}, inplace=True)

combined_data = pd.concat([us_agg_data, aus_agg_data, south_agg_data], ignore_index=True)

fig = px.scatter_geo(combined_data, lat='Latitude', lon='Longitude', hover_name='Location', size='Count')
fig.show()