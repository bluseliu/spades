import json
from pymongo import MongoClient
import pymongo
import os
import requests
import time

path_dir = 'E:\專題\Mobile01\基隆景點'
os.chdir(path_dir)
load_all = os.listdir(r'E:\專題\Mobile01\基隆景點')
nums = len(load_all)
print('筆數:', nums)

for num in range(0, nums):
    filenames = load_all[num]

# 讀取爬完要寫入的資料
    with open(filenames,"r",encoding="utf-8") as f:
        new_dict = eval(f.readlines()[0]) # 將資料轉為可讀, 再以eval轉為dict型別
        print(new_dict, type(new_dict))
        # trn = eval(con)
        # print(trn, type(trn))

        # new_dict = json.load(f) # load:把檔案開啟，並把字串變換資料型別為字典
        # print(new_dict)

        # filename_0 = new_dict['文章網址']
        # print(filename_0)
        filename = str(new_dict['文章網址'])
        # filename = str(filename_1).split('-')[-1] # 取文章編號
        print('filename:', filename)
# 讀取mongoDB的資料
        try:
            client = pymongo.MongoClient('127.0.0.1:27017')  # python連mongodb
            db = client.spades  # 資料庫名稱為spades
            collection = db.place  # collection名稱:景點為place, 美食用food
            dict = collection.find_one({"文章網址": filename})
            # print('dict:', dict, type(dict))

            if dict == None:
                collection.insert_one(new_dict)
                print('已寫入', new_dict)

            else:
                print('資料已存在:', dict)
        except:
            print('save pass')

print('insert', filename, 'to mongoDB success')

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
