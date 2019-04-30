import sys
# import PyQt5
from PyQt5 import QtWidgets
# from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor, QFont
# from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
# from PyQt5.QtWidgets import QCalendarWidget, QFontDialog, QColorDialog, QTextEdit, QFileDialog
# from PyQt5.QtWidgets import QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, QLineEdit, QInputDialog
import math
import diploma

class ExampleApp(QtWidgets.QMainWindow, diploma.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле fisrt.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.home()

    def check(cp, ck, cf):
        sinus = math.sqrt(1 - float(cf)**2)
        tang = sinus/float(cf)
        pk = float(ck)*float(cp)
        qp = float(pk)*float(tang)
        s = float(math.sqrt(float(pk**2)+float(qp**2)))
        x = float(s)*0.77 #if float(self.s[index])<=700 else (float(self.s[index])-700)*2.16+700*0.77
        return sinus, tang, pk, qp, s, x


    def home(self):
        self.input.setMaxLength(4)
        self.pushButton.clicked.connect(self.result_application)

        self.name = []
        self.cp = []
        self.ck = []
        self.cf = []
        # self.sin = 0
        # self.tg = 0
        # self.pk = 0
        # self.qk = 0
        # self.s = 0
        # self.x = 0
        self.sin = []
        self.tg = []
        self.pk = []
        self.qk = []
        self.s = []
        self.x = []
        with open('table') as file:  # таблица
            for line in file:
                line = line.replace("\r", "").replace("\n", "")
                try:
                    n, p, k, f = line.split(' ')
                except:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Ошибка файла!')
                    msg.setText('Введите корректные данные! В файле table значения должны быть разделены символом ; (точка с запятой)')
                    msg.setIcon(msg.Warning)
                    msg.exec()
                self.name.append(n)
                self.cp.append(p)
                self.ck.append(k)
                self.cf.append(f)
                self.sin.append(0)
                self.tg.append(0)
                self.pk.append(0)
                self.qk.append(0)
                self.s.append(0)
                self.x.append(0)


        self.TEXT_IN = QtWidgets.QLabel('Входные данные: cp-{0} ck-{1} cf-{2}'.format(self.cp[0],self.ck[0],self.cf[0]), self)
        self.TEXT_OUT_SIN = QtWidgets.QLabel('', self)
        self.TEXT_OUT_S = QtWidgets.QLabel('', self)
        self.TEXT_OUT_X = QtWidgets.QLabel('', self)


        for index, n in enumerate(self.name):
            self.comboBox.addItem(self.name[index])


        self.comboBox.activated[str].connect(self.input_change)

        self.TEXT_IN.setGeometry(10, 80, 200, 20)
        self.TEXT_OUT_SIN.setGeometry(10, 110,500 ,20)
        self.TEXT_OUT_S.setGeometry(10, 140,500 ,20)
        self.TEXT_OUT_X.setGeometry(10, 170,500 ,20)
        font = QFont()
        font.setPointSize(10)
        self.TEXT_OUT_SIN.setFont(font)
        self.TEXT_OUT_S.setFont(font)
        self.TEXT_OUT_X.setFont(font)

        self.show()

    def input_change(self):
        # value = str(QApplication.comboBox.currentText())
        index = int(self.comboBox.currentIndex())
        text_in=('Входные данные: cp-{0} ck-{1} cf-{2}'.format(self.cp[index],self.ck[index],self.cf[index]))
        self.TEXT_IN.setText(text_in)
        self.TEXT_OUT_SIN.setText('')
        self.TEXT_OUT_S.setText('')
        self.TEXT_OUT_X.setText('')

    def result_application(self):
        index = int(self.comboBox.currentIndex())
        self.sin[index] = 0
        self.tg[index] = 0
        self.pk[index] = 0
        self.qk[index] = 0
        self.s[index] = 0
        self.x[index] = 0
        try:
            hour = int(self.input.text())
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите корректные данные! Целое количество часов от 1 до 9999.')
            msg.setIcon(msg.Warning)
            msg.exec()
        self.sin[index] = math.sqrt((1 - float(self.cf[index]) * float(self.cf[index])))
        self.tg[index] = self.sin[index] / float(self.cf[index])
        self.pk[index] = float(self.ck[index])*float(self.cp[index])
        self.qk[index] = float(self.pk[index])*float(self.tg[index])
        self.s[index] = float(math.sqrt(float(self.pk[index]**2)+float(self.qk[index]**2)))
        self.x[index] = (float(self.s[index])*0.77 if float(self.s[index])<=700 else (float(self.s[index])-700)*2.16+700*0.77)*hour


        self.TEXT_OUT_SIN.setText('Sinus={0}; Tangens={1}'.format(round(self.sin[index],6),round(self.tg[index],6)))
        self.TEXT_OUT_S.setText('pk-{0} qk-{1}  итого {2} кВт/ч '.format(round(self.pk[index],4),round(self.qk[index],4),round(self.s[index],4)))
        self.TEXT_OUT_X.setText('Результат: {} сом'.format(round(self.x[index],2)))


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()