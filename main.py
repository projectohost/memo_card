from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget

from memo_app import app  # V
from memo_data import *
from memo_menu_layout import *  # V
from memo_card_layout import *
from memo_edit_layout import *  # V

main_width, main_height = 1000, 450 
card_width, card_height = 600, 500 
time_unit = 1000     
    
questions_listmodel = QuestionListModel() 
frm_edit = QuestionEdit(0, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3) 
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] 
frm_card = 0 
timer = QTimer() 
win_card = QWidget() 
win_main = QWidget() 

def testlist(): 
    
    frm = Question('Столиця України??', 'apple', 'Kyiv', 'Lviv', 'Kharkiv')
    questions_listmodel.form_list.append(frm)
    frm = Question('Дім', 'house', 'horse', 'hurry', 'hour')
    questions_listmodel.form_list.append(frm)
    frm = Question('Мишка', 'mouse', 'mouth', 'muse', 'museum')
    questions_listmodel.form_list.append(frm)
    frm = Question('Число', 'number', 'digit', 'amount', 'summary')
    questions_listmodel.form_list.append(frm)

######################################     Проведення тесту    #############################################
# Підключення всіх екранів =>

app.setStyleSheet('''QWidget{
                  font-size: 30px;
}''')

testlist()
set_card()
set_main()
connects()

app.setStyleSheet('''QWidget{
                  background: lightgrey;
                  font-size: 30px;
}
                  ''')

win_main.show()
app.exec_()
