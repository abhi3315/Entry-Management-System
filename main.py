# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uifile.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 445)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setTextFormat(QtCore.Qt.AutoText)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setInputMask("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setMaxLength(32767)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        #
        self.lineEdit_3.setValidator(QtGui.QIntValidator()) #To take only integer input in lineEdit_3
        #
        self.lineEdit_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setMaxLength(10)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        ##########
        for x in hostname:
            self.comboBox.addItem("")
        #########
        self.horizontalLayout_6.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        ####################
        self.pushButton.clicked.connect(self.addvisitor)
        ####################
        self.horizontalLayout_7.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 27))
        self.menubar.setObjectName("menubar")
        self.menuEdit_Host = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.menuEdit_Host.setFont(font)
        self.menuEdit_Host.setObjectName("menuEdit_Host")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_New_Host = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Host.setObjectName("actionAdd_New_Host")
        self.actionVisitor_History = QtWidgets.QAction(MainWindow)
        self.actionVisitor_History.setObjectName("actionVisitor_History")
        self.actionVisitor_History_2 = QtWidgets.QAction(MainWindow)
        self.actionVisitor_History_2.setObjectName("actionVisitor_History_2")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuEdit_Host.addAction(self.actionAdd_New_Host)
        self.menuEdit_Host.addSeparator()
        self.menuEdit_Host.addAction(self.actionVisitor_History)
        self.menuEdit_Host.addAction(self.actionVisitor_History_2)
        self.menuEdit_Host.addSeparator()
        self.menuEdit_Host.addAction(self.actionExit)
        self.menubar.addAction(self.menuEdit_Host.menuAction())

        ############
        self.menubar.triggered[QtWidgets.QAction].connect(self.menu)
        #############

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; text-decoration: underline;\">ENTRY MANAGEMENT SYSTEM</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Visitor Details</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Name :"))
        self.label_3.setText(_translate("MainWindow", "Email :"))
        self.label_4.setText(_translate("MainWindow", "Phone :"))
        self.label_5.setText(_translate("MainWindow", "Checkin Time :"))
        self.label_7.setText(_translate("MainWindow", "Select Host :"))
        ##########
        i=0
        for x in hostname:
            self.comboBox.setItemText(i, _translate("MainWindow",x[0]))
            i=i+1
        ##########
        self.pushButton.setText(_translate("MainWindow", "Add Visitor Details"))
        self.menuEdit_Host.setTitle(_translate("MainWindow", "MENU"))
        self.actionAdd_New_Host.setText(_translate("MainWindow", "Add New Host"))
        self.actionVisitor_History.setText(_translate("MainWindow", "Pending Visitors"))
        self.actionVisitor_History_2.setText(_translate("MainWindow", "Visitors History"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

##################function definition#####################

    def menu(self,action):
        txt=(action.text())

        if txt=='Add New Host':
            from addhost import Ui_Dialog
            Dialog=QtWidgets.QDialog()
            ui=Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()

        if txt=='Visitors History':
            from history import Ui_Dialog
            Dialog=QtWidgets.QDialog()
            ui=Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()

        if txt=='Pending Visitors':
            from pendingvisitor import Ui_Dialog
            Dialog=QtWidgets.QDialog()
            ui=Ui_Dialog()
            ui.setupUi(Dialog)
            ret=Dialog.exec()

        if txt=='Exit':
            self.close()
            
    def addvisitor(self):
        name=self.lineEdit.text()
        email=self.lineEdit_2.text()
        phone=self.lineEdit_3.text()
        if (name!='' and email!='' and phone!=''):
            email=self.checkmail(email)
            if email!=0:
                dateTime=datetime.now()
                checkin=dateTime.strftime("%H:%M")
                self.lineEdit_4.setText(str(checkin))
                timestamp=dateTime.strftime("%d-%b-%Y (%H:%M:%S)")
                hostname=self.comboBox.currentText()
                sql="INSERT INTO tblvisitors (name,email,phone,checkinTime,entryTimeStamp,host) VALUES('"+name+"','"+email+"','"+phone+"','"+checkin+"','"+timestamp+"','"+hostname+"');"
                try:
                    sql1="SELECT Email,Phone from tblhosts WHERE Name='"+hostname+"';"
                    cur=db.execute(sql1)
                    hostcon=cur.fetchall()
                    from sendmailhost import send_mail_host
                    from sendsmshost import send_sms_host
                    self.showdlg("Data added successfully.\nAn mail and SMS are sending to Host.\nPlease wait...")
                    send_mail_host(hostcon[0][0],name,checkin,phone,email)
                    cur=db.execute(sql)
                    db.commit()
                    send_sms_host(str(hostcon[0][1]),name,checkin,phone,email)
                except:
                    self.showdlg("Error in operation!")
                    cur.rollback()
            else:
                self.showdlg("Enter a valid email.")
        else:
            self.showdlg("Data field can not be empty.")


    def checkmail(self,mail):
        if '@' in mail and '.com' in mail:
            return mail
        else:
            return 0
        
    
    def showdlg(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("Pop up!")
        ret=Dialog.exec()
        
if __name__ == "__main__":
    import sqlite3
    db=sqlite3.connect('managementsys.db')
    cur=db.cursor()
    sql="SELECT Name FROM tblhosts;"
    cur=db.execute(sql)
    hostname=cur.fetchall()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


