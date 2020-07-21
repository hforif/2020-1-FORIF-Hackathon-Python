import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import random

main_class = uic.loadUiType('C:/catplanner/ui/Main_window.ui')[0]
set_class = uic.loadUiType('C:/catplanner/ui/set_sched.ui')[0]
lookup_class = uic.loadUiType('C:/catplanner/ui/check_sced.ui')[0]

studycat = uic.loadUiType("C:/catplanner/ui/cat1.ui")[0]
moneycat = uic.loadUiType("C:/catplanner/ui/cat2.ui")[0]
sleepcat = uic.loadUiType("C:/catplanner/ui/cat3.ui")[0]
foodcat = uic.loadUiType("C:/catplanner/ui/cat4.ui")[0]
funcat = uic.loadUiType("C:/catplanner/ui/cat5.ui")[0]
outsidecat = uic.loadUiType("C:/catplanner/ui/cat6.ui")[0]
undongcat = uic.loadUiType("C:/catplanner/ui/cat7.ui")[0]
cleancat = uic.loadUiType("C:/catplanner/ui/cat8.ui")[0]

plan_list = []

clean_cat= {'xp':0, 'level':1, 'quest':['쓰레기 버리기','방청소하기','대청소하기'],'category':'청소'}
eat_cat = {'xp':0, 'level':1, 'quest':['집밥먹기','반찬만들기','군것질 하지 않기'],'category':'식단'}
fun_cat = {'xp':0, 'level':1, 'quest':['친구와 전화하기','컴퓨터게임하기','보드게임하기'],'category':'오락'}
goout_cat = {'xp':0, 'level':1, 'quest':['마스크쓰고 나가기','손소독제휴대하기','기침가리고 하기'],'category':'외출'}
money_cat = {'xp':0, 'level':1, 'quest': ['충동구매 금지','돈쓰지 않기','현질하지 않기'],'category':'돈'}
sleep_cat = {'xp':0, 'level':1, 'quest': ['6시간 숙면취하기','일찍 일어나기','일찍 잠들기'],'category':'수면'}
study_cat = {'xp':0, 'level':1, 'quest':['과제하기','영단어 30개 외우기','문제집 5장 풀기'],'category':'공부'}
workout_cat = {'xp':0, 'level':1, 'quest' :['스쿼트하기','줄넘기하기','스트레칭하기'],'category':'운동'}


cat_group = [clean_cat,eat_cat,fun_cat,goout_cat,money_cat,sleep_cat,study_cat,workout_cat]

