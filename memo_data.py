from PyQt5.QtCore import*
from random import*

new_quest_templ = 'Нове запитання' 
new_answer_templ = 'Нова відповідь'

text_wrong = 'Неправильно'
text_correct = 'Правильно'

'''Цей клас зберігає інформацію про запитання, включаючи саме запитання, правильну відповідь та три неправильні варіанти.'''
class Question():
    ''' Збереження інформації про запитання'''
    def __init__(self, question=new_quest_templ, 
                answer=new_answer_templ, 
                wrong_answer1='', wrong_answer2='', 
                wrong_answer3=''):
        self.question = question # питання
        self.answer = answer # правильна відповідь
        self.wrong_answer1 = wrong_answer1 # 3 непр. варіанти
        self.wrong_answer2 = wrong_answer2 # 
        self.wrong_answer3 = wrong_answer3 #
        self.is_active = True 
        self.attempts = 0 # к-сть разів задавання питання
        self.correct = 0 # к-сть правильних відповідей
    def got_right(self):
        self.attempts += 1
        self.correct += 1
    def got_wrong(self):
        self.attempts += 1

'''Цей клас відповідає за відображення всіх віджетів, пов'язаних із запитанням.'''
class QuestionView():   # відображення всіх віджетів, що стосуються запитання
    def __init__(self, frm_model, question, 
                 answer, wrong_answer1, wrong_answer2, 
                 wrong_answer3):
        
        self.frm_model = frm_model  
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3  
    def change(self, frm_model):
        ''' обновлення даних '''
        self.frm_model = frm_model
    def show(self):
        ''' всі з об'єкта виводяться '''
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)

'''можливість редагувати запитання та відповіді.'''
class QuestionEdit(QuestionView):
    def save_question(self):
        ''' зберігає текст запитання '''
        self.frm_model.question = self.question.text()
    def save_answer(self):
        self.frm_model.answer = self.answer.text() 
    def save_wrong(self):
        self.frm_model.wrong_answer1 = self.wrong_answer1.text()
        self.frm_model.wrong_answer2 = self.wrong_answer2.text()
        self.frm_model.wrong_answer3 = self.wrong_answer3.text()
    def set_connects(self):
        self.question.editingFinished.connect(self.save_question)
        self.answer.editingFinished.connect(self.save_answer)
        self.wrong_answer1.editingFinished.connect(self.save_wrong) 
        self.wrong_answer2.editingFinished.connect(self.save_wrong)
        self.wrong_answer3.editingFinished.connect(self.save_wrong)
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.set_connects()

class AnswerCheck(QuestionView):
    
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, 
                 wrong_answer3, showed_answer, result):
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.showed_answer = showed_answer
        self.result = result

    def check(self):
        if self.answer.isChecked():
            # Якщо вибрана відповідь правильна
            self.result.setText(text_correct) # підпис правильно/неправильно
            self.showed_answer.setText(self.frm_model.answer) # правильна відповідь запитання (незалежно чи правильно/неправильно)
            self.frm_model.got_right() # зараховуємо як правильне
        else:
            # ответ неверный, запишем и отразим в статистике
            self.result.setText(text_wrong) # підпис правильно/неправильно
            self.showed_answer.setText(self.frm_model.answer) # правильна відповідь запитання (незалежно правильно/неправильно)
            self.frm_model.got_wrong() # зараховуємо як неправильне
            

'''Показує запитання у списку меню'''
class QuestionListModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.form_list = []

    def rowCount(self, index):
        return len(self.form_list)
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            form = self.form_list[index.row()]
            return form.question
        
    def insertRows(self, parent=QModelIndex()):
        position = len(self.form_list)
        self.beginInsertRows(parent, position, position) 
        self.form_list.append(Question())
        self.endInsertRows() 
        QModelIndex()
        return True 
    
    def removeRows(self, position, parent=QModelIndex()):
        self.beginRemoveRows(parent, position, position) 
        self.form_list.pop(position) 
        self.endRemoveRows()
        return True
    
    def random_question(self):
        total = len(self.form_list)
        current = randint(0, total - 1)
        return self.form_list[current]

def random_AnswerCheck(list_model, w_question, widgets_list, w_showed_answer, w_result):
    frm = list_model.random_question()
    shuffle(widgets_list)
    frm_card = AnswerCheck(frm, w_question, widgets_list[0], widgets_list[1], widgets_list[2], widgets_list[3], w_showed_answer, w_result)
    return frm_card