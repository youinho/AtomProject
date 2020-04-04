
# Import libraries
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import pandas as pd
import folium
import webbrowser
import json
from coding.part3.trip_ban_data import *
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
# You have to download this file and set the directory where you saved it

class world_map:
    def __init__(self):
        # print(folium.__version__)
        # print()
        state_geo =os.path.join(os.path.dirname(__file__), '../../resource/world5.json')
        geo= json.load(open(state_geo,encoding='utf-8'))
        #세계 여행 금지구역 csv 파일 from trip_ban_data (country_ban.csv)
        state_data = pd.read_csv(country_ban_url)
        # print(geo)
        # Initialize the map:
        m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=3)

        # Add the color for the chloropleth:
        Set3  = {
            3 : [ 'rgb (141,211,199)' , 'rgb (255,255,179)' , 'rgb (190,186,218)' ],
            4 : [ 'rgb (141,211,199)' , 'rgb (255,255,179)' , 'rgb (190,186,218)' , 'rgb (251,128,114)' ],
            5 : [ 'rgb (141,211,199)' , 'rgb (255,255,179)' , 'rgb (190,186,218)' , 'rgb (251,128,114)' , 'rgb (128,177,211)' ],
            6 : [ 'rgb (141,211,199)' , 'rgb (255,255,179)' , 'rgb (190,186,218)' , 'rgb (251,128,114)' , 'rgb (128,177,211)' , 'rgb (253,180,98)' ],
            7 : [ 'rgb (141,211,199)' , 'rgb (255,255,179)' , 'rgb (190,186,218)' , 'rgb (251,128,114)' , 'rgb (128,177,211)' , 'rgb (253,180,98)' , 'rgb ( 179,222,105) ' ],
            8 : [ 'rgb (141,211,199)' , 'rgb (255,255,179)' , 'rgb (190,186,218)' , 'rgb (251,128,114)' , 'rgb (128,177,211)' , 'rgb (253,180,98)' , 'rgb ( 179,222,105) ' , 'rgb (252,205,229) ' ],
            9 : [ 'rgb (141,211,199)' , 'rgb (255,255,179)' , 'rgb (190,186,218)' , 'rgb (251,128,114)' , 'rgb (128,177,211)' , 'rgb (253,180,98)' , 'rgb ( 179,222,105) ' , 'rgb (252,205,229) ' , 'rgb (217,217,217) ' ],
            10 : [ 'rgb (141,211,199)' , 'rgb (255,255,179)' , 'rgb (190,186,218)' , 'rgb (251,128,114)' , 'rgb (128,177,211)' , 'rgb (253,180,98)' , 'rgb ( 179,222,105) ' , 'rgb (252,205,229) ' , 'rgb (217,217,217) ' , 'rgb (188,128,189) ' ],
            11 : [ 'rgb (141,211,199)' , 'rgb (255,255,179)' , 'rgb (190,186,218)' , 'rgb (251,128,114)' , 'rgb (128,177,211)' , 'rgb (253,180,98)' , 'rgb ( 179,222,105) ' , 'rgb (252,205,229) ' , 'rgb (217,217,217) ' , 'rgb (188,128,189) ' , 'rgb (204,235,197) ' ],
            12 : [ 'rgb (141,211,199)' , 'rgb (255,255,179)' , 'rgb (190,186,218)' , 'rgb (251,128,114)' , 'rgb (128,177,211)' , 'rgb (253,180,98)' , 'rgb ( 179,222,105) ' , 'rgb (252,205,229) ' , 'rgb (217,217,217) ' , 'rgb (188,128,189) ' , 'rgb (204,235,197) ' , 'rgb (255,237,111) ' ]
        }
        # tooltip=folium.features.Tooltip(fields=['feature.properties.NAME'])
        m1 =folium.Choropleth(
         geo_data=geo,
         name='m1',
         data=state_data,
         columns=['name', 'ban'],
         # tooltip=folium.features.GeoJsonTooltip(
         #            fields=['name'],
         #            aliases=['country name : '],
         #              labels=True,
         #              sticky=True
         #        ),
         nan_fill_color='#ffffff',
         nan_fill_opacity=0.9,
         key_on='feature.properties.NAME',
         fill_color='OrRd',
         fill_opacity=0.7,
         line_opacity=0.5,
         legend_name='여행 금지 국가'
        ).add_to(m)
        #마우스오버 나라이름
        m1.geojson.add_child(
            folium.features.GeoJsonTooltip(fields=['NAME'],
                                           aliases=["country :"])
        )



        folium.LayerControl().add_to(m)
        self.path = 'resource/country_ban.html'
        # Save to html 파일
        m.save(self.path)
        print('완료')
        # webbrowser.open_new("country_ban.html")


    def geturl(self):
        return self.path



if __name__ == "__main__":
    world_map = world_map()
    world_map.geturl()
    # browser=webdriver.Chrome("D:/section7/webdriver/chrome/chromedriver.exe")
    # browser.get(window.url)
