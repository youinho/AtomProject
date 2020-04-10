import folium
import pandas as pd
import json
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import io
from coding.part3.seoul_data import *
import webbrowser
class seoul_map:
    def __init__(self):
        print(folium.__version__)
        print()
        sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
        # 서울시 행정구역별 geo 파일  출처 : https://data.seoul.go.kr/
        state_geo =os.path.join(os.path.dirname(__file__), '../../resource/seoul_geo.json')
        # state_geo = 'D:/pro/ex/seoul_WGS1984.json'
        #geo json 인코딩후 파일 로드
        geo= json.load(open(state_geo,encoding='utf-8'))
        #실시간 서울 구별 확진자 수 csv 파일 오픈  ( from seoul_data ) 에서 BeautifulSoup 으로 선택자 html parser 구 코드 and 확진사 인원수를 뽑아서 csv 파일로 저장
        #folium 에서 데이터타입이 csv 타입이여야 함
        state_data = pd.read_csv(seoul_pd_save_url,encoding='utf-8')

        # state_data = seoul_pd
        # for i in range(len(state_data)):
        #     state_data.loc[i,"Code"]=str(state_data.loc[i,"Population"])

        #서울시 구별 확진자데이터 확인
        # print(state_date)
        # print(state_date['Code'])
        # print(state_date['Population'])
        # print(state_date.columns)

        # 맵 위치 시작 지점, 맵 스타일 설정
        m = folium.Map(
            location=[37.5838699,127],
            zoom_start=11.1,
            tiles="OpenStreetMap"



        )

