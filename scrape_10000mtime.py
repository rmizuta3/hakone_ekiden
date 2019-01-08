import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import pandas as pd
import csv
import copy

#webdriverのオプション設定
options = Options()
# 必須
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# エラーの許容
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--disable-web-security')
# 言語
options.add_argument('--lang=ja')
# 画像を読み込まないで軽くする
options.add_argument('--blink-settings=imagesEnabled=false')

# ChromeのWebDriverオブジェクトを作成する。
b = webdriver.Chrome('./chromedriver',chrome_options=options)
# ページ推移

b.get('http://www13.plala.or.jp/jwmiurat/senryoku/senryoku_m.html')
#b.get('http://www13.plala.or.jp/jwmiurat/yosou/entry_hon.html')

time.sleep(1)

#print(b.page_source)
soup = BeautifulSoup(b.page_source, "html5lib")
#テーブルを指定
table = soup.findAll("table")[0]
rows = table.findAll("tr")

#ファイル書き込み
#f = open("10000m.csv", 'wt')
f = open("10000m_2018.csv", 'wt')
writer = csv.writer(f)

for row in rows:
    csvRow = []
    for cell in row.findAll(['td', 'th']):
        csvRow.append(cell.get_text())
    writer.writerow(csvRow)
f.close()

#不要なものも含まれるためcsvファイルは後に手動で加工
