# Import libraries
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import pandas as pd
import folium
import webbrowser
import json
from coding.part3.Korea_data import *

class korea_map:
    def __init__(self):
        # print(folium.__version__)
        # print()
        state_geo =os.path.join(os.path.dirname(__file__), '../../resource/korea_geo.json')
        geo= json.load(open(state_geo,encoding='utf-8'))
        # 대한민국 전국 확진자데이터 from Korea_data(korea_pd.csv)
        state_data = pd.read_csv(korea_pd_save_url)
        # print(geo)
        # Initialize the map:
        m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)

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

        m1=folium.Choropleth(
         geo_data=geo,
         name='choropleth',
         data=state_data,
         columns=['Code', 'Population'],
         key_on='feature.properties.CTP_KOR_NM',
         fill_color='YlGn',
         threshold_scale=[0,100,200,400,500,1000,1500,8000],
         fill_opacity=0.7,
         line_opacity=0.5,
         legend_name='코로나 확진자 (명)'
        ).add_to(m)
        m1.geojson.add_child(
            folium.features.GeoJsonTooltip(fields=['CTP_KOR_NM'],
                                           aliases=["지역 :"])
        )

        folium.LayerControl().add_to(m)

        # Save to html
        self.path='resource/coronamap_korea.html'
        m.save('resource/coronamap_korea.html')
        print('완료')

    def geturl(self):
        return self.path


if __name__ == "__main__":
    korea_map = korea_map()
    korea_map.geturl()
    # browser=webdriver.Chrome("D:/section7/webdriver/chrome/chromedriver.exe")
    # browser.get(window.url)
