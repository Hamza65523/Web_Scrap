from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv
driver = webdriver.Chrome()

give_link = driver.get('https://chinafencing.aliexpress.com/store/all-wholesale-products/1626122.html?spm=a2g0o.store_pc_home.pcShopHead_11287267.99')

print(driver.title)
link_list=[]
i = 0

SCROLL_PAUSE_TIME = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page

    sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        print(new_height,'range',last_height)
        break
    last_height = new_height

sleep(10)
# maindata = driver.find_element(By.XPATH,('/html/body/div[1]/div[5]/div[2]/div/div[2]/div[1]/div/div/div[5]/div/div/ul'))
# print(maindata.text)
maindata = driver.find_elements(By.CLASS_NAME,('item'))
with open('Links.csv', 'w',encoding='UTF8',newline='') as f:
    while i < len(maindata):
        try:
            writer =csv.writer(f)
            data = maindata[i].find_element(By.TAG_NAME,('a')).get_attribute('href')
            writer.writerow([data])
            print(link_list)
        except:
            print('nodata')
        
        i += 1
    # print('start',link_list,'end')


