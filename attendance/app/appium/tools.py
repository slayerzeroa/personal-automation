from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.options import ArgOptions

import time
import datetime



# 드라이버 생성
def get_driver():
    options = ArgOptions()
    
    capabilities = {
        "platformName": "Android",
        "deviceName": "SM-G930K",
        "udid": "ce0116019a307b3804",  # 'adb devices' 명령어로 확인 가능
        "automationName": "UiAutomator2",
        "uiautomator2ServerInstallTimeout": 120000,  # 120초로 시간 증가
        "adbExecTimeout": 120000  # ADB 실행 시간 초과 설정
    }


    for key, value in capabilities.items():
        options.set_capability(key, value)

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    return driver


# 현재 실행중인 앱 패키지명 확인
def get_current_package_name(driver):
    current_package_name = driver.current_package
    print(f"Current package name: {current_package_name}")
    return current_package_name

def go_to_home(driver):
    # 홈 버튼 키코드
    KEYCODE_HOME = 3
    # 홈 버튼 누르기
    driver.press_keycode(KEYCODE_HOME)


def go_to_app(driver, package_name):
    driver.activate_app(package_name)
    print(f"{package_name} app started.")


def click_text(driver, text):
    try:
        # "메뉴" 버튼을 찾기
        target = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")').click()
        print(f"Clicked {text} button.")
    except:
        print(f"Failed to click {text} button.")


# 부분적인 텍스트를 포함하는 요소 찾아서 클릭
def click_partial_text(driver, text):
    try:
        # "메뉴" 버튼을 찾기
        target = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().textContains("{text}")').click()
        print(f"Clicked {text} button.")
    except:
        print(f"Failed to click {text} button.")

def click_content_desc(driver, content_desc):
    try:
        # "메뉴" 버튼을 찾기
        target = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().description("{content_desc}")').click()
        print(f"Clicked {content_desc} button.")
    except:
        print(f"Failed to click {content_desc} button.")


def scroll_and_click_element_by_text(driver, text):
    driver = get_driver()
    try:
        # 스크롤하여 특정 텍스트를 포함하는 요소 찾기
        element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                      f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))')
        element.click()
        print(f"Element with text '{text}' clicked.")
    except Exception as e:
        print(f"Error: {e}")


def find_all_clickable(driver):
    clickable_elements = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().clickable(true).enabled(true)')
    print(f"Found {len(clickable_elements)} clickable elements.")
    for element in clickable_elements:
        print(element.text)


def find_all_index(driver, index=0):
    index_elements = driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().index({index})')
    print(f"Found {len(index_elements)} index elements.")
    result = []
    for element in index_elements:
        result.append(element)
    return result


# 앱 구조 dump
def dump_ui_hierarchy(driver):
    # 현재 UI 계층 구조 덤프
    xml_dump = driver.page_source
    with open("attendance/app/dump/ui_dump.xml", "w", encoding="utf-8") as f:
        f.write(xml_dump)
    print("UI hierarchy dumped to ui_dump.xml")


# 켜져 있는 앱이 있다면 종료
def close_app(driver, package_name):
    try:
        driver.terminate_app(package_name)
        print(f"{package_name} app terminated.")
    except:
        print(f"{package_name} app is not running.")