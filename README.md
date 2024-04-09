# this a selenium training
## question (這邊說明為何要這麼做，用英文)

### step 1 將地號從一欄改為一列



### step 2 放入需要使用的庫，然後開啟網頁

#%pip install selenium
#%pip install webdriver_manager
#%pip install beautifulsoup4
#%pip install requests
#%pip install openpyxl
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

### step 3 設計迴圈，取得結果

for building_number, num2_value in building_data:
  time.sleep(0.01)
  clearbutton = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/form/div[4]/div/input[2]')
  clearbutton.click()
  time.sleep(0.05)
  select_area = driver.find_element(By.NAME, 'SiteArea')
  select_area.send_keys("新營區")   #區自己調
  time.sleep(0.1)
  select_site = driver.find_element(By.NAME, 'R48')
  select_site.send_keys("2146")   #段自己調
  time.sleep(0.01)
  #怎麼點選建號還地號?對該按鈕檢查後copy xpath
  clickbutton = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/form/div[2]/div/div[2]')
  clickbutton.click()
  time.sleep(0.01)
  num1 = driver.find_element(By.NAME, "NUM1")
  time.sleep(0.01)
  num2 = driver.find_element(By.NAME, "NUM2")
  time.sleep(0.01)
  num1.send_keys(building_number)
  num2.send_keys(num2_value)
  resultbutton = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/form/div[4]/div/input[1]')
  resultbutton.click()
    
  time.sleep(0.01)
    
  elem = driver.find_element(By.XPATH, "//*")
  time.sleep(0.01)
  html_text = elem.text
  html_text
    
  pattern = r'(\d{4}-\d{4})'
  start_tag = "\n行政區 土地段代碼 土地段小段名 地號 建物段代碼 建物段小段名 建號"     
  end_tag = "\n本查詢系統資料以各地政事務所為準，本系統資料僅供參考。\n"
  start_index = html_text.find(start_tag)
  if start_index != -1:
    end_index = html_text.find(end_tag, start_index + len(start_tag))
    if end_index != -1:
      result_text = html_text[start_index:end_index]
      land_numbers = re.findall(pattern, result_text)
      if land_numbers:
        found = False
        for land_number in land_numbers:
          if "周武段" in result_text:
            land_number = land_number.replace("周武段", "").strip()
            print(land_number)
            found = True
            break
            if not found:
              print("未找到周武段")
          else:
            print("未找到地號信息")
        else:
          print("未找到結束標記")
      else:
        print("未找到開始標記")



