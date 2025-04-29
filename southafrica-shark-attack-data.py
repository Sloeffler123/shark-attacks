import time
import plotly.express as px
import pandas as pd
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from shark_species import shark_species


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/List_of_fatal_shark_attacks_in_South_Africa#')
driver.maximize_window()
time.sleep(1)

data = driver.find_elements(By.TAG_NAME, 'td')

data_lst = [i.text for i in data]

def check_shark(text, shark_lst):
    for k,v in shark_lst.items():
        if text.lower() in k.lower():
            return v
    return 'unknown'  

all_data = {}
j = 0
s = 0
count = 1
for i in data_lst:
    if f'victim {count}' not in all_data:
        all_data.update({f'victim {count}': [i]})
    elif j == 4 or (j - 4) % 5 == 0:
        pass
    elif j == 3 or (j - 3) % 5 == 0:
        shark = check_shark(i, shark_species)
        all_data[f'victim {count}'].append(shark)
    else:
        all_data[f'victim {count}'].append(i)
    j += 1
    s += 1
    if s == 5:
        count += 1
        s = 0
        if count == 112:
            break
    
print(all_data)
