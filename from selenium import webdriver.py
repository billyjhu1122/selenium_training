from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re


driver_path = ChromeDriverManager().install()
print(driver_path)
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


driver.get("https://land-query.tainan.gov.tw/query/rwd/RHD10.jsp?csrf.param=23F87EFEA633013778626BE62DE9626C&menu=false#queryResult")
print(driver.title)


select_area = driver.find_element(By.NAME, 'SiteArea')
select_area.send_keys("新營區")   #區自己調
select_site = driver.find_element(By.NAME, 'R48check')
select_site.send_keys("周武段")   #段自己調