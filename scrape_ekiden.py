import requests
from bs4 import BeautifulSoup
import subprocess
import csv

years=[90,91,92,93,94]

for year in years:
    s = requests.Session()
    r = s.get('http://www.hakone-ekiden.jp/data/data_race.php?racenum={}'.format(year))
    soup = BeautifulSoup(r.text, "lxml")

    #テーブルを指定
    table = soup.findAll("table",{"class":"data_list"})[0]
    rows = table.findAll("tr")

    #ファイル書き込み
    f = open("{}_hakone_result.csv".format(year), 'wt')
    writer = csv.writer(f)

    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
    f.close()
