import pandas as pd
import plotly.express as px

# us_locations = pd.read_csv('us-shark-attack-data')


# agg_data = us_locations.groupby(['Location', 'Latitude', 'Longitude'], as_index=False).size()
# agg_data.rename(columns={'size': 'Count'}, inplace=True)
# fig = px.scatter_geo(agg_data, lat='Latitude', lon='Longitude', hover_name='Location', size='Count')

# fig.show()



aus_location = pd.read_csv('aus-backup')

agg_data = aus_location.groupby(['Location', 'Latitude', 'Longitude'], as_index=False).size()
agg_data.rename(columns={'size': 'Count'}, inplace=True)
fig = px.scatter_geo(agg_data, lat='Latitude', lon='Longitude', hover_name='Location', size='Count')

fig.show()





















