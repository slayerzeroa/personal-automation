
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
import time
import os

service = Service(executable_path='attendance/selenium/chromedriver.exe')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = ActionChains(driver)

implicit_wait = 10

f = open('attendance/web/env/lotteon.txt', 'r')
id = f.readline().strip()
password = f.readline().strip()
f.close()


# 1. 롯데백화점 페이지 접속
url = "https://www.lotteon.com/p/display/main/ellotte"
driver.get(url)
driver.implicitly_wait(implicit_wait)

# 1.1 팝업창 닫기
tabs = driver.window_handles
driver.implicitly_wait(implicit_wait)
print(tabs)
# 팝업창이 여러 개일 경우 닫기
while len(tabs) != 1:
    driver.implicitly_wait(implicit_wait)
    driver.switch_to.window(tabs[1])
    driver.close()

# 메인 탭으로 이동
driver.switch_to.window(tabs[0])


# iframe 확인

# 모든 iframe 요소 찾기
iframes = driver.find_elements(By.TAG_NAME, 'iframe')

# 각 iframe의 ID와 name 속성 출력
for index, iframe in enumerate(iframes):
    iframe_id = iframe.get_attribute('id')
    iframe_name = iframe.get_attribute('name')
    print(f"Iframe #{index}: ID='{iframe_id}', Name='{iframe_name}'")

driver.switch_to.frame('destination_publishing_iframe_lotteshopping_0')


# 2. 출석체크 페이지 접속
driver.find_element(By.XPATH, '//*[@id="quickmenu_shapemix-swiper__67"]/div/div[7]/a').click()
driver.implicitly_wait(implicit_wait)

time.sleep(30)


# # 2. 로그인 버튼 클릭
# driver.find_element(By.XPATH, '//*[@id="welcome_header_wrap"]/div[1]/div/div[2]/ul/li[2]/a').click()
# driver.implicitly_wait(implicit_wait)


# # 3. 아이디, 비밀번호 입력
# driver.find_element(By.XPATH, '//*[@id="mainDiv"]/main/section/div[1]/div[1]/div[1]/div/input').click()
# driver.implicitly_wait(implicit_wait)
# action.send_keys(id).perform()
# driver.implicitly_wait(implicit_wait)
# driver.find_element(By.XPATH, '//*[@id="mainDiv"]/main/section/div[1]/div[1]/div[2]/div/input').click()
# action.send_keys(password).perform()
# driver.implicitly_wait(implicit_wait)
# driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()
# time.sleep(30)


# # 4. 출석체크 버튼 클릭
# driver.find_element(By.XPATH, '//*[@id="contents"]/div/div/div/div[1]/div[1]/button').click()
