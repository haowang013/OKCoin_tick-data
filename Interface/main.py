# -*- coding: utf-8 -*-
# @author:Richard Wong
# Form implementation generated from reading ui file 'main.py'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtWidgets,QtCore
from Interface import Ui_Form
import time
import sys
import json
import server
import client
from collections import deque


class MyThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(str)

    def __init__(self,parent=None):
        super(MyThread, self).__init__()

    def run_(self,message):
        #time.sleep(1)
        self.trigger.emit(message)


class mainWindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(mainWindow,self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.StartThread)

        self.threads1 = MyThread(self)
        self.threads2 = MyThread(self)
        self.threads3 = MyThread(self)
        self.threads4 = MyThread(self)
        self.threads1.trigger.connect(self.Dataupdate1)
        self.threads2.trigger.connect(self.Dataupdate2)
        self.threads3.trigger.connect(self.Dataupdate3)
        self.threads4.trigger.connect(self.Dataupdate4)
        self.thread_no = 0

    def StartThread(self):
        while True:
            self.thread_no += 1
            data_btc = server.get_data('btc')['ticker']
            message1 = str(data_btc)
            data_ltc = server.get_data('ltc')['ticker']
            message2 = str(data_ltc)

            deq_btc = client.dataque()
            deq_ltc = client.dataque()
            message3 = str(deq_btc.average_eight('btc'))
            message4 = str(deq_ltc.average_eight('ltc'))
            self.threads1.run_(message1)
            self.threads2.run_(message2)
            self.threads3.run_(message3)
            self.threads4.run_(message4)


    def Dataupdate1(self,message):
        QtWidgets.QApplication.processEvents()
        self.textEdit.append(message)

    def Dataupdate2(self,message):
        QtWidgets.QApplication.processEvents()
        self.textEdit_2.append(message)

    def Dataupdate3(self,message):
        QtWidgets.QApplication.processEvents()
        self.textEdit_3.append(message)

    def Dataupdate4(self,message):
        QtWidgets.QApplication.processEvents()
        self.textEdit_4.append(message)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    intf = mainWindow()
    intf.show()
    sys.exit(app.exec())