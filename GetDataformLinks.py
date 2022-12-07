from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import json

driver = webdriver.Chrome()

Link = ["https://www.aliexpress.com/item/32802046365.html?pdp_npi= 2 % 40dis % 21USD % 21US % 20 % 2472.00 % 21US % 20 % 2472.00 % 21US % 20 % 2472.00 % 21 % 21 % 21 % 21 % 402100bb5116699882205247569e036f % 2164177374539 % 21sh"
        ]

time.sleep(5)

for i, value in enumerate(Link):
    data = []
    driver.get(Link[i])
    time.sleep(10)
    data.insert(0, Link[i])
    try:
        maindiv = driver.find_element(By.CLASS_NAME, 'product-main')
        time.sleep(35)

        # imgs = maindiv.find_element(By.TAG_NAME, 'img')
        # data.insert(1, imgs.get_attribute('src'))
        print(maindiv)
    except:
        print('noimgurl')
    
        

json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)