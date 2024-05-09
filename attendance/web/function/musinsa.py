
import requests
from bs4 import BeautifulSoup as BS
from datetime import date
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
import time
import autoit
import os
import clipboard

service = Service(executable_path='attendance/selenium/chromedriver.exe')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = ActionChains(driver)

implicit_wait = 10

f = open('attendance/web/env/musinsa.txt', 'r')
id = f.readline().strip()
password = f.readline().strip()
f.close()


# 1. 출석체크 페이지 접속
url = "https://www.musinsa.com/mz/streetsnap"
driver.get(url)
driver.implicitly_wait(implicit_wait)

# 2. 로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[2]/div/div/div[3]/ul/li[2]').click()

# 2. 스냅샷 페이지 접속
driver.find_element(By.XPATH, '//*[@id="wrapper"]/div[2]/div[2]/div[2]/div/div/div[3]/ul/li[1]').click()
driver.implicitly_wait(implicit_wait)

time.sleep(10)


# # 3. 아이디, 비밀번호 입력
# action.send_keys(id).perform()
# driver.implicitly_wait(implicit_wait)
# driver.find_element(By.XPATH, '//*[@id="typeMemberInputPassword"]').click()
# driver.implicitly_wait(implicit_wait)
# action.send_keys(password).perform()
# driver.implicitly_wait(implicit_wait)
# driver.find_element(By.XPATH, '//*[@id="btn_memberLogin"]').click()
# driver.implicitly_wait(implicit_wait)

# # 모든 iframe 요소 찾기
# iframes = driver.find_elements(By.TAG_NAME, 'iframe')

# # 각 iframe의 ID와 name 속성 출력
# for index, iframe in enumerate(iframes):
#     iframe_id = iframe.get_attribute('id')
#     iframe_name = iframe.get_attribute('name')
#     print(f"Iframe #{index}: ID='{iframe_id}', Name='{iframe_name}'")

# driver.switch_to.frame('AttendRulletFrame')

# driver.find_element(By.XPATH, '//*[@id="wrapper"]/a').click()
# time.sleep(30)


# # 4. 출석체크 버튼 클릭
# driver.find_element(By.XPATH, '//*[@id="wrapper"]/a').click()

# time.sleep(10)
# driver.implicitly_wait(implicit_wait)
