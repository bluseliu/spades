import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from urllib import request
from bs4 import BeautifulSoup
import os
import time
import random

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

# 列表 =====
area = {188:'基隆市', 189:'台北市', 190:'新北市', 191:'桃園市', 192:'新竹市', 193:'新竹縣', 209:'宜蘭縣'}
print(area.items())
num = input('請輸入縣市代碼: ')

# 建立縣市資料夾 =====
# path_dir = 'E:\專題\Mobile01\基隆市'
path_dir = 'E:\專題\\Mobile01\\' + area.get(int(num))
# if not os.path.exists(path_dir):
#     os.mkdir(path_dir)
#     print('建立新資料夾:', path_dir, '\n') # E:\專題\Mobile01\基隆市
# else:
#     print('資料夾 ' + path_dir + ' 已存在')

# 爬取列表 =====
print('開始爬取:', area.get(int(num)))

url_p1 = 'https://www.mobile01.com/topiclist.php?f=' + num
# url_p1 = 'https://www.mobile01.com/topiclist.php?f=188'
req = request.Request(url=url_p1, headers=headers)
res = request.urlopen(req)
# print(res.read().decode('utf-8'))
content_p1 = BeautifulSoup(res, 'html.parser')
# print(content_p1)
title_txt = content_p1.select('div[class="c-listTableTd__title"] a[class="c-link u-ellipsis"]')

# 總頁數 =====
total_pages = int(content_p1.select('div[class="l-navigation__item l-navigation__item--min"], a[class="c-pagination"]')[-1].text) +1
# total_pages = 2

# 列表頁 =====
page = 1
while page < total_pages:
    # url = 'https://www.mobile01.com/topiclist.php?f=' + num + '&p=1'
    # url = 'https://www.mobile01.com/topiclist.php?f=188&p=26'
    url = 'https://www.mobile01.com/topiclist.php?f=' + num + '&p={0}'.format(page)
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    content_all = BeautifulSoup(res, 'html.parser')
    title_txt = content_all.select('div[class="c-listTableTd__title"] a[class="c-link u-ellipsis"]')
    print('page', page, ':', url)

# 特殊符號 =====
    for n in range(0,30):
        try:
            title_replace = title_txt[n].text
            title_save = title_replace[0:20].replace('*','').replace('|','').replace('\\','').replace(':','')\
            .replace('\"','').replace('<','').replace('>','').replace(']','').replace('[','').replace('?','')\
            .replace('/','').replace('《','').replace('》','').replace('・','').replace('/','').replace('，','')\
            .replace('「','').replace('」','').replace('！','').replace('｜','').replace('【','').replace('】','')\
            .replace('？','').replace('、','').replace('.','').replace('’','').replace('–','').replace('～','')\
            .replace('?','').replace('#','').replace('!','').replace('(','').replace(')','').replace('~','')

        except:
            title_save = "title pass"
            print(title_save)

# 文章序號 =====
        try:
            url_back = title_txt[n]['href'][12:]
            url_article = 'https://www.mobile01.com/topicdetail.' + url_back # 文章網址
            serial = url_article.split('=')[-1] # 文章序號

        except:
            print('article serial pass')

# 讀取進度 =====
        os.chdir('E:\專題\\Mobile01\\')
        serial_txt = area.get(int(num)) + '_serial.txt'
        f = open(serial_txt, mode='a', encoding='utf8' + '\n')
        content_txt = open(serial_txt)
        serial_content = content_txt.read()
        serial = url_back.split('=')[-1]

        if serial in serial_content:
            print('page', page, ':文章編號' + serial + '已存在')

        else:
            f = open(serial_txt, mode='a', encoding='utf8' + '\n')
            f.write(serial + '\n')

