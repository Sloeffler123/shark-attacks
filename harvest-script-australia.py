import time
import plotly.express as px
import pandas as pd
import json
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from locations import coastal_states
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

lst_of_data = []
j = 0
for i in data:
    if j == 1 or (j - 1) % 11 == 0:
        pass
    elif j == 3 or (j - 3) % 11 == 0:
        pass
    elif j == 5 or (j - 5) % 11 == 0:
        pass
    elif j == 6 or (j - 6) % 11 == 0:
        pass
    elif j == 7 or (j - 7) % 11 == 0:
        pass
    elif j == 8 or (j - 8) % 11 == 0:
        pass
    elif j == 10 or (j - 10) % 11 == 0:
        pass
    elif i.text == '' or i.text == ' ':
        lst_of_data.append('Unknown')
    else:
        cleaned_text = re.sub(r'\[.*?\]', '', i.text)
        lst_of_data.append(cleaned_text)
    j += 1        

print(len(lst_of_data))
print(lst_of_data)