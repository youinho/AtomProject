from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io
import re
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="http://www.seoul.go.kr/coronaV/coronaStatus.do"
res=req.urlopen(url).read()
soup = BeautifulSoup(res,"html.parser")
seoul_list = soup.select("#move-cont1 > div.status-confirm.map-status.display-none > div > div.seoul-map.seoul-map-all > span.district")
for i in seoul_list:
    print("지역:",i.select_one("em.sr-only").string)
    print("확진자 수 :",i.select_one(".num").string)





# 양주출력
# print(soup.select("li:nth-of-type(4)")[1].string)
# print(soup.select_one("#ac-list > li:nth-of-type(4)").string)
# # 양주 출력
# param={"data-lo":"cn", "class":"alcohol"}
# print(soup.find("li", param).string)
# print(soup.find(id="ac-list").find("li", param).string)
#

# # 삼겹살 find
# for ac in soup.find_all("li") :
#     if ac['data-lo']=='us' :
#         print('data-lo==us : ', ac.string)
#
#
# # find_all 필터링=ko
# for fd in soup.find_all("li") :
#     if fd['data-lo']=='ko' :
#         print('data-lo==ko : ', fd.string)