class LookUp(QDialog, lookup_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        background = QImage('C:/catplanner/images/일정조회하기.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)
        self.setWindowTitle("일정 로그 조회")
        self.date_choose.setMinimumDate(QDate.currentDate())
        self.sced_table.setColumnWidth(0,200)
        self.sced_table.setColumnWidth(1,100)
        self.sced_table.setColumnWidth(2,120)
        self.sced_table.setColumnWidth(3,60)
        log_count = 0
        global plan_list

        for plan in plan_list:
            if plan.get("date").__eq__(self.date_choose.date()):
                self.sced_table.insertRow(log_count)
                time_str = plan.get("start_time").toString('AP hh시 mm분')+'~'+plan.get("end_time").toString('AP hh시 mm분')
                self.sced_table.setItem(log_count, 0, QTableWidgetItem(time_str))
                self.sced_table.setItem(log_count, 1, QTableWidgetItem(plan.get("category")))
                self.sced_table.setItem(log_count, 2, QTableWidgetItem(plan.get("content")))
                self.sced_table.setItem(log_count, 3, QTableWidgetItem(plan.get("difficulty")))
                log_count += 1

        self.date_choose.setMinimumDate(QDate.currentDate())
        self.date_choose.dateChanged.connect(self.addToTable)

    def addToTable(self):
        print(0)
        for i in range(self.sced_table.rowCount()):
            self.sced_table.removeRow(0)
        print(1)
        log_count = 0
        global plan_list
        for plan in plan_list:
            if plan.get("date").__eq__(self.date_choose.date()):
                self.sced_table.insertRow(log_count)
                time_str = plan.get("start_time").toString('AP hh시 mm분')+'~'+plan.get("end_time").toString('AP hh시 mm분')
                self.sced_table.setItem(log_count, 0, QTableWidgetItem(time_str))
                self.sced_table.setItem(log_count, 1, QTableWidgetItem(plan.get("category")))
                self.sced_table.setItem(log_count, 2, QTableWidgetItem(plan.get("content")))
                self.sced_table.setItem(log_count, 3, QTableWidgetItem(plan.get("difficulty")))
                log_count += 1
                



class Studycat(QDialog, studycat):
    global cat_group
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("공부냥이")
        background = QImage('C:/catplanner/images/공부냥이.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)
        
    
        self.exp_progressBar.setRange(0,10)
        self.exp_progressBar.setValue(cat_group[6]['xp'])
        self.label_4.setText(str(cat_group[6]['level']))
    

        log_count = 0
        global plan_list
        for plan in plan_list:
            if plan.get("date") .__eq__(QDate.currentDate()) and plan.get("category") == '공부' :
                self.tableWidget.insertRow(log_count)
                self.tableWidget.setItem(log_count, 0, QTableWidgetItem(plan.get("date").toString('yyyy-MM-dd')))
                time_str = plan.get("start_time").toString('AP hh시 mm분')+'~'+plan.get("end_time").toString('AP hh시 mm분')
                self.tableWidget.setItem(log_count, 1, QTableWidgetItem(time_str))
                self.tableWidget.setItem(log_count, 2, QTableWidgetItem(plan.get("category")))
                self.tableWidget.setItem(log_count, 3, QTableWidgetItem(plan.get("content")))
                self.tableWidget.setItem(log_count, 4, QTableWidgetItem(plan.get("difficulty")))
                log_count += 1

        #self.Cat1_btn_clicked(self.Studycheck)


class Moneycat(QDialog, moneycat):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("돈냥이")
        background = QImage('C:/catplanner/images/돈냥이.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)

        self.exp_progressBar.setRange(0,10)
        self.exp_progressBar.setValue(cat_group[4]['xp'])
        self.label_4.setText(str(cat_group[4]['level']))

        log_count = 0
        global plan_list
        for plan in plan_list:
            if plan.get("date") .__eq__(QDate.currentDate()) and plan.get("category") == '돈' :
                self.tableWidget.insertRow(log_count)
                self.tableWidget.setItem(log_count, 0, QTableWidgetItem(plan.get("date").toString('yyyy-MM-dd')))
                time_str = plan.get("start_time").toString('AP hh시 mm분')+'~'+plan.get("end_time").toString('AP hh시 mm분')
                self.tableWidget.setItem(log_count, 1, QTableWidgetItem(time_str))
                self.tableWidget.setItem(log_count, 2, QTableWidgetItem(plan.get("category")))
                self.tableWidget.setItem(log_count, 3, QTableWidgetItem(plan.get("content")))
                self.tableWidget.setItem(log_count, 4, QTableWidgetItem(plan.get("difficulty")))
                log_count += 1
        #self.Cat2_btn_clicked(self.Moneycheck)


class Sleepcat(QDialog, sleepcat):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("수면냥이")
        background = QImage('C:/catplanner/images/수면냥이.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)

        self.exp_progressBar.setRange(0,10)
        self.exp_progressBar.setValue(cat_group[5]['xp'])
        self.label_4.setText(str(cat_group[5]['level']))

        log_count = 0
        global plan_list
        for plan in plan_list:
            if plan.get("date") .__eq__(QDate.currentDate()) and plan.get("category") == '수면' :
                self.tableWidget.insertRow(log_count)
                self.tableWidget.setItem(log_count, 0, QTableWidgetItem(plan.get("date").toString('yyyy-MM-dd')))
                time_str = plan.get("start_time").toString('AP hh시 mm분')+'~'+plan.get("end_time").toString('AP hh시 mm분')
                self.tableWidget.setItem(log_count, 1, QTableWidgetItem(time_str))
                self.tableWidget.setItem(log_count, 2, QTableWidgetItem(plan.get("category")))
                self.tableWidget.setItem(log_count, 3, QTableWidgetItem(plan.get("content")))
                self.tableWidget.setItem(log_count, 4, QTableWidgetItem(plan.get("difficulty")))
                log_count += 1
        #self.Cat3_btn_clicked(self.Sleepcheck)


class Foodcat(QDialog, foodcat):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("식단냥이")
        background = QImage('C:/catplanner/images/식사냥이.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)

        self.exp_progressBar.setRange(0,10)
        self.exp_progressBar.setValue(cat_group[1]['xp'])
        self.label_4.setText(str(cat_group[1]['level']))

        log_count = 0
        global plan_list
        for plan in plan_list:
            if plan.get("date") .__eq__(QDate.currentDate()) and plan.get("category") == '식사' :
                self.tableWidget.insertRow(log_count)
                self.tableWidget.setItem(log_count, 0, QTableWidgetItem(plan.get("date").toString('yyyy-MM-dd')))
                time_str = plan.get("start_time").toString('AP hh시 mm분')+'~'+plan.get("end_time").toString('AP hh시 mm분')
                self.tableWidget.setItem(log_count, 1, QTableWidgetItem(time_str))
                self.tableWidget.setItem(log_count, 2, QTableWidgetItem(plan.get("category")))
                self.tableWidget.setItem(log_count, 3, QTableWidgetItem(plan.get("content")))
                self.tableWidget.setItem(log_count, 4, QTableWidgetItem(plan.get("difficulty")))
                log_count += 1

        #self.Cat4_btn_clicked(self.Foodcheck)


class Funcat(QDialog, funcat):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("오락냥이")
        background = QImage('C:/catplanner/images/오락냥이.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)

        self.exp_progressBar.setRange(0,10)
        self.exp_progressBar.setValue(cat_group[2]['xp'])
        self.label_4.setText(str(cat_group[2]['level']))

        log_count = 0
        global plan_list
        for plan in plan_list:
            if plan.get("date") .__eq__(QDate.currentDate()) and plan.get("category") == '오락' :
                self.tableWidget.insertRow(log_count)
                self.tableWidget.setItem(log_count, 0, QTableWidgetItem(plan.get("date").toString('yyyy-MM-dd')))
                time_str = plan.get("start_time").toString('AP hh시 mm분')+'~'+plan.get("end_time").toString('AP hh시 mm분')
                self.tableWidget.setItem(log_count, 1, QTableWidgetItem(time_str))
                self.tableWidget.setItem(log_count, 2, QTableWidgetItem(plan.get("category")))
                self.tableWidget.setItem(log_count, 3, QTableWidgetItem(plan.get("content")))
                self.tableWidget.setItem(log_count, 4, QTableWidgetItem(plan.get("difficulty")))
                log_count += 1

        #self.Cat5_btn_clicked(self.Funcheck)


class Outsidecat(QDialog, outsidecat):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("외출냥이")
        background = QImage('C:/catplanner/images/외출냥이.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)
        
        self.exp_progressBar.setRange(0,10)
        self.exp_progressBar.setValue(cat_group[3]['xp'])
        self.label_4.setText(str(cat_group[3]['level']))

        log_count = 0
        global plan_list
        for plan in plan_list:
            if plan.get("date") .__eq__(QDate.currentDate()) and plan.get("category") == '외출' :
                self.tableWidget.insertRow(log_count)
                self.tableWidget.setItem(log_count, 0, QTableWidgetItem(plan.get("date").toString('yyyy-MM-dd')))
                time_str = plan.get("start_time").toString('AP hh시 mm분')+'~'+plan.get("end_time").toString('AP hh시 mm분')
                self.tableWidget.setItem(log_count, 1, QTableWidgetItem(time_str))
                self.tableWidget.setItem(log_count, 2, QTableWidgetItem(plan.get("category")))
                self.tableWidget.setItem(log_count, 3, QTableWidgetItem(plan.get("content")))
                self.tableWidget.setItem(log_count, 4, QTableWidgetItem(plan.get("difficulty")))
                log_count += 1

        #self.Cat6_btn_clicked(self.Outsidecheck)


class Undongcat(QDialog, undongcat):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("운동냥이")
        background = QImage('C:/catplanner/images/운동냥이.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)

        self.exp_progressBar.setRange(0,10)
        self.exp_progressBar.setValue(cat_group[7]['xp'])
        self.label_4.setText(str(cat_group[7]['level']))

        log_count = 0
        global plan_list
        for plan in plan_list:
            if plan.get("date") .__eq__(QDate.currentDate()) and plan.get("category") == '운동' :
                self.tableWidget.insertRow(log_count)
                self.tableWidget.setItem(log_count, 0, QTableWidgetItem(plan.get("date").toString('yyyy-MM-dd')))
                time_str = plan.get("start_time").toString('AP hh시 mm분')+'~'+plan.get("end_time").toString('AP hh시 mm분')
                self.tableWidget.setItem(log_count, 1, QTableWidgetItem(time_str))
                self.tableWidget.setItem(log_count, 2, QTableWidgetItem(plan.get("category")))
                self.tableWidget.setItem(log_count, 3, QTableWidgetItem(plan.get("content")))
                self.tableWidget.setItem(log_count, 4, QTableWidgetItem(plan.get("difficulty")))
                log_count += 1

        #self.Cat7_btn_clicked(self.Undongcheck)


class Cleancat(QDialog, cleancat):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("청소냥이")
        background = QImage('C:/catplanner/images/청소냥이.png')
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)

        self.exp_progressBar.setRange(0,10)
        self.exp_progressBar.setValue(cat_group[0]['xp'])
        self.label_4.setText(str(cat_group[0]['level']))

        log_count = 0
        global plan_list
        for plan in plan_list:
            if plan.get("date") .__eq__(QDate.currentDate()) and plan.get("category") == '청소' :
                self.tableWidget.insertRow(log_count)
                self.tableWidget.setItem(log_count, 0, QTableWidgetItem(plan.get("date").toString('yyyy-MM-dd')))
                time_str = plan.get("start_time").toString('AP hh시 mm분')+'~'+plan.get("end_time").toString('AP hh시 mm분')
                self.tableWidget.setItem(log_count, 1, QTableWidgetItem(time_str))
                self.tableWidget.setItem(log_count, 2, QTableWidgetItem(plan.get("category")))
                self.tableWidget.setItem(log_count, 3, QTableWidgetItem(plan.get("content")))
                self.tableWidget.setItem(log_count, 4, QTableWidgetItem(plan.get("difficulty")))
                log_count += 1

        #self.Cat8_btn_clicked(self.Cleancatcheck)



class Set (QDialog, set_class):
    def __init__(self, _table):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("일정 추가하기")
        oimage = QImage('C:/catplanner/images/일정만들기.png')
        palette = QPalette()
        palette.setBrush(10,QBrush(oimage))
        self.setPalette(palette)
        self.set_sche_btn.setStyleSheet('''QPushButton{image:url(C:/catplanner/images/set_sche_btn1.png); border:0px;}
                                        QPushButton:hover{image:url(C:/catplanner/images/set_sche_btn2.png); border:0px;}''')
        
        self.dateEdit.setMinimumDate(QDate.currentDate())
        self.set_sche_btn.clicked.connect(lambda state, table=_table :self.set_sched(state, table))

    def set_sched (self, state, table):
        global plan_list   
        new_plan = {"date":self.dateEdit.date(), "start_time":self.timeEdit_start.time(),
                    "end_time":self.timeEdit_finish.time(), "category":self.comboBoxss.currentText(),
                    "content":self.lineEdit.text(), "difficulty":self.spinBox.value()}

        index = 1
        for plan in plan_list:
            if new_plan.get("date").__gt__(plan.get("date")):
                index += 1
            elif new_plan.get("date").__eq__(plan.get("date")):
                if new_plan.get("start_time").__gt__(plan.get("start_time")):
                    index += 1
                else: break
            else: break
        plan_list.insert(index, new_plan)

        ans = QMessageBox.question(self, "일정 기록 완료!", "일정이 추가되었습니다.\n일정 목록을 조회하러 가시겠습니까?",
                                   QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.No:
            self.close()

        else:
            self.close()
            lookup_window = LookUp()
            lookup_window.show()
            lookup_window.exec()
     
        if new_plan.get("date").__eq__(QDate.currentDate()):
            table.insertRow(index)
            time_str=new_plan.get("start_time").toString("AP hh시 mm분")+'~'+new_plan.get("end_time").toString("AP hh시 mm분")
            table.setItem(index, 0, QTableWidgetItem(time_str))
            table.setItem(index, 1, QTableWidgetItem(new_plan.get("category")))
            table.setItem(index, 2, QTableWidgetItem(new_plan.get("content")))

            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            table.setItem(index, 3, item)
        



        
class Main(QMainWindow,main_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('고양이가 세상을 "집"애한다')
        oImage = QImage('C:/catplanner/images/background image.png')
        palette = QPalette()
        palette.setBrush(10,QBrush(oImage))
        self.setPalette(palette)
        self.set_sche_btn.setStyleSheet(
            '''QPushButton{image:url(C:/catplanner/images/set_btn_1.png); border:0px;}
                QPushButton:hover{image:url(C:/catplanner/images/set_btn_2.png); border:0px;}''')
        self.Lookup_schedule_btn.setStyleSheet(
            '''QPushButton{image:url(C:/catplanner/images/lookup_btn_1.png); border:0px;}
                QPushButton:hover{image:url(C:/catplanner/images/lookup_btn_2.png); border:0px;}''')
        
        #고양이 프로필 버튼
        self.Cat_profile_btn_1.setStyleSheet(
            '''QPushButton{image:url(C:/catplanner/images/공부냥이1.png); border:0px;}
QPushButton:hover{image:url(C:/catplanner/images/공부냥이2.png); border:0px;}''')       
        self.Cat_profile_btn_2.setStyleSheet(
            '''QPushButton{image:url(C:/catplanner/images/돈냥이1.png); border:0px;}
QPushButton:hover{image:url(C:/catplanner/images/돈냥이2.png); border:0px;}''')
        self.Cat_profile_btn_3.setStyleSheet(
            '''QPushButton{image:url(C:/catplanner/images/수면냥이1.png); border:0px;}
QPushButton:hover{image:url(C:/catplanner/images/수면냥이2.png); border:0px;}''')
        self.Cat_profile_btn_4.setStyleSheet(
            '''QPushButton{image:url(C:/catplanner/images/식사냥이1.png); border:0px;}
QPushButton:hover{image:url(C:/catplanner/images/식사냥이2.png); border:0px;}''')
        self.Cat_profile_btn_5.setStyleSheet(
            '''QPushButton{image:url(C:/catplanner/images/오락냥이1.png); border:0px;}
QPushButton:hover{image:url(C:/catplanner/images/오락냥이2.png); border:0px;}''')
        self.Cat_profile_btn_6.setStyleSheet(
            '''QPushButton{image:url(C:/catplanner/images/외출냥이1.png); border:0px;}
QPushButton:hover{image:url(C:/catplanner/images/외출냥이2.png); border:0px;}''')
        self.Cat_profile_btn_7.setStyleSheet(
            '''QPushButton{image:url(C:/catplanner/images/운동냥이1.png); border:0px;}
QPushButton:hover{image:url(C:/catplanner/images/운동냥이2.png); border:0px;}''')
        self.Cat_profile_btn_8.setStyleSheet(
            '''QPushButton{image:url(C:/catplanner/images/청소냥이1.png); border:0px;}
QPushButton:hover{image:url(C:/catplanner/images/청소냥이2.png); border:0px;}''')

        self.date_tracker.setDate(QDate.currentDate())
        self.create_quest()
        self.Table_widgets.setColumnWidth(0, 200)
        self.Table_widgets.setColumnWidth(1, 100)
        self.Table_widgets.setColumnWidth(2, 120)
        self.Table_widgets.setColumnWidth(3, 50)
                

        self.set_sche_btn.clicked.connect(self.set_sche_btn_clicked)
        self.Lookup_schedule_btn.clicked.connect(self.check_schedule_btn_clicked)
        self.Cat_profile_btn_1.clicked.connect(self.Cat1_btn_clicked)
        self.Cat_profile_btn_2.clicked.connect(self.Cat2_btn_clicked)
        self.Cat_profile_btn_3.clicked.connect(self.Cat3_btn_clicked)
        self.Cat_profile_btn_4.clicked.connect(self.Cat4_btn_clicked)
        self.Cat_profile_btn_5.clicked.connect(self.Cat5_btn_clicked)
        self.Cat_profile_btn_6.clicked.connect(self.Cat6_btn_clicked)
        self.Cat_profile_btn_7.clicked.connect(self.Cat7_btn_clicked)
        self.Cat_profile_btn_8.clicked.connect(self.Cat8_btn_clicked)
        self.date_tracker.dateChanged.connect(self.create_quest)
        self.Table_widgets.itemClicked.connect(self.handleItemClicked)
    def handleItemClicked(self,item):
        item.setFlags(Qt.NoItemFlags)
        global plan_list
        global cat_group
       
        
        if item.row() == 0: #퀘스트 일시
            category = self.Table_widgets.item(0, 1).text()
            

            if category=='청소':
                level=cat_group[0].get('level')
                level+=1
                cat_group[0]['level']=level
                 

            if category == '식단':

                level=cat_group[1].get('level')
                level+=1
                cat_group[1]['level']=level
             

            if category == '오락':
                
                level=cat_group[2].get('level')
                level+=1
                cat_group[2]['level']=level
                    
            if category == '외출':
                
                level=cat_group[3].get('level')
                level+=1
                cat_group[3]['level']=level
                    
            if category == '돈':
                
                level=cat_group[4].get('level')
                level+=1
                cat_group[4]['level']=level
                    
            if category == '수면':
                xp=cat_group[5].get('xp')
                xp+=10
                if xp>=10:
                    xp-=10
                    level=cat_group[5].get('level')
                    level+=1
                    cat_group[5]['level']=level
                    cat_group[5]['xp']=xp
                else:
                    cat_group[5]['xp']=xp

            if category == '공부':
                
                level=cat_group[6].get('level')
                level+=1
                cat_group[6]['level']=level
                   
            if category == '운동':
                
                level=cat_group[7].get('level')
                level+=1
                cat_group[7]['level']=level
                   
            
            
            
        else:
            category = plan_list[item.row()-1].get('category')
            difficulty = plan_list[item.row()-1].get('difficulty')
            
            if category == '청소':
                xp=cat_group[0].get('xp')
                xp+=int(difficulty)
                if xp>=10:
                    xp-=10
                    level=cat_group[0].get('level')
                    level+=1
                    cat_group[0]['level']=level
                    cat_group[0]['xp']=xp
                else:
                    cat_group[0]['xp']=xp

            if category == '식단':
                xp=cat_group[1].get('xp')
                xp+=int(difficulty)
                if xp>=10:
                    xp-=10
                    level=cat_group[1].get('level')
                    level+=1
                    cat_group[1]['level']=level
                    cat_group[1]['xp']=xp
                else:
                    cat_group[1]['xp']=xp

            if category == '오락':
                xp=cat_group[2].get('xp')
                xp+=int(difficulty)
                if xp>=10:
                    xp-=10
                    level=cat_group[2].get('level')
                    level+=1
                    cat_group[2]['level']=level
                    cat_group[2]['xp']=xp
                else:
                    cat_group[2]['xp']=xp

            if category == '외출':
                xp=cat_group[3].get('xp')
                xp+=int(difficulty)
                if xp>=10:
                    xp-=10
                    level=cat_group[3].get('level')
                    level+=1
                    cat_group[3]['level']=level
                    cat_group[3]['xp']=xp
                else:
                    cat_group[3]['xp']=xp

            if category == '돈':
                xp=cat_group[4].get('xp')
                xp+=int(difficulty)
                if xp>=10:
                    xp-=10
                    level=cat_group[4].get('level')
                    level+=1
                    cat_group[4]['level']=level
                    cat_group[4]['xp']=xp
                else:
                    cat_group[4]['xp']=xp

            if category == '수면':
                xp=cat_group[5].get('xp')
                xp+=int(difficulty)
                if xp>=10:
                    xp-=10
                    level=cat_group[5].get('level')
                    level+=1
                    cat_group[5]['level']=level
                    cat_group[5]['xp']=xp
                else:
                    cat_group[5]['xp']=xp

            if category == '공부':
                xp=cat_group[6].get('xp')
                xp+=difficulty
                if xp>=10:
                    xp-=10
                    level=cat_group[6].get('level')
                    level+=1
                    cat_group[6]['level']=level
                    cat_group[6]['xp']=xp
                else:
                    cat_group[6]['xp']=xp

            if category == '운동':
                xp=cat_group[7].get('xp')
                xp+=int(difficulty)
                if xp>=10:
                    xp-=10
                    level=cat_group[7].get('level')
                    level+=1
                    cat_group[7]['level']=level
                    cat_group[7]['xp']=xp
                else:
                    cat_group[7]['xp']=xp          
                    
                    
        
        
    def create_quest(self):
        global cat_group
        category = random.randint(0, 6)
        quest_num = random.randint(0, 2)
        today_quest = cat_group[category].get("quest")[quest_num]
        
        self.quest_label.setText('오늘의 퀘스트: '+ today_quest)
        
        self.Table_widgets.insertRow(0)
        self.Table_widgets.setItem(0, 0 , QTableWidgetItem('오늘 자정까지'))
        self.Table_widgets.setItem(0, 1 , QTableWidgetItem(cat_group[category].get('category')))
        self.Table_widgets.setItem(0, 2 , QTableWidgetItem(today_quest))
        item = QTableWidgetItem()
        item.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
        item.setCheckState(Qt.Unchecked)
        self.Table_widgets.setItem(0, 3, item)
        
    

    def Cat1_btn_clicked(self):  
        cat1_window = Studycat()
        cat1_window.show()
        cat1_window.exec()

    def Cat2_btn_clicked(self):  
        cat2_window = Moneycat()
        cat2_window.show()
        cat2_window.exec()

    def Cat3_btn_clicked(self): 
        cat3_window = Sleepcat()
        cat3_window.show()
        cat3_window.exec()

    def Cat4_btn_clicked(self):
        cat4_window = Foodcat()
        cat4_window.show()
        cat4_window.exec()

    def Cat5_btn_clicked(self):
        cat5_window = Funcat()
        cat5_window.show()
        cat5_window.exec()

    def Cat6_btn_clicked(self):
        cat6_window = Outsidecat()
        cat6_window.show()
        cat6_window.exec()

    def Cat7_btn_clicked(self):
        cat7_window = Undongcat()
        cat7_window.show()
        cat7_window.exec()

    def Cat8_btn_clicked(self):
        cat8_window = Cleancat()
        cat8_window.show()
        cat8_window.exec()

    def check_schedule_btn_clicked(self):
        lookup_window = LookUp()
        lookup_window.show()
        lookup_window.exec()


    def set_sche_btn_clicked(self):
        set_window = Set(self.Table_widgets)
        set_window.show()
        set_window.exec()



if __name__=="__main__":
    app = QApplication(sys.argv)
    main_window = Main()
    main_window.show()
    app.exec_()
