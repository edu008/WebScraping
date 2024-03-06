from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

url = 'https://www.IDK.com/#!/IDK/IDK'

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get(url)


time.sleep(5)

html_content = driver.page_source

soup = BeautifulSoup(html_content, 'html.parser')


all_links = soup.find_all('a')

for link in all_links:

    #The href attribute is required; it could be provided using 'ng-href'.
    href = link.get('IDK')
    #Here you should describe the structure of the links as found in the browser's inspect tool.
    if href and href.startswith('#!/IDK/IDK/IDK/'):
        #If the href element is missing some elements, preventing the link from being opened, use this workaround.
        url2 = "https://www.IDK.com/" + href
        
        driver.get(url2)
        time.sleep(3)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')

        # Now you should identify the type of information needed from the inspect tool.
        field_value = soup.find('div', class_='IDK')
        if field_value:
            print("content:")
            print(field_value.text.strip())
        else:
            print("no content found")




driver.quit()
