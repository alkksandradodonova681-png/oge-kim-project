# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dbpage.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(761, 911)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 90, 281, 31))
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(250, 10, 256, 41))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(200, 140, 111, 31))
        self.textBrowser_4 = QTextBrowser(self.centralwidget)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(30, 140, 161, 31))
        self.textBrowser_5 = QTextBrowser(self.centralwidget)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(30, 200, 171, 31))
        self.textBrowser_6 = QTextBrowser(self.centralwidget)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(30, 260, 131, 31))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(210, 200, 101, 31))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(170, 260, 141, 31))
        self.textBrowser_7 = QTextBrowser(self.centralwidget)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(30, 320, 131, 31))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(170, 320, 141, 31))
        self.textBrowser_8 = QTextBrowser(self.centralwidget)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(30, 440, 281, 31))
        self.textBrowser_9 = QTextBrowser(self.centralwidget)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(400, 90, 256, 31))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 810, 81, 26))
        self.lineEdit_5 = QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(400, 140, 113, 26))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(400, 180, 81, 26))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 500, 281, 131))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(650, 810, 81, 26))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 640, 281, 91))
        self.label.setAcceptDrops(True)
        self.label.setStyleSheet(u"border: 1px dashed gray;")
        self.label_answer = QLabel(self.centralwidget)
        self.label_answer.setObjectName(u"label_answer")
        self.label_answer.setGeometry(QRect(400, 640, 281, 91))
        self.label_answer.setAcceptDrops(True)
        self.label_answer.setStyleSheet(u"border: 1px dashed gray;")
        self.textBrowser_10 = QTextBrowser(self.centralwidget)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setGeometry(QRect(30, 380, 131, 31))
        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(170, 380, 141, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 761, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u043d\u0438\u0435:</p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:700;\">\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u0431\u0430\u0437\u043e\u0439 \u0434\u0430\u043d\u043d\u044b\u0445</span></p></body></html>", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"MATH-OGE", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"PHYS-OGE", None))

        self.textBrowser_4.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442:</p></body></html>", None))
        self.textBrowser_5.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u0434\u0430\u043d\u0438\u044f \u043f\u043e \u043f\u043e\u0440\u044f\u0434\u043a\u0443:</p></body></html>", None))
        self.textBrowser_6.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u043e\u043c\u0435\u0440 \u043f\u0440\u043e\u0442\u043e\u0442\u0438\u043f\u0430:</p></body></html>", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0432\u043e\u0434 \u2116 \u043f/\u043f", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0432\u043e\u0434 \u2116 \u043f\u0440\u043e\u0442\u043e\u0442\u0438\u043f\u0430", None))
        self.textBrowser_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u043b\u043e\u0436\u043d\u043e\u0441\u0442\u044c:</p></body></html>", None))
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))

        self.textBrowser_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0435\u043a\u0441\u0442 \u0437\u0430\u0434\u0430\u043d\u0438\u044f:</p></body></html>", None))
        self.textBrowser_9.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u043d\u0438\u0435(\u043f\u043e \u0443\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u043c\u0443 ID):</p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043d\u0438\u043a\u0430\u043b\u044c\u043d\u044b\u0439 ID ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0442\u0435\u043a\u0441\u0442 \u0437\u0430\u0434\u0430\u043d\u0438\u044f</p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u0433\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430(\u0435\u0441\u043b\u0438 \u043d\u0430\u0434\u0430->\u043f\u0435\u0440\u0435\u0442\u0430\u0449\u0438\u0442\u044c png)", None))
        self.label_answer.setText(QCoreApplication.translate("MainWindow", u"\u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0430 \u043e\u0442\u0432\u0435\u0442\u0430(\u0435\u0441\u043b\u0438 \u043d\u0430\u0434\u0430->\u043f\u0435\u0440\u0435\u0442\u0430\u0449\u0438\u0442\u044c png)", None))
        self.textBrowser_10.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0422\u0438\u043f \u043e\u0442\u0432\u0435\u0442\u0430:</p></body></html>", None))
        self.comboBox_3.setItemText(0, "")
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"multiple_choice", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"short_answer", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"extended_answer", None))

    # retranslateUi

