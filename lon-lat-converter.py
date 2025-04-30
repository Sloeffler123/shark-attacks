import pandas as pd
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

us_locations_t = pd.read_csv('us-shark-attack-data')
geolocator = Nominatim(user_agent='geoapi', timeout=10)
us_longitute = []
us_latitude = []
for i in us_locations_t['Location']:
    time.sleep(1)
    try:
        geo = geolocator.geocode(i)
        if i.strip() == 'location unknown':
            us_longitute.append('None')
            us_latitude.append('None')
        elif geo:
            print('passed')
            print(i)
            us_longitute.append(geo.longitude)
            us_latitude.append(geo.latitude)
        else:
            print('didnt pass')
            print(i)
            us_longitute.append(None)
            us_latitude.append(None)    
    except GeocoderTimedOut:
        time.sleep(1)    

us_locations_t['Latitude'] = us_latitude
us_locations_t['Longitude'] = us_longitute


us_locations_t.to_csv('us-shark-attack-data', index=False)
