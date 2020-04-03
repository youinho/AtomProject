from PyQt5 import QtWebEngineWidgets, QtCore
from ui.UI_Main import Ui_MainWindow
from coding.part2.bar import *
from coding.part2.pie import *
from coding.part2.world_page import *
import coding.part2.daily_chart as daily_chart
import coding.part2.total_chart as total_chart
import coding.part3.Coronyang_Korea as map_korea
import coding.part3.Coronyang_Seoul as map_seoul
import coding.part3.Coronyang_world as map_world

class Main(QMainWindow,Ui_MainWindow):
    #생성자
    def __init__(self):
        super().__init__()#부모의 생성자 함수 호출
        # 초기화
        self.setupUi(self)
        # 국내 세계 그래프
        domestic_pie=pie_chart(self.page_local_view_3)
        domestic_bar=bar_chart(self.page_local_view_3)
        world_bar = page_world(self.page_world)
        world_bar.setGeometry(QtCore.QRect(0,70,750,700))
        #차트 붙이기
        self.chart1=daily_chart.daily_chart(self.view_daily_chart)
        self.chart2=total_chart.total_chart(self.view_total_chart)

        #지도 초기화
        self.changeMapView_0()
        # 시그널 초기화
        self.initSignal()
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_local_view.setCurrentIndex(0)

        #메인
        main_list = domestic_pie.getMain()
        self.init_main(main_list)

    def initSignal(self) :
    #----- push버튼 3종세트
        # 로고/타이틀 클릭시 > 홈화면으로
        self.pushButton_logo.clicked.connect(self.changeMain_0)
        # 국내현황
        self.pushButton_local.clicked.connect(self.changeMain_1)
        self.pushButton_local.clicked.connect(self.changeCategory_0)

        # 국내현황 버튼3개
        self.pushButton_category_local_1.clicked.connect(self.changeLocalView_0)
        self.pushButton_category_local_2.clicked.connect(self.changeLocalView_1)
        self.pushButton_category_local_3.clicked.connect(self.changeLocalView_2)


        # 세계현황
        self.pushButton_world.clicked.connect(self.changeMain_1)
        self.pushButton_world.clicked.connect(self.changeCategory_1)

        # 지도
        self.pushButton_map.clicked.connect(self.changeMain_1)
        self.pushButton_map.clicked.connect(self.changeCategory_2)

        # 지도 버튼 3개
        self.pushButton_category_map_1.clicked.connect(self.changeMapView_0)
        self.pushButton_category_map_2.clicked.connect(self.changeMapView_1)
        self.pushButton_category_map_3.clicked.connect(self.changeMapView_2)

        self.pb_home_part1_1.clicked.connect(self.home_part_2)
        self.pb_home_part2.clicked.connect(self.home_part_1)

    #메인화면에 값 넣기
    def init_main(self,list):
        self.label_con_1.setText(list[0])
        self.label_con_2.setText(list[1])
        self.label_con_3.setText("<font color=white>"+list[2][4:]+"</font>")
        self.label_con_4.setText("<font color=white>"+list[3]+"</font>")
        self.label_con_5.setText("<font color=white>"+list[4]+"</font>")
        self.label_con_6.setText("<font color=white>"+list[5]+"</font>")
        self.label_con_7.setText("<font color=white>"+list[6][4:]+"</font>")
        self.label_con_8.setText("<font color=white>"+list[7]+"</font>")
        self.label_con_10.setText("<font color=white>"+list[8]+"</font>")
        self.label_con_9.setText("<font color=white>"+list[9]+"</font>")

    # 홈/메인 전환
    def changeMain_0(self): # 홈
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_local.setEnabled(True)
        self.pushButton_world.setEnabled(True)
        self.pushButton_map.setEnabled(True)

    def changeMain_1(self): # 메인
        self.stackedWidget.setCurrentIndex(1)


    # 메인 >  전환
    def changeCategory_0(self): # 국내
        self.main_category.setCurrentIndex(0)
        self.pushButton_local.setEnabled(False)
        self.pushButton_world.setEnabled(True)
        self.pushButton_map.setEnabled(True)

    def changeCategory_1(self): # 세계
        self.main_category.setCurrentIndex(1)
        self.pushButton_local.setEnabled(True)
        self.pushButton_world.setEnabled(False)
        self.pushButton_map.setEnabled(True)

    def changeCategory_2(self): # 지도
        self.main_category.setCurrentIndex(2)
        self.pushButton_local.setEnabled(True)
        self.pushButton_world.setEnabled(True)
        self.pushButton_map.setEnabled(False)


    # 홈 > 개요/예방수칙
    def home_part_1(self) :
        self.home_view_part.setCurrentIndex(0)

    def home_part_2(self) :
        self.home_view_part.setCurrentIndex(1)


    # 국내 버튼 누르고 > 하단 뷰창
    def changeLocalView_0(self):
        self.stackedWidget_local_view.setCurrentIndex(0)
    def changeLocalView_1(self):
        self.stackedWidget_local_view.setCurrentIndex(1)
    def changeLocalView_2(self):
        self.stackedWidget_local_view.setCurrentIndex(2)

    # 지도 버튼 누르고 > 하단 뷰창
    def changeMapView_0(self):
        #한국
        self.stackedWidget_map_view.setCurrentIndex(1)
        m = map_korea.korea_map()
        path=os.path.join(os.path.dirname(__file__), m.geturl())
        url=QtCore.QUrl.fromLocalFile(path)
        self.webEngine_map_korea.load(url)

    def changeMapView_1(self):
        #서울
        self.stackedWidget_map_view.setCurrentIndex(2)
        s = map_seoul.seoul_map()
        path=os.path.join(os.path.dirname(__file__), s.geturl())
        url=QtCore.QUrl.fromLocalFile(path)
        self.webEngine_map_seoul.load(url)


    def changeMapView_2(self):
        #세계
        self.stackedWidget_map_view.setCurrentIndex(0)
        w = map_world.world_map()
        path=os.path.join(os.path.dirname(__file__), w.geturl())
        url=QtCore.QUrl.fromLocalFile(path)
        self.webEngine_map_world.load(url)



if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
