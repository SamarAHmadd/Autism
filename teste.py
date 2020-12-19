from selenium import webdriver
from bs4 import BeautifulSoup
url="https://www.kaggle.com/faizunnabi/autism-screening"
browser = webdriver.Chrome()
browser.get(url)
import time
time.sleep(10)
html=browser.page_source
soup=BeautifulSoup(html,'html.parser')
with open('Autism.csv','w')as file:
    file.write(str(soup))