from selenium import webdriver
import time
import os
import pandas as pd

# 當前程式碼的絕對路徑
this_path = os.path.abspath(os.path.dirname(__file__))
# print(this_path)
# *\github\other_code\LeetCode_question_list

# 禁止圖片的載入
prefs={'profile.managed_default_content_settings.omages':2}

# 呼叫相對路徑的Chrime爬蟲套件
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',prefs)
browser = webdriver.Chrome(executable_path=this_path+'/chromedriver' )

# 連接leetcode題庫的網址
url = 'https://leetcode.com/problemset/all'
browser.get(url)
time.sleep(20) # 等待網址的動態
# 確認換頁的點擊位置
table= browser.find_element_by_class_name("question-list-table")
page_button = table.find_elements_by_tag_name("tbody")[1]

# 存放題目
lines = list()

# 人工確認總共有34頁的題庫(一頁約有50題)
for i in range(1,34):
    # 從第一頁的位置開始點擊
    # 使用網頁元素的文字訊息進行確認
    page_button.find_element_by_link_text(f"{i}").click()
    table= browser.find_element_by_class_name("question-list-table")
    time.sleep(10)

    # 開始抓取題目的訊息
    # 用list存放資料
    table_temp = table.find_elements_by_tag_name("tbody")[0]
    questions = table_temp.find_elements_by_tag_name("tr")

    # check用於辨識對應的題目是否有鎖定
    # leetCode有些題目是必須升級為VIP會員才能夠練習的
    check = False
    for x in questions:
        # 單一行的題目
        line = list()
        check = True
        # table 表格元素的獲取
        col = x.find_elements_by_tag_name("td")

        for i in range(len(col)-1):
            # 判斷是否為VIP題目
            # 是：題目不列入清單中and跳出迴圈，否：題目納入
            if col[i].find_elements_by_class_name("fa-lock"):
                check =False
                break
            
            # 存入每個欄位的資訊
            string = col[i].text
            if len(string) != 0:
                line.append(col[i].text)

        # 判斷是否為VIP題目
        # 是：題目不列入清單中and跳出迴圈，否：題目納入
        if check:
            lines.append(line)
    # print(lines)

# 關閉瀏覽器
browser.quit()


# 把轉換為dict格式，方便放入datadframe
to_pd_dict = {
    "name":[x[1]for x in lines ],
    "accept":[x[2]for x in lines ],
    "level":[x[3]for x in lines ],
}
# print(to_pd_dict)


# 轉換成比較好理解的datadframe格式
# 在使用accept欄位的數值來判斷題目的順序，越高的數字代表此題目完成的人越多
# 越高的數字代表此題目完成的人越多，對應來說會是比較簡單的題目
LC_list =  pd.DataFrame(to_pd_dict)
LC_list.sort_values(by=['accept'],ascending=False,inplace=True)
LC_list.reset_index()

# leetcode題目習慣為網址+題目文字小寫且用'-'當作空白
# 例如：https://leetcode.com/problems/binary-tree-pruning/
# 就是題目 814. Binary Tree Pruning
# 下方為驗證測試工具，確認網址是否可以連接到leetCode網址
print( f"https://leetcode.com/problems/{ '-'.join(LC_list.loc[0,['name']].values[0].split())}/")
#
# print(LC_list)

# 將資料存成CSV檔，以方便後續使用
LC_list.to_csv(this_path+"/LC_list.csv")