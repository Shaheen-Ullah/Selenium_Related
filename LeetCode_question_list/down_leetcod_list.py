from selenium import webdriver
import time
import os
import pandas as pd

this_path = os.path.abspath(os.path.dirname(__file__))
print(this_path)
prefs={'profile.managed_default_content_settings.omages':2}
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',prefs)
browser = webdriver.Chrome(executable_path=this_path+'/chromedriver' )
url = 'https://leetcode.com/problemset/all'
browser.get(url)
time.sleep(20)
table= browser.find_element_by_class_name("question-list-table")
page_button = table.find_elements_by_tag_name("tbody")[1]
lines = list()
for i in range(1,34):
    page_button.find_element_by_link_text(f"{i}").click()
    table= browser.find_element_by_class_name("question-list-table")
    table_temp = table.find_elements_by_tag_name("tbody")[0]
    questions = table_temp.find_elements_by_tag_name("tr")
    # questions = table_test.find_elements_by_tag_name("tr")
    # lines = list()
    check = False
    for x in questions:
        line = list()
        check = True
        col = x.find_elements_by_tag_name("td")

        for i in range(len(col)-1):
            if col[i].find_elements_by_class_name("fa-lock"):
                check =False
                break

            string = col[i].text
            if len(string) != 0:
                line.append(col[i].text)

        if check:
            lines.append(line)
    # print(lines)
    time.sleep(30)

browser.quit()
# print(len(lines))
# print(lines[:5])
to_pd_dict = {
    "name":[x[1]for x in lines ],
    "accept":[x[2]for x in lines ],
    "level":[x[3]for x in lines ],
}
# print(to_pd_dict)
LC_list =  pd.DataFrame(to_pd_dict)
newdata = data.sort_values(by=['accept'],ascending=False).reset_index()
test = f"https://leetcode.com/problems/{ '-'.join(newdata.loc[0,['name']].values[0].split())}/"