# with open('seoul_WGS1984.json',mode='rt',encoding='utf-8') as f:
#     geo = json.loads(f.read())
#     f.close()

        #서울 확진사수 비율을 구별로 색칠
        m1=folium.Choropleth(
         geo_data=geo,
         data=state_data,
         columns=['Code','Population'],
         fill_color='YlOrRd', # 비율별 색깔 노랑->오렌지 -> 빨강
         key_on='feature.properties.SIG_CD', # 구 코드에 맵핑
         highlight=True,  #마우스오버 효과 설정
         fill_opacity=0.7, # 색 투명도
         line_opacity=1, #구 나눔 선 투명도
         legend_name='COVID-19 Confirmer (인원)' # 비율 표시
         ).add_to(m)  # 저장
        folium.Marker(
          location=[37.591793, 126.970535],
           popup=folium.Popup('<a href="https://www.jongno.go.kr/"target="_blank">'+self.cal_popu(state_data,"종로구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='종로구'
        ).add_to(m)

        folium.Marker(
          location=[37.560039, 126.995876],
          popup=folium.Popup('<a href="http://www.junggu.seoul.kr/index.jsp"target="_blank">'+self.cal_popu(state_data,"중구")+'명'+'</a>'),
          icon=folium.Icon(color='red',icon='star'),
          tooltip='중구'
        ).add_to(m)

        folium.Marker(
          location=[37.531504, 126.980477],
           popup=folium.Popup('<a href="http://www.yongsan.go.kr/index.htm"target="_blank">'+self.cal_popu(state_data,"용산구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='용산구'
        ).add_to(m)

        folium.Marker(
          location=[37.551145, 127.040495],
           popup=folium.Popup('<a href="https://www.sd.go.kr/sd/intro.do"target="_blank">'+self.cal_popu(state_data,"성동구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='성동구'
        ).add_to(m)

        folium.Marker(
          location=[37.545862, 127.086300],
           popup=folium.Popup('<a href="https://www.gwangjin.go.kr/index1.html"target="_blank">'+self.cal_popu(state_data,"광진구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='광진구'
        ).add_to(m)
        folium.Marker(
          location=[37.582188, 127.055998],
           popup=folium.Popup('<a href="https://www.ddm.go.kr/"target="_blank">'+self.cal_popu(state_data,"동대문구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='동대문구'
        ).add_to(m)


        folium.Marker(
          location=[37.598109, 127.092874],
           popup=folium.Popup('<a href="https://www.jungnang.go.kr/intro.jsp"target="_blank">'+self.cal_popu(state_data,"중랑구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='중랑구'
        ).add_to(m)

        folium.Marker(
          location=[37.606107, 127.017625],
           popup=folium.Popup('<a href="http://www.sb.go.kr/"target="_blank">'+self.cal_popu(state_data,"성북구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='성북구'
        ).add_to(m)

        folium.Marker(
          location=[37.639645, 127.011943],
           popup=folium.Popup('<a href="http://www.gangbuk.go.kr/intro_gb.jsp"target="_blank">'+self.cal_popu(state_data,"강북구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='강북구'
        ).add_to(m)

        folium.Marker(
          location=[37.669217, 127.032275],
           popup=folium.Popup('<a href="http://www.dobong.go.kr/"target="_blank">'+self.cal_popu(state_data,"도봉구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='도봉구'
        ).add_to(m)

        folium.Marker(
          location=[37.652695, 127.075081],
          popup=folium.Popup('<a href="http://www.nowon.kr/"target="_blank">'+self.cal_popu(state_data,"노원구")+'명'+'</a>'),
          icon=folium.Icon(color='red',icon='star'),
          tooltip='노원구'
        ).add_to(m)

        folium.Marker(
          location=[37.619137, 126.926804],
           popup=folium.Popup('<a href="http://www.ep.go.kr/CmsWeb/viewPage.req?idx=PG0000001180"target="_blank">'+self.cal_popu(state_data,"은평구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='은평구'
        ).add_to(m)
        folium.Marker(
          location=[37.578073, 126.940295],
           popup=folium.Popup('<a href="https://www.sdm.go.kr/index.do"target="_blank">'+self.cal_popu(state_data,"서대문구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='서대문구'
        ).add_to(m)

        folium.Marker(
          location=[37.560197, 126.908567],
           popup=folium.Popup('<a href="http://www.mapo.go.kr/html/corona/intro.htm"target="_blank">'+self.cal_popu(state_data,"마포구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='마포구'
        ).add_to(m)

        folium.Marker(
          location=[37.522685, 126.854648],
           popup=folium.Popup('<a href="http://www.yangcheon.go.kr/html/index_corona.html"target="_blank">'+self.cal_popu(state_data,"양천구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='양천구'
        ).add_to(m)

        folium.Marker(
          location=[37.561433, 126.820492],
           popup=folium.Popup('<a href="http://www.gangseo.seoul.kr/new_portal/index.jsp"target="_blank">'+self.cal_popu(state_data,"강서구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='강서구'
        ).add_to(m)

        folium.Marker(
          location=[37.494611, 126.842694],
           popup=folium.Popup('<a href="http://www.guro.go.kr/"target="_blank">'+self.cal_popu(state_data,"구로구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='구로구'
        ).add_to(m)

        folium.Marker(
          location=[37.460973, 126.900647],
           popup=folium.Popup('<a href="https://www.geumcheon.go.kr/"target="_blank">'+self.cal_popu(state_data,"금천구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='금천구'
        ).add_to(m)

        folium.Marker(
          location=[37.522054, 126.909206],
         popup=folium.Popup('<a href="https://www.ydp.go.kr/site/corona/index.html"target="_blank">'+self.cal_popu(state_data,"영등포구")+'명'+'</a>'),
         icon=folium.Icon(color='red',icon='star'),
         tooltip='영등포구'
        ).add_to(m)
        folium.Marker(
          location=[37.504018, 126.950223],
          popup=folium.Popup('<a href="http://www.dongjak.go.kr/index.jsp#n"target="_blank">'+self.cal_popu(state_data,"동작구")+'명'+'</a>'),
          icon=folium.Icon(color='red',icon='star'),
          tooltip='동작구'
        ).add_to(m)

        folium.Marker(
          location=[37.467795, 126.947435],
           popup=folium.Popup('<a href="https://www.gwanak.go.kr/"target="_blank">'+self.cal_popu(state_data,"관악구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='관악구'
        ).add_to(m)

        folium.Marker(
                  location=[37.473886, 127.029650],
                  popup=folium.Popup('<a href="http://www.seocho.go.kr/index.jsp#n"target="_blank">'+self.cal_popu(state_data,"서초구")+'명'+'</a>'),
                  icon=folium.Icon(color='red',icon='star'),
                  tooltip='서초구'
                 ).add_to(m)
        # print(list(list(state_data['Code'])))
        # print(list(state_data['Code']))

        folium.Marker(
          location=[37.496435, 127.061931],
           popup=folium.Popup('<a href="https://www.gangnam.go.kr/index.htm"target="_blank">'+self.cal_popu(state_data,"강남구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='강남구'
        ).add_to(m)

        folium.Marker(
          location=[37.506706, 127.112769],
           popup=folium.Popup('<a href="http://www.songpa.go.kr/index.jsp#n"target="_blank">'+self.cal_popu(state_data,"송파구")+'명'+'</a>'),
           icon=folium.Icon(color='red',icon='star'),
           tooltip='송파구'
        ).add_to(m)

        folium.Marker(
          location=[37.551310, 127.144418],
          popup=folium.Popup('<a href="https://www.gangdong.go.kr/"target="_blank">'+self.cal_popu(state_data,"강동구")+'명'+'</a>'),
          icon=folium.Icon(color='red',icon='star'),
          tooltip='강동구',

        ).add_to(m)
        m1.geojson.add_child(
            folium.features.GeoJsonTooltip(fields=['SIG_KOR_NM'],
                                           aliases=["구 :"])
        )

        self.path = 'resource/coronamap_seoul.html'

        #html  파일로 변환 저장
        m.save(self.path)
        print('완료')
    def cal_popu(self,state_data,location):
        return str(state_data["Population"][list(state_data['Code']).index(str(seoul_codes[location]))])



    def geturl(self):
        self.path='resource/coronamap_seoul.html'
        return self.path
        # return self.path


if __name__ == "__main__":
    seoul_map = seoul_map()
    seoul_map.geturl()
