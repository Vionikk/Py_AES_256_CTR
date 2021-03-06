# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab5.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# https://cryptobook.nakov.com/symmetric-key-ciphers/aes-encrypt-decrypt-examples

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMenuBar, QMenu, QMessageBox
from os import getcwd
import sys
import chilkat

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(935, 497)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 141, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 15, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 100, 141, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 180, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 200, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 10, 341, 411))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(550, 10, 341, 411))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 430, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 430, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.openfile)
        self.pushButton_2.clicked.connect(self.make)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab 5 CybSec"))
        self.label.setText(_translate("MainWindow", "Key:"))
        self.label_2.setText(_translate("MainWindow", "Initialization vector:"))
        self.label_3.setText(_translate("MainWindow", "Mode:"))
        self.radioButton.setText(_translate("MainWindow", "Encrypt"))
        self.radioButton_2.setText(_translate("MainWindow", "Decrypt"))
        self.pushButton.setText(_translate("MainWindow", "Open text"))
        self.pushButton_2.setText(_translate("MainWindow", "Run"))

    def openfile(self):
        fname = QFileDialog.getOpenFileName()[0]
        try:
            f = open(fname, 'r')
            with f:
                data = f.read()
                self.plainTextEdit.setPlainText(data)
        except FileNotFoundError:
            print('No such file')

    def make(self):
        if self.radioButton.isChecked():
            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and self.plainTextEdit.toPlainText() != "":
                text = self.plainTextEdit.toPlainText()
                key = self.lineEdit.text()
                iv = self.lineEdit_2.text()

                crypt = chilkat.CkCrypt2()
                crypt.put_CryptAlgorithm("aes")
                crypt.put_CipherMode("ctr")
                crypt.put_KeyLength(256)
                crypt.put_EncodingMode("base64")
                crypt.SetEncodedIV(iv,"ascii")
                crypt.SetEncodedKey(key,"ascii")
                encStr = crypt.encryptStringENC(text)
                self.plainTextEdit_2.setPlainText(encStr) 


            else: 
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Input data')
                msg.setWindowTitle("Error")
                msg.exec_()
        elif self.radioButton_2.isChecked():
            if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and self.plainTextEdit.toPlainText() != "":
                text = self.plainTextEdit.toPlainText()
                key = self.lineEdit.text()
                iv = self.lineEdit_2.text()
                decrypt = chilkat.CkCrypt2()
                decrypt.put_CryptAlgorithm("aes")
                decrypt.put_CipherMode("ctr")
                decrypt.put_KeyLength(256)
                decrypt.put_EncodingMode("base64")
                decrypt.SetEncodedIV(iv,"ascii")
                decrypt.SetEncodedKey(key,"ascii")
                decStr = decrypt.decryptStringENC(text)
                self.plainTextEdit_2.setPlainText(decStr) 


            else: 
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Input data')
                msg.setWindowTitle("Error")
                msg.exec_()
        else: 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Select mode')
            msg.setWindowTitle("Error")
            msg.exec_()
        
        # Error provider: 
        # msg = QMessageBox()
        # msg.setIcon(QMessageBox.Critical)
        # msg.setText("Error")
        # msg.setInformativeText('More information')
        # msg.setWindowTitle("Error")
        # msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    main()

def main():
    print("A")

# python3 lab5.py