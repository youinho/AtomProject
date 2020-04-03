from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

# def __init__(self):
url="http://www.seoul.go.kr/coronaV/coronaStatus.do?menu_code=01"
res=req.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")
seoul_list = soup.select("#move-cont1 > div.status-confirm.map-status.display-none > div > div.seoul-map.seoul-map-all > span.district")

seoul_codes = { '종로구':11110 ,'중구':11140 ,'용산구':11170, '성동구':11200,
                '광진구':11215,'동대문구':11230,'중랑구':11260,'성북구':11290,
                '강북구':11305, '도봉구':11320,'노원구':11350,'은평구':11380,
                '서대문구':11410,'마포구':11440,'양천구':11470,'강서구':11500,
                '구로구':11530,'금천구':11545,'영등포구':11560 ,'동작구':11590 ,
                '관악구':11620,'서초구':11650,'강남구':11680,'송파구':11710,'강동구':11740,'서귀포':'50130A'}

population = []
code = []
for i,e in enumerate(seoul_list):
    locate = e.select_one("em.sr-only").string
    code.append(seoul_codes[locate])
    population.append(e.select_one(".num").string)

code.append('50130A')
population.append(0)

seoul_dict = {'Code':code,'Population':population}
seoul_pd = pd.DataFrame(seoul_dict)

seoul_pd_save_url='resource/seoul_pd.csv'
seoul_pd.to_csv(seoul_pd_save_url,mode='w',index=None)
# print(seoul_pd)
# print(seoul_pd.columns)
# print(seoul_pd)
# print(seoul_codes[
# seoul_codes2=seoul_codes
# seoul_codes2 = dict((value,key) for key,value in seoul_codes2.items())
# search_gu = ()
# print(seoul_codes2)
# print(seoul_codes2[11110])



# if __name__ == "__main__":
#     seoulData = seoul_data()
