

### install selenium & webdriver_manager

#%pip install selenium
#%pip install webdriver_manager


### import some required packages

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


### Connecting to website

driver_path = ChromeDriverManager().install()
print(driver_path)
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://land-query.tainan.gov.tw/query/rwd/RHD10.jsp?csrf.param=23F87EFEA633013778626BE62DE9626C&menu=false#queryResult")
print(driver.title)


### copy from building_data_finish.xlsx 

building_data = [ ('00889','000'),('00891','000'),('00671','000'),('00674','000'),('00680','000'),('00681','000'),('00682','000'),('00689','000'),('00690','000'),('00691','000'),('00693','000'),('00694','000'),('00695','000'),('00697','000'),('00685','000'),('00541','000'),('00566','000'),('00540','000'),('00539','000'),('00531','000'),('00545','000'),('00535','000'),('00518','000'),('00517','000'),('00515','000'),('00511','000'),('00512','000'),('00514','000'),('00562','000'),('00635','000'),('00636','000'),('00637','000'),('00638','000'),('00639','000'),('00640','000'),('00641','000'),('00642','000'),('00643','000'),('00644','000'),('00645','000'),('00628','000'),('00629','000'),('00630','000'),('00631','000'),('00632','000'),('00633','000'),('00560','000'),('00559','000'),('00543','000'),('00564','000'),('00492','000'),('00496','000'),('00498','000'),('00457','000'),('00458','000'),('00462','000'),('00522','000'),('00526','000'),('00527','000'),('00546','000'),('00549','000'),('00552','000'),('00298','000'),('00002','000'),('00308','000'),('00310','000'),('00312','000'),('00315','000'),('00239','000'),('00230','000'),('00208','000'),('00041','000'),('00036','000'),('00015','000'),('00016','000'),('00028','000'),('00183','000'),('00182','000'),('00181','000'),('00162','000'),('00077','000'),('00419','000'),('00836','000'),('00835','000'),('00769','000'),('00449','000'),('00813','000'),('00816','000'),('00825','000'),('00827','000'),('00829','000'),('00831','000'),('00893','000'),('00897','000'),('00544','000'),('00489','000'),('00504','000'),('00455','000'),('00460','000'),('00435','000'),('00570','000'),('00617','000'),('00572','000'),('00575','000'),('00718','000'),('00710','000'),('00721','000'),('00726','000'),('00616','000'),('00615','000'),('00605','000'),('00713','000'),('00600','000'),('00584','000'),('00598','000'),('00652','000'),('00654','000'),('00657','000'),('00658','000'),('00666','000'),('00619','000'),('00502','000'),('00320','000'),('00325','000'),('00391','000'),('00394','000'),('00395','000'),('00281','000'),('00280','000'),('00272','000'),('00400','000'),('00403','000'),('00402','000'),('00399','000'),('00771','000'),('00733','000'),('00734','000'),('00812','000'),('00809','000'),('00742','000'),('00736','000'),('00781','000'),('00782','000'),('00213','000'),('00156','000'),('00056','000'),('00055','000'),('00053','000'),('00051','000'),('00409','000'),('00116','000'),('00145','000'),('00146','000'),('00060','000'),('00059','000'),('00058','000'),('00065','000'),('00066','000'),('00067','000'),('00068','000'),('00070','000'),('00071','000'),('00422','000'),('00421','000'),('00479','000'),('00488','000'),('00495','000'),('00648','000'),('00647','000'),('00573','000'),('00582','000'),('00590','000'),('00591','000'),('00592','000'),('00595','000'),('00596','000'),('00429','000'),('00474','000'),('00431','000'),('00484','000'),('00485','000'),('00503','000'),('00505','000'),('00506','000'),('00476','000'),('00478','000'),('00481','000'),('00486','000') ]


### Write a loop

for building_number, num2_value in building_data:
    clearbutton = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/form/div[4]/div/input[2]')
    clearbutton.click()
    time.sleep(0.1)
    select_area = driver.find_element(By.NAME, 'SiteArea')
    select_area.send_keys("新營區")   #區自己調
    time.sleep(0.1)
    select_site = driver.find_element(By.NAME, 'R48')
    select_site.send_keys("2146")   #段自己調
    time.sleep(0.01)
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
    elem = driver.find_element(By.XPATH, "//*")
    time.sleep(0.01)
    html_text = elem.text
    
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
