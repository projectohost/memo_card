''' Головне вікно програми '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from memo_edit_layout import layout_form  

list_questions = QListView()
wdgt_edit = QWidget()
wdgt_edit.setLayout(layout_form)
btn_add = QPushButton('Нове запитання')
btn_add.setStyleSheet(
    '''background: purple;
    color: white;
    font-size: 25px;
    '''
)

btn_delete = QPushButton('Видалити запитання')
btn_start = QPushButton('Почати тренування')

main_col1 = QVBoxLayout()
main_col1.addWidget(list_questions)
main_col1.addWidget(btn_add)
# list_questions.setStyleSheet('''background-color: navy; color: white;''')

main_col2 = QVBoxLayout()
main_col2.addWidget(wdgt_edit)
main_col2.addWidget(btn_delete)

main_line1 = QHBoxLayout()
main_line1.addLayout(main_col1)
main_line1.addLayout(main_col2)

main_line2 = QHBoxLayout()
main_line2.addStretch(1)
main_line2.addWidget(btn_start, stretch=2)
main_line2.addStretch(1)

layout_main = QVBoxLayout()
layout_main.addLayout(main_line1)
layout_main.addLayout(main_line2)

