from appium import webdriver
from selenium.webdriver.common.options import ArgOptions
from appium.webdriver.common.appiumby import AppiumBy
import time
import datetime

from .tools import *

# "C:\Users\slaye\AppData\Local\Android\Sdk\tools\bin\uiautomatorviewer.bat"

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

def go_to_home_screen(driver):
    # 홈 버튼 키코드
    KEYCODE_HOME = 3
    # 홈 버튼 누르기
    driver.press_keycode(KEYCODE_HOME)


def go_to_ok_cashbag(driver):
    # OK캐시백 앱 패키지명
    package_name = "com.skmc.okcashbag.home_google"
    
    # OK캐시백 앱 실행
    driver.activate_app(package_name)
    print("OK Cashbag app started.")

def dump_ui_hierarchy(driver):
    # 현재 UI 계층 구조 덤프
    xml_dump = driver.page_source
    with open("attendance/app/dump/ui_dump.xml", "w", encoding="utf-8") as f:
        f.write(xml_dump)
    print("UI hierarchy dumped to ui_dump.xml")

def click_menu_button(driver):
    try:
        # "메뉴" 버튼을 찾기
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("메뉴")').click()
    except:
        print("Failed to click the menu button.")

def scroll_and_click_element_by_text(driver, text):
    try:
        # 스크롤하여 특정 텍스트를 포함하는 요소 찾기
        element = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 
                                      f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))')
        element.click()
        print(f"Element with text '{text}' clicked.")
    except Exception as e:
        print(f"Error: {e}")

def click_element_by_bounds(driver, bounds):
    try:
        # XPath로 bounds를 이용하여 요소를 찾기
        xpath = f'//android.widget.TextView[@bounds="{bounds}"]'
        element = driver.find_element(AppiumBy.XPATH, xpath)
        element.click()
        print(f"Element with bounds '{bounds}' clicked.")
    except Exception as e:
        print(f"Error: {e}")


def click_attendance_button_by_index(driver, target_index):
    try:
        # 특정 index에 해당하는 View 요소를 찾고 클릭
        buttons = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
        button = buttons[target_index]
        button.click()
        print(f"Clicked the attendance button at index {target_index}.")
    except Exception as e:
        try:
            click_text(driver, "출석체크")
            print("Clicked the attendance button.")
        except Exception as e:
            pass

        print(f"Error: {e}")

def get_today_index():
    # 오늘 날짜의 일(day)을 가져옵니다.
    today = datetime.datetime.now().day
    # index는 0부터 시작하므로 오늘 날짜에서 1을 뺍니다.
    today_index = today - 1
    return today_index

def start_ok_cashback():
    driver = get_driver()
    go_to_home_screen(driver)
    time.sleep(5)
    go_to_ok_cashbag(driver)  # OK캐시백 앱 실행
    time.sleep(5)
    click_menu_button(driver)  # "메뉴" 버튼 클릭
    # time.sleep(10)
    # dump_ui_hierarchy()  # UI 계층 구조 덤프
    time.sleep(5)
    scroll_and_click_element_by_text(driver, "출석체크")  # 예시 텍스트 "출석체크"
    time.sleep(5)
    click_text(driver, "참여하기")
    time.sleep(5)
    package_name = "com.skmc.okcashbag.home_google"
    close_app(driver, package_name)
    

# if __name__ == "__main__":
#     driver = get_driver()
#     go_to_home_screen(driver)
#     time.sleep(5)
#     go_to_ok_cashbag(driver)  # OK캐시백 앱 실행
#     time.sleep(5)
#     click_menu_button(driver)  # "메뉴" 버튼 클릭
#     # time.sleep(10)
#     # dump_ui_hierarchy()  # UI 계층 구조 덤프
#     time.sleep(5)
#     scroll_and_click_element_by_text(driver, "출석체크")  # 예시 텍스트 "출석체크"
#     time.sleep(5)
#     tools.click_text(driver, "참여하기")
#     time.sleep(5)

