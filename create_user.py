import sys
from selene.browsers import BrowserName
from selene.api import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import traceback
from time import sleep
import ssl
import datetime
import schedule

#各種パロメータの設定
users = [
    "userA",
    "userB"
]

names = [
    "username A",
    "username B",
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
        element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/ul/li[2]/a")
        element.click()
        sleep(1)
        element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/a")
        element.click()
        sleep(1)

        #input user information
        for i,d in enumerate(users):
            #user id
            element = driver.find_element(By.ID,"user_login")
            element.clear()
            print(users[i])
            element.send_keys(users[i])
            
            #name
            name = names[i]
            print(name)
            name_dic= name.split(" ")
            first_name = name_dic[0]
            last_name = name_dic[1]
            element = driver.find_element(By.ID, "user_firstname")
            element.clear()
            element.send_keys(first_name)
            element = driver.find_element(By.ID, "user_lastname")
            element.clear()
            element.send_keys(last_name)
            element = driver.find_element(By.ID, "user_mail")
            element.clear()
            element.send_keys(users[i] + "@g.nihon-u.ac.jp")
            element = driver.find_element(By.ID, "user_language")
            Select(element).select_by_value("ja")
            element.click()

            #password
            element = driver.find_element(By.ID, "user_password")
            element.clear()
            element.send_keys(users[i])
            element = driver.find_element(By.ID, "user_password_confirmation")
            element.clear()
            element.send_keys(users[i])
            
            #create_user_to_next
            element = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/form/p[2]/input[2]")
            element.click()

            sleep(1)
        
        browser.quit()

    except:
        print(traceback.format_exc())
        browser.quit()

main()



