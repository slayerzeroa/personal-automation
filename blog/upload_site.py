'''
Author : slayerzeroa
Date : 2023-01-24
티스토리 블로그 포스팅 반자동화
'''

#pip install gensim==3.8.3
#pip install webdriver_manager
#pip install -U pyautoit


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
import pyperclip
import time
import autoit
import os
import clipboard

def upload_tistory(title, contents, url):
    f = open('blog/env/tistory_id.txt', 'r')
    id = f.readline()
    f.close()

    f = open('blog/env/tistory_password.txt', 'r')
    password = f.readline()
    f.close()

    n = 0
    while n < 30:
        time.sleep(2)
        try:
            # 셀레니움
            service = Service(executable_path='blog/selenium/chromedriver.exe')
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            action = ActionChains(driver)

            # 1. 티스토리 로그인 접속
            login_url = "https://www.tistory.com/auth/login"
            driver.get(login_url)

            time.sleep(2)
            # 2. 카카오 로그인 접속
            elem = driver.find_element(By.CLASS_NAME, 'txt_login')
            elem.click()

            time.sleep(2)
            # 3. 아이디, 비밀번호 입력
            elem_id = driver.find_element(By.NAME, 'loginId')
            elem_id.click()
            pyperclip.copy(id)
            elem_id.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)

            elem_pw = driver.find_element(By.NAME, 'password')
            elem_pw.click()
            pyperclip.copy(password)
            elem_pw.send_keys(Keys.CONTROL, 'v')
            time.sleep(1)

            # 4. 로그인 버튼 클릭
            driver.find_element(By.CLASS_NAME, 'btn_g.highlight').click()
            time.sleep(300)

                # 5. Authentic 버튼 클릭
            driver.find_element(By.CLASS_NAME, 'btn_agree').click()
            time.sleep(5)
            
            break
        except:
            n += 1
            driver.close()



    # 6. 프로필 클릭
    driver.find_element(By.CLASS_NAME, 'thumb_profile').click()

    # 7. 작성 클릭
    driver.find_element(By.CLASS_NAME, 'img_common_tistory.link_edit').click()

    time.sleep(2)
    autoit.send("{Enter}")
    time.sleep(2)

    # 8. 카테고리 선정
    driver.find_element(By.ID, 'category-btn').click()
    driver.find_element(By.XPATH, "//span[text()='- 번역']").click()

    # 9. 내용 마련
    translate_contents, translate_title = contents, title

    # 10. 내용 및 제목 작성
    driver.find_element(By.ID, "post-title-inp").click()
    time.sleep(5)
    action.send_keys(translate_title).perform()
    time.sleep(5)


    driver.find_element(By.ID, 'kakao-editor-container').click()
    action.send_keys("\n").perform()
    time.sleep(5)
    action.send_keys(translate_contents).perform()
    time.sleep(5)
    action.send_keys("\n").perform()
    time.sleep(5)
    action.send_keys(url).perform()
    time.sleep(2)
    action.send_keys("\n").perform()
    action.send_keys("\n").perform()
    time.sleep(5)

    driver.find_element(By.ID, 'mceu_0-open').click()
    time.sleep(5)
    driver.find_element(By.ID, 'attach-image').click()
    handle = "[CLASS:#32770; TITLE:열기]"
    time.sleep(5)
    autoit.win_active("열기")
    time.sleep(5)
    img_path = "C:\\Users\\slaye\\VscodeProjects\\personal-automation\\blog\\public\\logo.PNG"
    autoit.control_send(handle, "Edit1", img_path)
    time.sleep(5)
    autoit.control_click(handle, "Button1")
    time.sleep(5)


    # 11. 완료 버튼 누르기
    driver.find_element(By.ID, "publish-layer-btn").click()
    time.sleep(5)
    driver.find_element(By.ID, "publish-btn").click()
    time.sleep(5)

upload_tistory('test', 'test', 'test')