from selenium import webdriver
import time
import os

this_path = os.path.abspath(os.path.dirname(__file__))
print(this_path)
prefs={'profile.managed_default_content_settings.omages':2}
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',prefs)
browser = webdriver.Chrome(executable_path=this_path+'/chromedriver' )
    # options=options)
    

url = 'https://leetcode.com/problemset/all/'
browser.get(url)
text = browser.page_source
print(text)
time.sleep(30)

browser.quit()

