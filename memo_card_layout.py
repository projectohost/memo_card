''' Вікно для карточки запитання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from memo_app import app 

# mainWindow = QWidget()

btn_Menu = QPushButton('Меню')
btn_Sleep = QPushButton('Побити байдики') 
box_Minutes = QSpinBox() 
box_Minutes.setValue(30)
btn_OK = QPushButton('Відповісти')
lb_Question = QLabel('Запитання?')

RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup() 

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 

RadioGroupBox.setLayout(layout_ans1) 
AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('Правильно/неправильно') 
lb_Correct = QLabel('Правильна відповідь!') 

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=Qt.AlignCenter)
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
layout_line4 = QHBoxLayout() 

layout_line1.addWidget(btn_Menu)
layout_line1.addWidget(btn_Sleep)
layout_line1.addStretch(1) 
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('секунд')) 

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2) 
layout_line4.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    ''' показати панель відповідей '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Наступне запитання')

def show_question():
    ''' показати панель запитань '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Відповісти')
    
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

# app.setStyleSheet('QWidget{font-size: 35px;}')

# mainWindow.setLayout(layout_card)
# mainWindow.show()
# app.exec()