# 標題及建立文章資料夾 =====
            try:
                title = ('{"標題":"' + title_save + '"}')
                path_dir_each = path_dir + '\\' + title_save

            except:
                title = "title pass"
                print(title)

            # 網址
            try:
                url_back = title_txt[n]['href'][12:]
                url_article = 'https://www.mobile01.com/topicdetail.' + url_back
                url_article_1 = ('{"文章網址":"' + url_article + '"}')

            except:
                url_article = "https://www.Nodata_url_article"
                print(url_article)

# 建立圖片資料夾 =====(要抓圖片時取消此段註解即可)
#             if not os.path.exists(path_dir_each):
#                 os.mkdir(path_dir_each)
#             os.chdir(path_dir_each)
#             # print('getcwd', os.getcwd())

# 內文 =====
            try:
                url_back = title_txt[n]['href'][12:]
                url_article = 'https://www.mobile01.com/topicdetail.' + url_back

                req_con = request.Request(url=url_article, headers=headers)
                res_con = request.urlopen(req_con)
                soup_con = BeautifulSoup(res_con, 'html.parser')
                # print('soup_con:', soup_con)

                article = soup_con.select('div[itemprop="articleBody"] ')[0].text.strip()
                article_1 = ('{"文章內容":"' + article + '"}')

                postdate = soup_con.select('span[class="o-fNotes o-fSubMini"]')[0].text
                postdate_1 = ('{"發文日期":"' + postdate + '"}')

            except:
                print('article or postdate pass')


# 圖片 =====(要抓圖片時取消此段註解即可)
#             try:
#                 url_back = title_txt[n]['href'][12:]
#                 url_article = 'https://www.mobile01.com/topicdetail.' + url_back

#                 req_con = request.Request(url=url_article, headers=headers)
#                 res_con = request.urlopen(req_con)
#                 soup_con = BeautifulSoup(res_con, 'html.parser')
#                 pic_txt_0 = soup_con.select('div[itemprop="articleBody"] img[class="lazy"]')[0:]
#                 # print('pic_txt_0:', pic_txt_0)
#                 serial = url_article.split('=')[-1]

#             except:
#                 print('url_article pass')

#             if not os.path.exists(path_dir_each):
#                 os.mkdir(path_dir_each)
#             os.chdir(path_dir_each)

#             for pic in pic_txt_0:
#                 pic_url_head = pic['data-src'][0:6]
#                 # print('pic_url_head:', pic_url_head)

#                 if pic_url_head == 'https:':
#                     pic_url = pic['data-src']

#                 elif pic_url_head == '//atta':
#                     pic_url = 'http:' + str(pic['data-src'][0:])
#                     # print('elif:', pic_url)

#                 else:
#                     pic_url = 'http://www.nodata.com'

#                 try:
#                     request.urlretrieve(pic_url, 'pic_' + serial + '_' + str(pic_txt_0.index(pic)+1) + '.jpg')

#                 except:
#                     print('pic pass')

# 存檔 =====
            if not os.path.exists(path_dir + 'txt'):
                os.mkdir(path_dir + 'txt')
            os.chdir(path_dir +'txt')
            f = open(title_save + '.txt', mode='a', encoding='utf8')
            # f.write(url_article_1)  # 寫入網址

            total = url_article_1 + '\n' + postdate_1 + '\n' + title + '\n' + '{"景點名稱":"NA"}' + '\n' + article_1 + \
                    '\n' + '{"留言":"NA"}' + '\n' + '{"地址":"NA"}' + '\n' +\
                    '{"縣市":"' + area.get(int(num)) + '"}' + '\n' + '-----'+ '\n'

            f.write(total)
            print('Page', page, title + url_article_1 +' 存檔完成')

    time.sleep(random.randint(1, 3))
    page += 1

print(area.get(int(num)) + ' 所有文章存檔完成!!! at', time.asctime())

"""存檔格式
{
"文章網址": "",
"發文時間": "",
"標題": "",
"景點名稱": "", 
"文章內容": "",  
"留言": ["" ,"",.....],
"地址": "", 
"縣市": "",
}
"""
