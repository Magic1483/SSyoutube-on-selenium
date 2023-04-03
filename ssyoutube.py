from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import requests
from urllib.parse import quote



def download(link:str,title:str):
    import wget
    
    
    # Make http request for remote file data
    wget.download(link, title)

def download2(link:str,title:str):
    data =requests.get(link)
    with open(title,'wb') as f:
        f.write(data.content)

def main(url:str):
    options = Options()
    options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.

    driver = webdriver.Chrome(options=options)

    l = url.split('youtube')
    url = l[0]+'ssyoutube'+l[1]

    driver.get(url)
    time.sleep(4)
    bt = WebDriverWait(driver=driver,timeout=3).until(
        EC.presence_of_element_located((By.XPATH,"//a[contains(@class, 'link-download')]"))
    )

    title = bt.get_attribute('download')

    print(title)
    # driver.find_element(By.XPATH,"//a[@class='link link-download subname ga_track_events download-icon']")

    link = bt.get_attribute('href')


    # print(title,link)

    download(link,title)

    driver.quit()
    


if __name__ == '__main__':
    link = input('> ')
    main(link)