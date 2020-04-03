from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
import sys
import io
import re
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

url="http://ncov.mohw.go.kr"
res=req.urlopen(url).read()
soup=BeautifulSoup(res, "html.parser")
korea = soup.select("#main_maplayout>button")

location = []
population = []

for i,v in enumerate(korea):
    if(i==len(korea)-1):
        break
    location.append(v.select_one("span.name").string)
    population.append(int(v.select_one("span.num").string.replace(",","")))

location.append('독도A')
population.append(0)



korea_dict = {'Code':location,'Population':population}
korea_pd = pd.DataFrame(korea_dict)
korea_pd_save_url='resource/korea_pd.csv'
korea_pd.to_csv(korea_pd_save_url,mode='w',index=None)
