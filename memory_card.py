from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, randint

class Qeustions():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

quest_list = list()
quest_list.append(Qeustions('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Брзильский'))
quest_list.append(Qeustions('Какого цвета нет на флаге России', 'Зелёный', 'Белый', 'Красный', 'Синий'))
quest_list.append(Qeustions('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))


app = QApplication([])
window = QWidget()

btn_ok = QPushButton('Ответить')
lb_ques = QLabel('Какой то вопрос')

radio_group_box = QGroupBox("Варианты ответиков")

btn_1 = QRadioButton('Вариант 1')
btn_2 = QRadioButton('Вариант 2')
btn_3 = QRadioButton('Вариант 3')
btn_4 = QRadioButton('Вариант 4')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(btn_1)
layout_ans2.addWidget(btn_2)
layout_ans3.addWidget(btn_3)
layout_ans3.addWidget(btn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radio_group_box.setLayout(layout_ans1)

ans_group = QGroupBox("Результатики")
lb_result = QLabel("прав ты или нет?")
lb_correct = QLabel("ответ будет тут")

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment = Qt.AlignHCenter, stretch = 2)
ans_group.setLayout(layout_res)

lay_line1 = QHBoxLayout()
lay_line2 = QHBoxLayout()
lay_line3 = QHBoxLayout()

lay_line1.addWidget(lb_ques, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

lay_line2.addWidget(radio_group_box)
lay_line2.addWidget(ans_group)
ans_group.hide()

lay_line3.addStretch(1)
lay_line3.addWidget(btn_ok, stretch = 2)
lay_line3.addStretch(1)

lay_card = QVBoxLayout()

lay_card.addLayout(lay_line1, stretch = 2)
lay_card.addLayout(lay_line2, stretch = 8)
lay_card.addStretch(1)
lay_card.addLayout(lay_line3, stretch = 1)
lay_card.addStretch(1)
lay_card.setSpacing(5)

def show_result():
    radio_group_box.hide()
    ans_group.show()
    btn_ok.setText("Следующий вопрос")

def show_quest():
    radio_group_box.show()
    ans_group.hide()
    btn_ok.setText("Ответить")
    btn_1.setChecked(False)
    btn_2.setChecked(False)
    btn_3.setChecked(False)
    btn_4.setChecked(False)
 
answer = [btn_1, btn_2, btn_3, btn_4]

def ask(q: Qeustions):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_ques.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_quest()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct("Ты ответил правильно😘")
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
        
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct("Ты ответил не правильно, мистер лох")
            print('Рейтинг: ', (window.score/window.total*100), '%')

def next_quest():
    window.total += 1
    print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
    cur_question = randint(0, len(quest_list) - 1)
    q = quest_list[cur_question]
    ask(q)

def click_OK():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_quest()

window.setLayout(lay_card)
window.resize(700,300)
window.setWindowTitle('Memory Card')

window.score = 0
window.total = 0

btn_ok.clicked.connect(click_OK)
next_quest()

window.show()
app.exec()
