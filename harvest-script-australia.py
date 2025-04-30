import time
import plotly.express as px
import pandas as pd
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from shark_species import shark_species

# aus shark attacks
# Data format: Year/Area/Victim/Species
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/List_of_fatal_shark_attacks_in_Australia')
driver.maximize_window()
time.sleep(1)

data = driver.find_elements(By.TAG_NAME, 'td')

def check_shark(text, shark_lst):
    for k,v in shark_lst.items():
        if text.lower() in k.lower():
            return v
    return 'unknown'    
        
before_south_aus = {}
target_positions = [1, 3, 5, 6, 7, 8, 10]
j = 0
count = 1
evr = 0
for i in data:
    cleaned_text = re.sub(r'\[.*?\]', '', i.text).strip('\n')
    if any((j - pos) % 11 == 0 for pos in target_positions):
        pass
    elif f'victim {count}' not in before_south_aus:
        if cleaned_text == '1855':
            break  
        before_south_aus.update({f'victim {count}': [cleaned_text]})
    elif cleaned_text == '' or cleaned_text == ' ':
        before_south_aus[f'victim {count}'].append('Unknown')  
    elif j == 9 or (j - 9) % 11 == 0:
        shark = check_shark(cleaned_text,shark_species)
        before_south_aus[f'victim {count}'].append(shark)    
    else:
        before_south_aus[f'victim {count}'].append(cleaned_text)
    j += 1  
    evr += 1
    if evr == 11:
        count += 1
        evr = 0
   
south_aus = {} 
south_aus_target_positions = [1, 3, 4, 6, 7, 8, 9, 11]
s = 0
sou = 0
count_2 = count
for q in data[j:]:
    cleaned_text = re.sub(r'\[.*?\]', '', q.text).strip('\n')
    if any((s - pos) % 12 == 0 for pos in south_aus_target_positions):
        pass
    elif f'victim {count_2}' not in south_aus:
        if cleaned_text == '1820s':
            break
        south_aus.update({f'victim {count_2}': [cleaned_text]})
    elif cleaned_text == '' or cleaned_text == ' ':
        south_aus[f'victim {count_2}'].append('Unknown')
    elif s == 10 or (s - 10) % 12 == 0:
        shark = check_shark(cleaned_text, shark_species)
        south_aus[f'victim {count_2}'].append(shark)
    else:
        south_aus[f'victim {count_2}'].append(cleaned_text)
    s += 1    
    sou += 1 
    if sou == 12:
        count_2 += 1
        sou = 0

after_south_aus = {}     
num = j + s
w = 0
uy = 0
count_3 = count_2
for t in data[num:]:
    cleaned_text = re.sub(r'\[.*?\]', '', t.text).strip('\n')
    if any((w - pos) % 11 == 0 for pos in target_positions):
        pass
    elif f'victim {count_3}' not in after_south_aus:
        after_south_aus.update({f'victim {count_3}': [cleaned_text]})
    elif cleaned_text == '' or cleaned_text == ' ':
        after_south_aus[f'victim {count_3}'].append('Unknown')  
    elif w == 9 or (w - 9) % 11 == 0:
        shark = check_shark(cleaned_text,shark_species)
        after_south_aus[f'victim {count_3}'].append(shark)    
    else:
        after_south_aus[f'victim {count_3}'].append(cleaned_text)
    w += 1
    uy += 1
    if uy == 11:
        count_3 += 1
        uy = 0

before_south_aus.update(south_aus)

before_south_aus.update(after_south_aus)

json_string = json.dumps(before_south_aus)

# convert json to csv
df = pd.read_json(json_string)

# make csv file
df.to_csv('australia-shark-attack-data', index=False)

# see if i can split the locations and check each location to see if they are in the correct lat and lon in aus then append