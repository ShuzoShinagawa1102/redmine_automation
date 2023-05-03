import sys
from selene.browsers import BrowserName
from selene.api import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import traceback
from time import sleep
import ssl
import datetime
import schedule

#各種パロメータの設定
users = [
    "csao20073",
    "csfu20033",
    "csme22811",
    "csmo20053",
    "csry18021",
    "cssu20064",
    "cssz20040",
    "csti20807",
    "cstk20098",
    "csyo22809",
    "csyt19016",
    "gomi0917"
]

names = [
    "永井 蒼人",
    "小林 風太",
    "松浦 芽生",
    "高野 桃花",
    "釜田 諒大",
    "千葉 章大",
    "品川 周蔵",
    "徳永 泰介",
    "望月 丈瑠",
    "徳岡 美華",
    "江嵜 遊太",
    "五味 悠一郎"
]

def main():
    try:
        #setupu
        config.browser_name = BrowserName.CHROME
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--disable-gpu")
        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_option)
        browser.set_driver(driver)

        #access
        browser.open_url("https://redmine.gomilab.dynu.net")

        #login
        element = driver.find_element(By.CLASS_NAME,"login")
        element.click()
        element = driver.find_element(By.ID,"username")
        element.clear()
        element.send_keys("admin")
        element = driver.find_element(By.ID,"password")
        element.clear()
        element.send_keys("ttkh0218")
        element = driver.find_element(By.ID,"login-submit")
        element.click()
        print("ログイン完了")

        sleep(5)

        element = driver.find_element(By.CLASS_NAME,"administration")
        element.click()
        sleep(1)
        element = driver.find_element(By.CLASS_NAME,"icon icon-user users")
        element.click()
        sleep(1)
        element = driver.find_element(By.CLASS_NAME,"icon icon-add")
        element.click()
        sleep(1)

        #input user information
        for i,d in enumrate(users):
            #user id
            element = driver.find_element(By.ID,"user_login")
            element.clear()
            element.send_keys(users[d])
            
            #name
            name = names[d]
            name_dic= name.split("")
            first_name = name_dic[0]
            last_name = name_dic[1]
            element.driver.find_element(By.ID, "user_firstname")
            element.clear()
            element.send_keys(first_name)
            element.driver.find_element(By.ID, "user_lastname")
            element.clear()
            element.send_keys(last_name)
            element.driver.find_element(By.ID, "user_mail")
            element.clear()
            element.send_keys(users[d] + "@g.nihon-u.ac.jp")
            element = driver.find_element(By.ID, "user_language")
            Select(element).select_by_value("ja")
            element.click()

            #password
            element.driver.find_element(By.ID, "user_password")
            element.clear()
            element.send_keys(users[d])
            element.driver.find_element(By.ID, "user_password_confirmation")
            element.clear()
            element.send_keys(users[d])
            
            #create_user_to_next
            element.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form/p[2]/input[2]")
            element.click()

            sleep(1)
        
        browser.quit()

    except:
        print(traceback.format_exc())
        browser.quit()

main()



