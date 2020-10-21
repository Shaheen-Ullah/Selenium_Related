from selenium import webdriver
import time
import os
import pandas as pd




# 當前程式碼的絕對路徑
this_path = os.path.abspath(os.path.dirname(__file__))
# print(this_path)
# *\github\other_code\LeetCode_question_list

# 載入CSV檔
LC_list = pd.read_csv(this_path+"/LC_list.csv")

# 讀帳號密碼
account , password ="",""
with open(this_path+"/account.txt") as f:
    account = f.readline()
    password = f.readline()

print("account",account)
print("password",password)
# 禁止圖片的載入
# prefs={'profile.managed_default_content_settings.omages':2}

# 呼叫相對路徑的Chrime爬蟲套件
# options = webdriver.ChromeOptions()
# options.add_experimental_option('prefs',prefs)
driver = webdriver.Chrome(executable_path=this_path+'/chromedriver' )

# 連接facebook題庫的網址
url = 'https://www.facebook.com/groups/2649967561920825'
driver.get(url)
time.sleep(7)

#輸入email 
# context = driver.find_element_by_css_selector('input>#email')
context = driver.find_element_by_xpath('//*[@id="login_form"]/div/div[1]/label/input')
context.send_keys(account) 
time.sleep(1)

#輸入password
# context = driver.find_element_by_css_selector('input>#pass')
context = driver.find_element_by_xpath('//*[@id="login_form"]/div/div[2]/label/input')
context.send_keys(password)
time.sleep(1)

#
commit = driver.find_element_by_css_selector('#loginbutton')
commit.click()
time.sleep(7)
time.sleep(120) # 等待網址的動態

browser.quit()