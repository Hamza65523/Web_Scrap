from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import csv

driver = webdriver.Chrome()

# Link = ['https://www.facebook.com/events/453038920095128/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/659986508569897/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/599396098301516/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/579563257297636/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/1093221798229875/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/3153247694926000/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/885927752816136/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D',
#         'https://www.facebook.com/events/588087651543223/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/837504024242638/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/374061874883607/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/1059611751589587/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/1435546653588948/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/3226277817631235/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/342738934600080/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D', 'https://www.facebook.com/events/847074523216294/?acontext=%7B%22event_action_history%22%3A[%7B%22mechanism%22%3A%22search_results%22%2C%22surface%22%3A%22bookmark_search%22%7D]%2C%22ref_notif_type%22%3Anull%7D']

Link = ['https://www.facebook.com/events/search/?q=auckland&filters=eyJycF9ldmVudHNfbG9jYXRpb246MCI6IntcIm5hbWVcIjpcImZpbHRlcl9ldmVudHNfbG9jYXRpb25cIixcImFyZ3NcIjpcIjEwMTg4MzE0OTg1MzcyMVwifSJ9']
with open('book10.csv', 'w',encoding='UTF8',newline='') as f:
    for i, value in enumerate(Link):
        data = []
        driver.get(Link[i])
        time.sleep(0.7)
        data.insert(0, Link[i])
        try:
            img = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div[1]')
            imgs = img.find_element(By.TAG_NAME,'img')
            data.insert(1, imgs.get_attribute('src'))
        except:
            print('noimgurl')
        try:
            title = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/h2/span/span/span')
            data.insert(2,title.text)
        except:
            print('notitle')
        try:
            subTitle = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div[3]/span/span')
            data.insert(3,subTitle.text)
        except:
            print('nosubTitle')
        writer = csv.writer(f)
        writer.writerow(data)


