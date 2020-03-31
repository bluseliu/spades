import json
import os
import shutil
import requests
import time

# 讀取景點資料 =====
"""
來源檔案：基隆市景點_wiki.txt, 台北市景點_wiki.txt, 新北市景點_wiki.txt,　桃園市景點_wiki.txt, 
          新竹市景點_wiki.txt, 新竹縣景點_wiki.txt, 宜蘭縣景點_wiki.txt
"""
scenery_all = open('E:\專題\Mobile01\台北市景點_wiki.txt', 'r', encoding='utf8').read().split()# ____________換地區要修改
scenery_all_num = len(scenery_all) ; print('wiki景點數scenery_num:', scenery_all_num)
print('wiki景點名稱scenery_all:', scenery_all)
print()

for scenery_num in range(0,scenery_all_num):
    # print('比對的景點scenery_num_all[num]:', 'num:', scenery_num, scenery_all[scenery_num])
    # print('=====')

# 讀取json資料夾 =====
    path_dir = 'E:\專題\\Mobile01\\json' ; os.chdir(path_dir) # E:\專題\Mobile01\json
    load_all = os.listdir(r'E:\專題\\Mobile01\\json')
    article_nums = len(load_all) ; # print('json文章數article_nums:', article_nums)

# 讀取json檔內容 =====
    for json_num in range(0, article_nums):
        filenames = load_all[json_num]
        # print('json_num第:', json_num, '筆:')
        # print('filenames檔名:', filenames)

        # 讀取爬完的json檔
        with open(filenames, "r", encoding="utf-8") as f:
            each_article = str(json.load(f))  # load:把檔案開啟，並把字串變換資料型別為字典
            print('取出的文章each_article:', type(each_article), each_article) # 取出的文章內容
            area = each_article[-5:-2]
            f.close()

            if area == '台北市': # _________________________________________________________________________換地區要修改
                if scenery_all[scenery_num] in each_article: # if比對的景點有在取出的文章內容中
                    print(filenames, '中取出的文章有關鍵字:', scenery_all[scenery_num], each_article)
                    # print('-----')
                    oldname = 'E:\\專題\\Mobile01\\json\\' + filenames # ; print(oldname)
                    # newfolder = 'E:\專題\Mobile01\景點' # ; print(newfolder)
                    newfolder = 'E:\專題\Mobile01\景點\台北景點' # ; print(newfolder)________________________換地區要修改
                    shutil.move(oldname, newfolder) ; print('file moved success!')
                    print('-----')
                else:
                    # pass
                    print(filenames, '中取出的文章沒有關鍵字:') #, scenery_all[scenery_num], each_article
                    # print('-----')
            else:
                print(filenames, 'not in 台北市') # ________________________________________________________換地區要修改

# Line通知
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code

message = '景點分類_檔案搬移完成 at ', time.asctime() # 修改為你要傳送的訊息內容
token = os.environ.get("linetk") # 修改為你的權杖內容
lineNotifyMessage(token, message)
