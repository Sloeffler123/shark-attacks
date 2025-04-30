import pandas as pd
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

geolocator = Nominatim(user_agent='geoapi', timeout=10)


def get_lat_lon(location, lat, lon):

    for i in location['Location']:
        time.sleep(1)
        try:
            geo = geolocator.geocode(i)
            if i.strip() == 'Unknown':
                lon.append('None')
                lat.append('None')
            elif geo:
                print('passed')
                print(i)
                lon.append(geo.longitude)
                lat.append(geo.latitude)   
            else:
                print('didnt pass')
                print(i)
                lat.append('None')
                lon.append('None')    
        except GeocoderTimedOut:
            time.sleep(1)    
# us_locations_t = pd.read_csv('us-shark-attack-data')
# us_longitute = []
# us_latitude = []            
# get_lat_lon(us_locations_t, us_latitude, us_longitute)
# us_locations_t['Latitude'] = us_latitude
# us_locations_t['Longitude'] = us_longitute
# us_locations_t.to_csv('us-shark-attack-data', index=False)

# aus_locations = pd.read_csv('australia-shark-attack-data')
# aus_locations_t = aus_locations.T
# aus_locations_t.columns = ['Date', 'Location', 'Name', 'Shark species']

# aus_longitude = []
# aus_latitude = []
# get_lat_lon(aus_locations_t, aus_latitude, aus_longitude)

# aus_locations_t['Latitude'] = aus_latitude
# aus_locations_t['Longitude'] = aus_longitude

# aus_locations_t.to_csv('aus-backup')

south_africa_locations = pd.read_csv('southafrica-shark-attack-data')
south_africa_locations_t = south_africa_locations.T
south_africa_locations_t.columns = ['Name', 'Date', 'Location', 'Shark species']

south_africa_latitude = []
south_africa_longitude = []
get_lat_lon(south_africa_locations_t, south_africa_latitude, south_africa_longitude)

south_africa_locations_t['Latitude'] = south_africa_latitude
south_africa_locations_t['Longitude'] = south_africa_longitude

south_africa_locations_t.to_csv('south-backup')

