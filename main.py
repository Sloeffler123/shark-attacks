import time
import plotly.express as px
import pandas as pd
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from locations import coastal_states, australia_states_territories, south_africa_provinces
from shark_species import shark_species

# US attacks
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/List_of_fatal_shark_attacks_in_the_United_States')
driver.maximize_window()
time.sleep(1)
name_age = driver.find_elements(By.TAG_NAME, 'td')

lst = []
after_lst = []

found = 0
for i in name_age:
    if i.text == 'Stephen Howard Schafer, 38':
        found = 1   
        after_lst.append(i.text.strip())
    elif found == 0:
        cleaned_text = re.sub(r'\[\d+\]', '', i.text)
        lst.append(cleaned_text.strip())
    else:
        cleaned_text = re.sub(r'\[\d+\]', '', i.text)
        if i.text != '':
            after_lst.append(cleaned_text.strip())
count = 1
up_to_2009 = {}
after_2009_to_present = {}
def find_loc(locations, range_loc, list):
    loc = list[range_loc]
    for k,v in locations.items():
        if 'Unknown' in loc or 'Unconfirmed,' in loc:
            return None
        elif k in loc:
            return v
    return None    
def find_shark(sharks, range_loc, list):
    loc = list[range_loc]
    for k,v in sharks.items():
        if 'Unknown' in loc or 'Unconfirmed' in loc:
            return None
        elif k in loc:
            return v
    return None   

j = 0

for i in range(len(lst)):
    if f'victim {count}' not in up_to_2009:
        up_to_2009.update({f'victim {count}': [lst[i]]})
    elif i == 2 or (i - 2) % 4 == 0:
        shark = find_shark(shark_species, i, lst)
        if shark:
            up_to_2009[f'victim {count}'].append(shark)
        else:
            up_to_2009[f'victim {count}'].append('Unknown')    
    elif i == 3 or (i - 3) % 4 == 0:
        place = find_loc(coastal_states, i, lst)
        if place:
            up_to_2009[f'victim {count}'].append(place)    
        else:
            up_to_2009[f'victim {count}'].append('location unknown')    
    else:
        up_to_2009[f'victim {count}'].append(lst[i])    
    j += 1
    if j == 4:
        count += 1
        j = 0
  
    if i+1 == len(lst):
        d = 0
        for q in range(len(after_lst)):
            if f'victim {count}' not in after_2009_to_present:
                after_2009_to_present.update({f'victim {count}': [after_lst[q]]})
            elif q == 3 or (q - 3) % 4 == 0:
                shark = find_shark(shark_species, q, after_lst)
                print(shark)
                if shark:
                    after_2009_to_present[f'victim {count}'].append(shark)
                else:
                    after_2009_to_present[f'victim {count}'].append('Unknown')    
            elif q == 4 or (q - 4) % 4 == 0:
                pass
            #     place = find_loc(coastal_states, q)
            #     if place:
            #         after_2009_to_present[f'victim {count}'].append(place)
            #     else:
            #         after_2009_to_present[f'victim {count}'].append('location unknown')   
            else:
                after_2009_to_present[f'victim {count}'].append(after_lst[q])   
            d += 1
            if d == 5:
                count += 1
                d = 0                   
print(up_to_2009)
print(after_2009_to_present)