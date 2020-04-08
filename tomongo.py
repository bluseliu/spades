import json
from pymongo import MongoClient
import pymongo
import os
import requests
import time

folder_all = {'m':'Mobile01', 'y':'Yahoo', 'p':'Pixnet', 'o':'openrice', 'k':'okgo'}
print(folder_all.items())
folder = input('請輸入網站代碼: ')

# area = {11:'基隆景點', 12:'台北景點', 13:'新北景點', 14:'桃園景點', 15:'新竹景點', 16:'宜蘭景點'} # ____________景點
# area = {12:'台北景點'} # ____________openrice景點
area = {11:'基隆美食', 12:'台北美食', 13:'新北美食', 14:'桃園美食', 15:'新竹美食', 16:'宜蘭美食'} # ____________美食
print(area.items())

# for num in range(12,13): #_____________openrice
for num in range(11,17):
    path_dir = 'E:\專題\\' + folder_all.get(folder) + '\\' + area.get(int(num))
    print(path_dir)
    os.chdir(path_dir)
    load_all = os.listdir(path_dir)
    nums = len(load_all)
    print(area.get(int(num)), '筆數:', nums)

    for num in range(0, nums):
        filenames = load_all[num]
        # print(path_dir)
        # print('filenames:', filenames)

# 讀取爬完要寫入的資料
        with open(filenames,"r",encoding="utf-8") as f:
            new_dict = eval(f.readlines()[0]) # 將資料轉為可讀, 再以eval轉為dict型別
            # print('new_dict:', new_dict, type(new_dict))
            # trn = eval(con)
            # print(trn, type(trn))

            # new_dict = json.load(f) # load:把檔案開啟，並把字串變換資料型別為字典
            # print(new_dict)

            # filename_0 = new_dict['文章網址']
            # print(filename_0)
            filename = str(new_dict['文章網址'])
            # filename = str(filename_1).split('-')[-1] # 取文章編號
            # print('filename:', filename)
# 讀取mongoDB的資料
            try:
                client = pymongo.MongoClient('127.0.0.1:27017')  # python連mongodb
                db = client.spades  # 資料庫名稱為spades
                # collection = db.place  # collection名稱:景點為place
                collection = db.food  # collection名稱:美食用food
                dict = collection.find_one({"文章網址": filename})
                # print('dict:', dict, type(dict))

                if dict == None:
                    collection.insert_one(new_dict)
                    print('已寫入:', new_dict)

                else:
                    print('資料已存在:', dict)
            except:
                print('save pass')

print(folder_all.get(folder), '的所有資料已寫入MongoDB!!')

"""
# Line通知
def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code

message = 'mobile01_基隆景點 的所有文章已存入MongoDB at ', time.asctime() # 修改為你要傳送的訊息內容
token = os.environ.get("linetk") # 修改為你的權杖內容
lineNotifyMessage(token, message)
"""