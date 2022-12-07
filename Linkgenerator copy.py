from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import csv
driver = webdriver.Chrome()

give_link = driver.get('https://chinafencing.aliexpress.com/store/all-wholesale-products/1626122.html?spm=a2g0o.store_pc_home.pcShopHead_11287267.99')

print(driver.title)
link_list=[]
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
sleep(25)
maindata = driver.find_elements(By.XPATH,('/html/body/div[2]/div[5]/div[2]/div/div[2]/div[1]/div/div/div[5]/div/div/ul/*'))
i = 0

with open('Links.csv', 'w',encoding='UTF8',newline='') as f:
    while i < len(maindata):
        try:
            # link = maindata[i].find_element(By.TAG_NAME,('a')).get_attribute('href')
            # imgUrl = maindata[i].find_element(By.TAG_NAME,('img')).get_attribute('src')
            # date = maindata[i].find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[{}]/a/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div/div[1]/span/span'.format(i))
            # title = maindata[i].find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[{}]/a/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div/div[2]/span/span/object/a/span'.format(i))
            # subtitle = maindata[i].find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[{}]/a/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div/div[3]/span/span/span'.format(i))
            # intrested = maindata[i].find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[{}]/a/div[1]/div/div/div/div/div[2]/div[2]/div/span/span'.format(i))
            writer =csv.writer(f)
            maindata[i].find_element(By.TAG_NAME,'a').get_attribute('href')
            print(maindata[i])
            # writer.writerow([link,imgUrl,date.text,title.text,subtitle.text,intrested.text])
        except:
            print('ok')
        i += 1
