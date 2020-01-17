import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.load_workbook("award_naver_tv_data.xlsx")
sheet = wb.active

page = 19
while True:
    try:
        raw = requests.get(
            "https://tv.naver.com/search/clip?query=김생민&sort=date&page=" + str(page) + "&isTag=false"
            , headers={"User-Agent": "Mozilla/5.0"})
        page += 1
        html = BeautifulSoup(raw.text, 'html.parser')

        videos = html.select("div.inner")

        for v in videos:
            time = v.select_one("time").text
            if "년" in time:
                time = str(2019 - int(time[0]))
            else:
                time = "2019"
            program_name = v.select_one("span.ch_txt a").text
            hit = v.select_one("span.cds_ifc.cnp").text
            like = v.select_one("span.cds_ifc.bch").text
            hit = hit[4:]
            like = like[5:]
            sheet.append(["김생민", time, program_name, hit, like])
        if page == 41:
            break
    except Exception as e:
        print("비정상종료", e)
        print(page)
        continue

wb.save("award_naver_tv_data.xlsx")
